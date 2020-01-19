## New Story
* ask_weather
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* ask_weather{"city":"delhi"}
    - slot{"city":"delhi"}
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}

## basic answer weather
* ask_weather
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}

## New Story
* ask_weather{"city": "Seoul", "date":"19/12/2019", "time": "17:42"}
    - slot{"city":"delhi"}
    - slot{"date":"19/12/2019"}
    - slot{"time": "17:42"}
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* ask_weather
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}

## New Story
* greet
    - select_action
* ask_weather
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* ask_weather{"city":"london"}
    - slot{"city":"london"}
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* thanks
    - utter_noworries

## New Story
* greet
    - select_action
* ask_weather
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* ask_weather{"time":"9pm"}
    - slot{"time":"9pm"}
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}

## New Story
* greet
    - select_action
* ask_weather{"city": "Seoul", "time": "9pm"}
    - slot{"city": "Seoul"}
    - slot{"time": "9pm"}
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* goodbye
    - utter_goodbye

## New Story
* ask_weather
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* ask_weather{"city":"delhi"}
    - slot{"city":"delhi"}
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* ask_weather{"date":"tomorrow"}
    - slot{"date":"tomorrow"}
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* goodbye
    - utter_goodbye

## New Story
* ask_weather{"status":"temperature","date":"today"}
    - slot{"date":"today"}
    - slot{"status":"temperature"}
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* ask_weather{"city":"moscow"}
    - slot{"city":"moscow"}
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}
* thanks
    - utter_noworries

## interactive_story_1
* ask_weather{"city": "Seoul", "date":"17 Dec", "time": "9pm"}
    - slot{"city": "Seoul"}
    - slot{"time": "9pm"}
    - answer_weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
    - form{"name": null}

## say goodbye
* goodbye
  - utter_goodbye

## out_of_scope
* out_of_scope
    - utter_sorry

## New Story

* ask_weather{"city":"Seoul","day_of_week":"Thursday"}
    - slot{"city":"Seoul"}
    - slot{"day_of_week":"Thursday"}
    - answer_weather_form
    - form{"name":"answer_weather_form"}
    - slot{"city":"Seoul"}
    - slot{"city":"Seoul"}
    - slot{"day_of_week":null}
    - slot{"date":"19/12/2019"}
    - slot{"time":"09:25"}
    - form{"name":null}
    - slot{"requested_slot":null}
* ask_weather{"day_of_week":"Friday","time":"9pm"}
    - slot{"day_of_week":"Friday"}
    - slot{"time":"9pm"}
    - answer_weather_form
    - form{"name":"answer_weather_form"}
    - slot{"city":"Seoul"}
    - slot{"day_of_week":null}
    - slot{"date":"20/12/2019"}
    - slot{"time":"21:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
* ask_weather{"city":"Delhi"}
    - slot{"city":"Delhi"}
    - answer_weather_form
    - form{"name":"answer_weather_form"}
    - slot{"city":"Delhi"}
    - slot{"city":"Delhi"}
    - slot{"day_of_week":null}
    - slot{"date":"20/12/2019"}
    - slot{"time":"21:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
* ask_weather{"date":"today"}
    - slot{"date":"today"}
    - answer_weather_form
    - form{"name":"answer_weather_form"}
    - slot{"city":"Delhi"}
    - slot{"day_of_week":null}
    - slot{"date":"17/12/2019"}
    - slot{"time":"21:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_noworries

## New Story

* ask_weather{"day_of_week":"Saturday"}
    - slot{"day_of_week":"Saturday"}
    - answer_weather_form
    - form{"name":"answer_weather_form"}
    - slot{"requested_slot":"city"}
* ask_weather{"city":"Seoul"}
    - slot{"city":"Seoul"}
    - answer_weather_form
    - slot{"city":"Seoul"}
    - slot{"day_of_week":null}
    - slot{"date":"21/12/2019"}
    - slot{"time":"10:26"}
    - form{"name":null}
    - slot{"requested_slot":null}
* ask_weather{"date":"now"}
    - slot{"date":"now"}
    - answer_weather_form
    - form{"name":"answer_weather_form"}
    - slot{"city":"Seoul"}
    - slot{"day_of_week":null}
* ask_weather{"time":"9pm"}
    - slot{"time":"9pm"}
    - answer_weather_form
    - form{"name":"answer_weather_form"}
    - slot{"city":"Seoul"}
    - slot{"day_of_week":null}
    - slot{"date":"17/12/2019"}
    - slot{"time":"21:00"}
    - form{"name":null}
    - slot{"requested_slot":null}
* ask_weather{"date":"now"}
    - slot{"date":"now"}
    - answer_weather_form
    - form{"name":"answer_weather_form"}
    - slot{"city":"Seoul"}
    - slot{"day_of_week":null}
    - slot{"date":"17/12/2019"}
    - slot{"time":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_noworries

## New Story

* greet{"name":"Indong"}
    - slot{"name":"Indong"}
    - select_action

## New Story

* greet
    - select_action
* greet{"name":"himanshu"}
    - slot{"name":"himanshu"}
    - select_action
* ask_weather{"city":"Delhi"}
    - slot{"city":"Delhi"}
    - answer_weather_form
    - form{"name":"answer_weather_form"}
    - slot{"city":"Delhi"}
    - slot{"city":"Delhi"}
    - slot{"day_of_week":null}
    - slot{"date":"17/12/2019"}
    - slot{"time":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_noworries
* ask_weather{"city":"Noida"}
    - slot{"city":"Noida"}
    - answer_weather_form
    - form{"name":"answer_weather_form"}
    - slot{"city":"Noida"}
    - slot{"city":"Noida"}
    - slot{"day_of_week":null}
    - slot{"date":"17/12/2019"}
    - slot{"time":null}
    - form{"name":null}
    - slot{"requested_slot":null}
* thanks
    - utter_noworries
* goodbye
    - utter_goodbye
