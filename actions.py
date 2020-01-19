from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
import requests, json
from datetime import date, datetime, timedelta
import re
import enum


# about config #
key = '1ea75a1b36c46e434d533c244d0d8c35'
url_today = 'http://api.openweathermap.org/data/2.5/weather?'
url_5days = 'http://api.openweathermap.org/data/2.5/forecast?'

# about date #
weekday = {
    'Mon': 0, 'Monday': 0, 'mon': 0, 'monday': 0,
    'Tuesday': 1, 'Tue': 1, 'tuesday': 1, 'tue': 1,
    'wednesday': 2, 'Wednesday': 2, 'wed': 2, 'Wed': 2,
    'thursday': 3, 'Thursday': 3, 'thu': 3, 'Thu': 3,
    'Friday': 4, 'Fri': 4, 'friday': 4, 'fri': 4,
    'Saturday': 5, 'saturday': 5, 'Sat': 5, 'sat': 5,
    'Sunday': 6, 'sunday': 6, 'Sun': 6, 'sun': 6,
}
emojies = {'cloud': '☁️', 'rain': '☔', 'snow': '❄️', 'clear': '☀️'}
comments = {'cloud': 'The sky covers itself with its blanket☁️  :)', 
        'rain': 'I hope the sounds of raindrop🌧️  are beautiful. Don\'t forget to take your umbrella🌂 !',
        'snow': 'Olaf⛄  of Arendelle wanna hang out with you!',
        'clear': 'May the bright light🔆  be with you.'}

time_exp = re.compile('(\d+)[:\s]?(\d*)[\s]?([pPaA][\.]?[mM][\.]?)?')
date_exp = re.compile('(\d+)[/\.\-](\d+)[/\.\-]?(\d*)?')
string_date_of_exp = re.compile('(\d+\w*)[\s](of)[\s](\w+\.?)', re.IGNORECASE)
string_date_exp = re.compile('(\w+\.?)[\s](\d+\w*)', re.IGNORECASE)

# custom acitons #
def _string_month_to_num(month):
    return Month[month].value


def date_formating(value):
    result = str(value) if value >= 10 else '0' + str(value)
    return result


class Month(enum.Enum):
    January = '01'
    Jan = '01'
    February = '02'
    Feb = '02'
    March = '03'
    Mar = '03'
    April = '04'
    Apr = '04'
    May = '05'
    June = '06'
    Jun = '06'
    July = '07'
    Jul = '07'
    August = '08'
    Aug = '08'
    September = '09'
    Sep = '09'
    October = '10'
    Oct = '10'
    November = '11'
    Nov = '11'
    December = '12'
    Dec = '12'


class SelectAction(Action):

    def name(self) -> Text:
        return "select_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):

        buttons = [
            {"title": "Current Weather",
            "payload":"/ask_weather{\"date\": \"today\"}"},
            {"title": "Tomorrow's Forecast",
            "payload": "/ask_weather{\"date\": \"tomorrow\"}"},
        ]
        name = tracker.slots.get('name')
        if name:
            dispatcher.utter_button_message(f"Hi {name}! I'm Wenny can tell you weather information. What are you looking for?", buttons)
        else:
            # TODO: update rasa core version for configurable `button_type`
            dispatcher.utter_button_template("utter_greet", buttons, tracker)
        return []


class AnswerWeatherForm(FormAction):

    def name(self) -> Text:
        return "answer_weather_form"

    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["city"]


    def find_weather_info(self, idx, city, target_date):
        response = requests.get(url_5days + f'q={city}&APPID={key}').text
        weather = json.loads(response)
        if weather.get('cod') == '404':
            return {'text': f'Sorry, I couldn\'t find weather infomation in {city}. Would you give me a correct name of the city?'}
            
        
        if weather:
            city = weather.get('city').get('name')
            description = weather.get('list')[idx].get('weather')[0].get('description')
            comment = 'Have a nice day!'
            for des, emoji in emojies.items():
                if des in description:
                    description += emoji
                    comment = comments.get(des)
            temperature = int(weather.get('list')[idx].get('main').get('temp')) - 273.15
            humidity = weather.get('list')[idx].get('main').get('humidity')
            wind = weather.get('list')[idx].get('wind').get('speed')
            rain = weather.get('list')[idx].get('rain')
            snow = weather.get('list')[idx].get('snow')
            clouds = weather.get('list')[idx].get('clouds')

        return {'text': f'Datetime: {date_formating(target_date.month)}/{date_formating(target_date.day)}/{target_date.year} {date_formating(target_date.hour)}:{date_formating(target_date.minute)}\nCity: {city}\nWeather: {description}\nTemperature: {temperature:0.1f}°C\nHumidity: {humidity}\nWind: {wind}m/s.\n{comment}',
            'city': city,
            'description': description,
            'temperature': temperature,
            'humidity': humidity,
            'wind': wind,
            'rain': rain,
            'snow': snow,
            'clouds': clouds,
            }
        

    def find_time_idx(self, date, time, day_of_week):
        def calc_hour(nor, hour_idx):
            min_idx = hour_idx + 1
            pm_idx = hour_idx + 2
            hour = int(nor.group(hour_idx))
            if not nor.group(min_idx):
                minute = 0
            else:
                minute = int(nor.group(min_idx))
            if nor.group(pm_idx) and nor.group(pm_idx)[0].lower() == 'p':
                hour += 12
            return hour, minute


        now = datetime.now()
        if type(date) == str:
            chk_date_time = date_exp.match(date)
            chk_string_date = string_date_exp.match(date)
            chk_string_date_of = string_date_of_exp.match(date)
            if chk_date_time and not chk_string_date and not chk_string_date_of:
                day = int(chk_date_time.group(2))
                month = int(chk_date_time.group(1))
                if not chk_date_time.group(3):
                    if month < now.month:
                        year = now.year + 1
                    else:
                        year = now.year
                else:
                    year = int(chk_date_time.group(3))
            elif chk_string_date and not chk_string_date_of:
                day = chk_string_date.group(2)
                month = int(_string_month_to_num(chk_string_date.group(1)))
                if month < now.month:
                    year = now.year + 1
                else:
                    year = now.year
                if day.isdigit():
                    day= int(day)
                else:
                    day = int(day[:-2])
            elif chk_string_date_of:
                day = chk_string_date_of.group(3)
                month = int(_string_month_to_num(chk_string_date_of.group(1)))
                if month < now.month:
                    year = now.year + 1
                else:
                    year = now.year
                if day.isdigit():
                    day= int(day)
                else:
                    day = int(day[:-2]) 
        
        if type(time) == str:
            chk_time = time_exp.search(time)
            if chk_time:
                hour, minute = calc_hour(chk_time, 1)
        if not date or date == 'today' or date == 'now':
            year = now.year
            month = now.month
            day = now.day
        elif date == 'tomorrow':
            tmr = now + timedelta(days=1)
            year = tmr.year
            month = tmr.month
            day = tmr.day
        if not time or date == 'now':
            hour = now.hour
            minute = now.minute

        try:
            today = datetime(now.year, now.month, now.day, now.hour, now.minute)     
            if day_of_week:
                wkday = weekday[day_of_week]
                current_week = now.weekday()
                if wkday < current_week:
                    wkday += 7
                diff = wkday - current_week
                target = datetime(now.year, now.month, now.day, hour, minute) + timedelta(days=diff)
            else:
                target = datetime(year, month, day, hour, minute)
            delta = target - today
            idx = int(round((delta.seconds / (60 ** 2)) / 3) + (delta.days * 8)) 
            if target < today or idx >= 40:
                return "IMPOSSIBLE", None
            return idx, target
        except:
            return None, None
            

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:

        city = tracker.slots.get('city')
        date = tracker.slots.get('date')
        time = tracker.slots.get('time')
        status = tracker.slots.get('status')
        day_of_week = tracker.slots.get('day_of_week')
        
        idx, target_date = self.find_time_idx(date, time, day_of_week)
        if target_date != None:
            searched_date = f'{date_formating(target_date.month)}/{date_formating(target_date.day)}/{target_date.year}'
            searched_time = f'{date_formating(target_date.hour)}:{date_formating(target_date.minute)}'
            now = datetime.now()
            today = datetime(now.year, now.month, now.day, now.hour, now.minute)
            if status:
                response = self.find_weather_info(idx, city, target_date)
                if status == 'snow':
                    snow = response.get('snow')
                    if snow:
                        hourly = snow.get('1h')
                        if target_date == today:
                            dispatcher.utter_message(text=f'It\'s snowing in {city}. {hourly}mm/hour. Please be careful for slippery floor!')
                        else:
                            dispatcher.utter_message(text=f'It will snow in {city} at {searched_date} {searched_time}. {hourly}mm/hour. Please be careful for slippery floor!')
                    else:
                        if target_date == today:
                            dispatcher.utter_message(text=f'It\'s not snowing in {city}!')
                        else:
                            dispatcher.utter_message(text=f'It will not snow in {city} at {searched_date} {searched_time}!')
                elif status == 'rain':
                    rain = response.get('rain')
                    if rain:
                        hourly = rain.get('1h')
                        if target_date == today:
                            dispatcher.utter_message(text=f'It\'s raining in {city}. {hourly}mm/hour. please take your umbrella!')
                        else:
                            dispatcher.utter_message(text=f'It will rain in {city} at {searched_date} {searched_time}. {hourly}mm/hour. please take your umbrella!')
                    else:
                        if target_date == today:
                            dispatcher.utter_message(text=f'It\'s not raining in {city}!')
                        else:
                            dispatcher.utter_message(text=f'It will not rain in {city} at {searched_date} {searched_time}!')
                elif status == 'clear':
                    clear = response.get('description')
                    if 'clear' in clear:
                        if target_date == today:
                            dispatcher.utter_message(text=f'It\'s a nice day!')
                        else:
                            dispatcher.utter_message(text=f'It will be a nice day!')
                    else:
                        dispatcher.utter_message(text=f'It seems cloudy.')
                elif status == 'temperature':
                    temperature = response.get('temperature')
                    dispatcher.utter_message(text=f'{searched_date} {searched_time} {city}\'s temperature is {temperature:0.1f}°C')
                elif status == 'wind':
                    wind = self.find_weather_info(0, city, target_date).get('wind')
                    dispatcher.utter_message(text=f'{searched_date} {searched_time} {city}\'s wind speed is {wind}m/s')
                elif status == 'humidity':
                    humidity = response.get('humidity')
                    dispatcher.utter_message(text=f'{searched_date} {searched_time} {city}\'s wind humidity is {humidity}m/s')
                if target_date == today:
                    return [SlotSet("status", None), SlotSet("day_of_week", None), SlotSet("date", searched_date), SlotSet("time", None)]
                return [SlotSet("status", None), SlotSet("day_of_week", None), SlotSet("date", searched_date), SlotSet("time", searched_time)]

            if idx != None and idx != 'IMPOSSIBLE':
                dispatcher.utter_message(text=self.find_weather_info(idx, city, target_date).get('text'))
                if target_date == today:
                    print(target_date == today)
                    return [SlotSet("day_of_week", None), SlotSet("date", searched_date), SlotSet("time", None)]
                return [SlotSet("day_of_week", None), SlotSet("date", searched_date), SlotSet("time", searched_time)]
        if date == 'historical' or idx == 'IMPOSSIBLE':
            dispatcher.utter_message(text=f'I\'m really sorry:( I can\'t find weather information at this time.')
            return [SlotSet("time", None)]
        
        return []

