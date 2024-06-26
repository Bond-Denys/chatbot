import datetime
import random
import math

topic_history = []

comments = [
    "",
    "Цікавий вибір! ",
    "Супер! Я також люблю цю тему!😀 ",
    "Гарний вибір теми😎 ",
    "Тривіальний вибір☹ ",
    "Чудово! ",
    "Прекрасний вибір! "
]


def quotation():
    quotation_answer = """5 надихаючих цитат:
1. Успіх — це вміння рухатись від невдачі до невдачі, не втрачаючи ентузіазму. (Вінстон Черчилль)
2. Життя без стресу — це смерть. (Ганс Сельє)
3. У мене немає особливого таланту, я просто дуже допитливий. (Альберт Ейнштейн)
4. Гроші з’являються, коли ви займаєтеся правильною справою. (Майк Філліпс)
5. Освіта — це розпалювання полум'я, а не наповнення посудини. (Сократ)"""
    print_response(quotation_answer)
    chat_storage(input_text, quotation_answer)
    topics_reply()
    return


def carol_5():
    carol_5_answer = """«Вифлеємська зірка сяє»
Вифлеємська зірка сяє
Та з Різдвом усіх вітає!
Годі, люди, нам жаліться!
Посміхніться, обійміться!
Бо Різдвяний світлий час
В душі загляда до вас!
І, коли там, раптом, пусто –
Не поможе і капуста!
То нехай же розквіта
В душах світла доброта,
Зможете тоді все мати,
Що могли би побажати!
Ми бажаємо вам щиро
Злагоди, достатку, миру!
Тож з добром нас відпустіть
І щось в торбу покладіть!"""
    print_response(carol_5_answer)
    response_carol = f"""Ви обрали тему: "{get_current_topic()}". Я можу заспівати 5 різних колядок. Обирайте, яка 
Вам до душі: «{"», «".join(topics_dictionary["загальні"]["колядки"].keys())}»."""
    print_response(response_carol)
    chat_storage(input_text, f"""{carol_5_answer}
 {response_carol}""")
    return


def carol_4():
    carol_4_answer = """«Колядуєм, колядуєм»
Колядуєм, колядуєм!
Наша зіронька віщує,
Що у вашій всій господі
І в саду, і на городі,
Буде щедрий урожай!
І шумітиме, як гай,
Слава про усю родину
Ген на всеньку Україну!
Буде вдосталь хліба, солі,
Масла, ковбаси, квасолі
І гороху, бо у нас
Не такий доступний газ!
Буде все, чого вам треба!
Каже зіронька із неба,
Тільки ви тим не гордіться,
А із нами поділіться!"""
    print_response(carol_4_answer)
    response_carol = f"""Ви обрали тему: "{get_current_topic()}". Я можу заспівати 5 різних колядок. Обирайте, яка 
Вам до душі: «{"», «".join(topics_dictionary["загальні"]["колядки"].keys())}»."""
    print_response(response_carol)
    chat_storage(input_text, f"""{carol_4_answer}
 {response_carol}""")
    return


def carol_3():
    carol_3_answer = """«Ой на річці, на Йордані»
Ой на річці, на Йордані,
Там Пречиста ризи прала,
Свого сина сповивала,
На ялині колихала.
Прилетіли три янголи,
Взяли Христа під небеса.
Всі небеса розтворилися,
Всім святим поклонилися."""
    print_response(carol_3_answer)
    response_carol = f"""Ви обрали тему: "{get_current_topic()}". Я можу заспівати 5 різних колядок. Обирайте, яка 
Вам до душі: «{"», «".join(topics_dictionary["загальні"]["колядки"].keys())}»."""
    print_response(response_carol)
    chat_storage(input_text, f"""{carol_3_answer}
     {response_carol}""")
    return


def carol_2():
    carol_2_answer = """«Віє вітер з гір»
Віє вітер з гір
Та до вас у двір,
Проситься до хати
Заколядувати.
Ви його почуйте,
Смакоту готуйте!
Бога прославляйте,
Нас не забувайте!"""
    print_response(carol_2_answer)
    response_carol = f"""Ви обрали тему: "{get_current_topic()}". Я можу заспівати 5 різних колядок. Обирайте, яка 
Вам до душі: «{"», «".join(topics_dictionary["загальні"]["колядки"].keys())}»."""
    print_response(response_carol)
    chat_storage(input_text, f"""{carol_2_answer}
 {response_carol}""")
    return


def carol_1():
    carol_1_answer = """«Під ногами сніг рипучий»
Під ногами сніг рипучий,
Вітер стріхи обміта:
Нині день ясний, блискучий —
День Народження Христа!"""
    print_response(carol_1_answer)
    response_carol = f"""Ви обрали тему: "{get_current_topic()}". Я можу заспівати 5 різних колядок. Обирайте, яка 
Вам до душі: «{"», «".join(topics_dictionary["загальні"]["колядки"].keys())}»."""
    print_response(response_carol)
    chat_storage(input_text, f"""{carol_1_answer}
 {response_carol}""")
    return


def your_name():
    print_response("Як Вас звати?")
    chat_storage(get_current_topic(), "Як Вас звати?")
    a = get_user_input()
    your_name_answer = f"""Приємно познайомитись, {a}, а я Цезар,
віртуальний співрозмовник і можу відповідати на питання з певних шкільних предметів))"""
    print_response(your_name_answer)
    chat_storage(a, your_name_answer)
    topics_reply()
    return


def month():
    now = datetime.datetime.now()
    mon = now.month
    month_answer = f"Поточний місяць: {mon}"
    print_response(month_answer)
    chat_storage(input_text, month_answer)
    topics_reply()
    return


def new_year():
    now = datetime.datetime.now()
    n_year = datetime.datetime(now.year + 1, 1, 1)
    delta = n_year - now
    new_year_answer = f"До Нового Року залишилося: {delta.days} днів."
    print_response(new_year_answer)
    chat_storage(input_text, new_year_answer)
    topics_reply()
    return


def time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time_answer = f"Поточний час = {current_time}."
    print_response(time_answer)
    chat_storage(input_text, time_answer)
    topics_reply()
    return


def noun_genders():
    noun_genders_answer = """Українські іменники в однині належать до
чоловічого, жіночого, середнього та спільного роду."""
    print_response(noun_genders_answer)
    chat_storage(input_text, noun_genders_answer)
    topics_reply()
    return


def ukrainian_declension():
    ukrainian_declension_answer = """В українській мові сім відмінків, кожен з яких відповідає на певне питання:
Називний (Н. в.) — Хто? Що?
Родовий (Р. в.) — Кого? Чого?
Давальний (Д. в.) — Кому? Чому?
Знахідний (3. в.) — Кого? Що?
Орудний (Ор. в.) — Ким? Чим?
Місцевий (М. в.) — На кому? На чому?
Кличний (Кл. в.) — іменники виступають звертанням."""
    print_response(ukrainian_declension_answer)
    chat_storage(input_text, ukrainian_declension_answer)
    topics_reply()
    return


def planets_distance():
    planets_distance_answer = f"""Відстань між Землею та Сонцем не є статичною, вона змінюється в залежності від їх
положення відносно один до одного. Але середня відстань становить близько 149,6 мільйонів кілометрів."""
    print_response(planets_distance_answer)
    chat_storage(input_text, planets_distance_answer)
    topics_reply()
    return


def influence_health():
    influence_health_answer = """Правильне дозування зоряного світла може бути корисним для здоров'я.
Однак, при тривалому впливі зоряного світла на шкіру, можливі негативні наслідки. 
Занадто тривалий час під сонцем може призвести до опіків, передчасного старіння шкіри і т.д."""
    print_response(influence_health_answer)
    chat_storage(input_text, influence_health_answer)
    topics_reply()
    return


def planets_orbit():
    planets_orbit_answer = """Найбільша орбіта в Сонячній системі належить до планети Нептун,
який знаходиться в середньому на відстані близько 4,5 мільярда кілометрів від Сонця.
Найменша орбіта в Сонячній системі належить планеті Меркурій, який знаходиться
в середньому на відстані близько 58 мільйонів кілометрів від Сонця. """
    print_response(planets_orbit_answer)
    chat_storage(input_text, planets_orbit_answer)
    topics_reply()
    return


def cosmic_radiation():
    cosmic_radiation_answer = """Космічне випромінювання – це радіація, яка з'являється у
результаті вибухів наднових зірок, а також внаслідок термоядерних реакцій на Сонці."""
    print_response(cosmic_radiation_answer)
    chat_storage(input_text, cosmic_radiation_answer)
    topics_reply()
    return


def largest_continent():
    largest_continent_answer = "Євразія — найбільший материк на Землі та складається з Європи та Азії."
    print_response(largest_continent_answer)
    chat_storage(input_text, largest_continent_answer)
    topics_reply()
    return


def reservoirs():
    reservoirs_answer = "Росія та Канада – держави, які мають найбільшу кількість водосховищ у світі ."
    print_response(reservoirs_answer)
    chat_storage(input_text, reservoirs_answer)
    topics_reply()
    return


def lakes():
    lakes_answer = """Канада – країна з найбільшою кількістю озер. 60% всіх озер світу 
знаходяться на території Канади: більш 3 мільйонів озер, що займають 9% канадських земель."""
    print_response(lakes_answer)
    chat_storage(input_text, lakes_answer)
    topics_reply()
    return


def sahara():
    sahara_answer = "Найбільша пустеля Сахара знаходиться у Північній Африці."
    print_response(sahara_answer)
    chat_storage(input_text, sahara_answer)
    topics_reply()
    return


def largest_lake():
    largest_lake_answer = "Каспійське море - найбільший на Землі замкнуте водоймище, тобто озеро."
    print_response(largest_lake_answer)
    chat_storage(input_text, largest_lake_answer)
    topics_reply()
    return


def cos():
    cos_response = f"""Ви обрали операцію «{get_current_topic().capitalize()} - 
Косинус». Введіть кут у градусах: """
    print_response(cos_response)
    chat_storage(input_text, cos_response)
    angle_deg = get_float_input()
    angle_rad = math.radians(angle_deg)
    cos_value = math.cos(angle_rad)
    cos_answer = f"Косинус кута {angle_deg} градусів дорівнює {cos_value:.2f}"
    print_response(cos_answer)
    trig_response = f"""Ви обрали тему: "{get_current_topic()}". Я можу обчислити значення наступних 
тригонометричних функцій: {", ".join(topics_dictionary["математика"]["тригонометрія"].keys())}."""
    print_response(trig_response)
    chat_storage(angle_deg, f"""{cos_answer} 
 {trig_response}""")
    return


def sin():
    sin_response = f"""Ви обрали операцію «{get_current_topic().capitalize()} - 
Синус». Введіть кут у градусах: """
    print_response(sin_response)
    chat_storage(input_text, sin_response)
    angle_deg = get_float_input()
    angle_rad = math.radians(angle_deg)
    sin_value = math.sin(angle_rad)
    sin_answer = f"Синус кута {angle_deg} градусів дорівнює {sin_value:.2f}."
    print_response(sin_answer)
    trig_response = f"""Ви обрали тему: "{get_current_topic()}". Я можу обчислити значення наступних 
тригонометричних функцій: {", ".join(topics_dictionary["математика"]["тригонометрія"].keys())}."""
    print_response(trig_response)
    chat_storage(angle_deg, f"""{sin_answer} 
 {trig_response}""")
    return


def gcd():
    gcd_response = f"Ви обрали операцію «НСД». Введіть перше число: "
    print_response(gcd_response)
    chat_storage(input_text, gcd_response)
    num1 = get_float_input()
    gcd_answ_1 = "Введіть друге число: "
    print_response(gcd_answ_1)
    chat_storage(num1, gcd_answ_1)
    num2 = get_float_input()
    while num2:
        num1, num2 = num2, num1 % num2
    gcd_answer = f"Найбільший спільний дільник чисел дорівнює {num1}."
    print_response(gcd_answer)
    chat_storage(num2, gcd_answer)
    topics_reply()
    return


def lcm():
    lcm_response = f"Ви обрали операцію «НСК». Введіть перше число: "
    print_response(lcm_response)
    chat_storage(input_text, lcm_response)
    a = get_float_input()
    lcm_answ_1 = "Введіть друге число: "
    print_response(lcm_answ_1)
    chat_storage(a, lcm_answ_1)
    b = get_float_input()

    def gcd_lcm(a, b):
        if b == 0:
            return a
        return gcd_lcm(b, a % b)

    answer = abs(a * b) // gcd_lcm(a, b)
    lcm_answer = f"Найменше спільне кратне чисел {a} та {b} дорівнює {answer}."
    print_response(lcm_answer)
    chat_storage(b, lcm_answer)
    topics_reply()
    return


def vector():
    vector_response = f"""Ви обрали операцію «{get_current_topic().capitalize()}». Введіть координати 
першого вектора (через кому з пробілом): """
    print_response(vector_response)
    chat_storage(input_text, vector_response)
    a = calculation_vector()
    vector_answ_1 = "Введіть координати другого вектора (через кому з пробілом):"
    print_response(vector_answ_1)
    chat_storage(a, vector_answ_1)
    b = calculation_vector()
    x = a[1] * b[2] - a[2] * b[1]
    y = a[2] * b[0] - a[0] * b[2]
    z = a[0] * b[1] - a[1] * b[0]
    result = [x, y, z]
    if result == [0, 0, 0]:
        zero_vector = "Векторний добуток є нульовим вектором."
        print_response(zero_vector)
        chat_storage(b, zero_vector)
        topics_reply()
        return
    vector_answer = f"Результат добутку: ({result[0]}, {result[1]}, {result[2]})"
    print_response(vector_answer)
    chat_storage(b, vector_answer)
    topics_reply()
    return


def calculation_vector():
    while True:
        vector_str = get_user_input()
        if check_input(vector_str):
            vect = vector_str.split(", ")
            if len(vect) != 3:
                calc_vector_response = "Невірно введені координати вектора. Спробуйте ще раз: "
                print_response(calc_vector_response)
                chat_storage("неправильно введені дані", calc_vector_response)
            try:
                vect = [float(x) for x in vect]
            except ValueError:
                calc_vector_response = "Невірно введені координати вектора. Спробуйте ще раз: "
                print_response(calc_vector_response)
                chat_storage("неправильно введені дані", calc_vector_response)
            return vect


def triangle_area():
    triangle_response = f"""Ви обрали операцію «{get_current_topic().capitalize()} - {input_text.capitalize()}». Але 
за допомогою векторного добутку. Отож, введіть координати вектора a (через кому з пробілом): """
    print_response(triangle_response)
    chat_storage(input_text, triangle_response)
    a = calculation_vector()
    triangle_answ_1 = "Тепер напишіть координати вектора h (через кому з пробілом): "
    print_response(triangle_answ_1)
    chat_storage(a, triangle_answ_1)
    h = calculation_vector()
    cross_product = [a[1] * h[2] - a[2] * h[1],
                     a[2] * h[0] - a[0] * h[2],
                     a[0] * h[1] - a[1] * h[0]]
    s = 0.5 * abs(sum(cross_product))
    triangle_answer = f"Отже, площа трикутника = {s}."
    print_response(triangle_answer)
    math_response = f"""Ви обрали тему: "{get_current_topic()}". Я можу обчислити 
площу наступних об’єктів: {", ".join(topics_dictionary["математика"]["обчислення площі"].keys())}."""
    print_response(math_response)
    chat_storage(h, f"""{triangle_answer}
 {math_response}""")
    return


def trapezium_area():
    trapezium_response = f"""Ви обрали операцію «{get_current_topic().capitalize()} - 
{input_text.capitalize()}». Введіть a: """
    print_response(trapezium_response)
    chat_storage(input_text, trapezium_response)
    a = get_float_input()
    trapezium_answ_1 = "Тепер напишіть b: "
    print_response(trapezium_answ_1)
    chat_storage(a, trapezium_answ_1)
    b = get_float_input()
    trapezium_answ_2 = "Введіть висоту h: "
    print_response(trapezium_answ_2)
    chat_storage(b, trapezium_answ_2)
    h = get_float_input()
    s = 0.5 * (a + b) * h
    trapezium_answer = f"Отже, площа трапеції = {s}."
    print_response(trapezium_answer)
    math_response = f"""Ви обрали тему: "{get_current_topic()}". Я можу обчислити 
площу наступних об’єктів: {", ".join(topics_dictionary["математика"]["обчислення площі"].keys())}."""
    print_response(math_response)
    chat_storage(b, f"""{trapezium_answer}
 {math_response}""")
    return


def rectangle_area():
    rectangle_response = f"""Ви обрали операцію «{get_current_topic().capitalize()} - 
{input_text.capitalize()}». Введіть сторону a: """
    print_response(rectangle_response)
    chat_storage(input_text, rectangle_response)
    a = get_float_input()
    rectangle_answ_1 = "Тепер напишіть сторону b: "
    print_response(rectangle_answ_1)
    chat_storage(a, rectangle_answ_1)
    b = get_float_input()
    s = a * b
    rectangle_answer = f"Отже, площа прямокутника = {s}."
    print_response(rectangle_answer)
    math_response = f"""Ви обрали тему: "{get_current_topic()}". Я можу обчислити 
площу наступних об’єктів: {", ".join(topics_dictionary["математика"]["обчислення площі"].keys())}."""
    print_response(math_response)
    chat_storage(b, f"""{rectangle_answer}
 {math_response}""")
    return


def grav_constant():
    g = 6.6743 * 10 ** (-11)
    response_grav = "Гравітаційна стала G = {:.10} м^3 / (кг * с^2).".format(g)
    print_response(response_grav)
    chat_storage(input_text, response_grav)
    topics_reply()
    return


def ampere_form():
    ampere_response = """Ви обрали операцію «{get_current_topic()}». 
Введіть силу струму I: """
    print_response(ampere_response)
    chat_storage(input_text, ampere_response)
    i = get_float_input()
    ampere_answ_1 = "Тепер напишіть відстань до провідника r: "
    print_response(ampere_answ_1)
    chat_storage(i, ampere_answ_1)
    r = get_float_input()
    mu0 = 4 * math.pi * 10 ** (-7)
    b = (mu0 * i) / (2 * math.pi * r)
    ampere_answer = "Індукція магнітного поля B = {:.10f} Тл.".format(b)
    print_response(ampere_answer)
    chat_storage(r, ampere_answer)
    topics_reply()
    return


def topics_reply():
    global topic_history
    topic_history.pop()
    response_topics_reply = f"""Ви обрали тему: "{get_current_topic()}". Ви можете задати мені 
питання з наступних тем: {", ".join(topics_dictionary[get_current_topic().lower()].keys())}."""
    print_response(response_topics_reply)
    topic_history.append(get_current_topic())
    chat_storage("", response_topics_reply)


def get_float_input():
    while True:
        try:
            value = get_user_input()
            check_result = check_input(value)
            if check_result:
                value = float(value)
                if value <= 0:
                    response_message = "Значення має бути дійсним числом, що більше нуля. Спробуйте ще раз: "
                    print_response(response_message)
                    chat_storage("неправильно введені дані", response_message)
                else:
                    return value
        except ValueError:
            response_message = "Значення має бути дійсним числом, що більше нуля. Спробуйте ще раз: "
            print_response(response_message)
            chat_storage("неправильно введені дані", response_message)


def check_input(input_text):
    if input_text.lower() == "вихід":
        print_response("Радий був поспілкуватися, до зустрічі.")
        chat_storage("вихід", "Радий був поспілкуватися, до зустрічі.")
        exit()
    elif input_text.lower() == "допомога":
        help_message = f"""Ви обрали тему «{get_current_topic()}».
Для виходу, напишіть «вихід»."""
        print_response(help_message)
        chat_storage("допомога", help_message)
    else:
        return True


def print_greeting():
    global topics_dictionary
    greeting = f"""Вітаю, мене звати Цезар. Ви можете
задати мені питання з наступних тем: {', '.join(topics_dictionary.keys())}."""
    print_response(greeting)
    chat_storage("назад", greeting)


def print_response(text):
    print(f"\033[34m[Цезар]: \033[0m{text}")


def get_user_input():
    return input("\033[33m[Користувач]: \033[0m")


def get_previous_topic():
    global topic_history
    if len(topic_history) < 2:
        return None
    return topic_history[-2]


def get_current_topic():
    global topic_history
    if len(topic_history) == 0:
        return None
    return topic_history[-1]


def print_help():
    help_message = ""
    if len(topic_history) == 0:
        help_message += "Введіть назву операції: "
    else:
        help_message += f"""Ви обрали тему «{get_current_topic()}»."""

    help_message += f"""\nДля виходу, напишіть «вихід».\nДля повернення до останньої теми напишіть «назад»."""
    print_response(help_message)
    chat_storage("допомога", help_message)


def topic_selection(topic):
    global topic_history, topics_dictionary
    topic = topic.lower()
    if topic in topics_dictionary:
        topic_history.append(topic)
        topic_response = f"""{random.choice(comments)}Ви обрали тему: "{get_current_topic()}". Ви можете задати мені 
питання з наступних тем: {", ".join(topics_dictionary[get_current_topic()].keys())}."""
        print_response(topic_response)
        chat_storage(topic, topic_response)
        return
    elif get_current_topic() in topics_dictionary.keys() and \
            topic in topics_dictionary[get_current_topic()].keys():
        topic_history.append(topic)
        if topic == "колядки":
            response_carols = f"""{random.choice(comments)}Ви обрали тему: "{get_current_topic()}". Я можу заспівати 5 різних колядок. Обирайте, яка 
Вам до душі: «{"», «".join(topics_dictionary[get_previous_topic()][get_current_topic()].keys())}»."""
            print_response(response_carols)
            chat_storage(topic, response_carols)
        elif topic == "тригонометрія":
            response_trig = f"""{random.choice(comments)}Ви обрали тему: "{get_current_topic()}". Я можу обчислити значення наступних 
тригонометричних функцій: {", ".join(topics_dictionary[get_previous_topic()][get_current_topic()].keys())}."""
            print_response(response_trig)
            chat_storage(topic, response_trig)
        elif topic == "обчислення площі":
            response_square = f"""{random.choice(comments)}Ви обрали тему: "{get_current_topic()}". Я можу обчислити 
площу наступних об’єктів: {", ".join(topics_dictionary[get_previous_topic()][get_current_topic()].keys())}."""
            print_response(response_square)
            chat_storage(topic, response_square)
        else:
            topics_dictionary[get_previous_topic()][get_current_topic()]()
        return
    elif get_current_topic() in topics_dictionary["математика"].keys() and \
            input_text in topics_dictionary[get_previous_topic()][get_current_topic()].keys():
        topics_dictionary[get_previous_topic()][get_current_topic()][input_text]()
    elif get_current_topic() in topics_dictionary["загальні"].keys() and \
            input_text in topics_dictionary[get_previous_topic()][get_current_topic()].keys():
        topics_dictionary[get_previous_topic()][get_current_topic()][input_text]()
    else:
        available_subtopics = None
        if get_current_topic() in topics_dictionary.keys():
            available_subtopics = ", ".join(topics_dictionary[get_current_topic().lower()].keys())
        if available_subtopics:
            response = f"""Я не знаю цієї теми, натомість, ви можете задати мені 
питання з наступних тем: {available_subtopics},
{", ".join(topics_dictionary.keys())}."""
            print_response(response)
            chat_storage(input_text, response)
        else:
            response = f"""Я не знаю цієї теми, натомість, ви можете 
задати мені питання з наступних тем: {", ".join(topics_dictionary.keys())}."""
            print_response(response)
            chat_storage(input_text, response)


def chat_storage(request, response):
    with open('chat_dialog.txt', 'a', encoding='utf-8') as file:
        file.write(f'[Користувач]: {request}\n')
        file.write(f'[Цезар]: {response}\n')


topics_dictionary = {
    "фізика": {
        "формула ампера": ampere_form,
        "гравітаційна стала": grav_constant
    },
    "математика": {
        "обчислення площі": {
            "прямокутник": rectangle_area,
            "трапеція": trapezium_area,
            "трикутник": triangle_area
        },
        "найбільший спільний дільник": gcd,
        "найменше спільне кратне": lcm,
        "векторний добуток": vector,
        "тригонометрія": {
            "синус": sin,
            "косинус": cos
        }
    },
    "географія": {
        "найбільше озеро": largest_lake,
        "континент найбільшої пустелі": sahara,
        "держава з найбільшою кількістю озер": lakes,
        "дві держави з найбільшою кількістю водосховищ": reservoirs,
        "найбільший материк": largest_continent
    },
    "філологія": {
        "відмінки української мови": ukrainian_declension,
        "роди українських іменників": noun_genders
    },
    "астрономія": {
        "космічне випромінювання": cosmic_radiation,
        "планети нашої системи з найбільшими та найменшими орбітами": planets_orbit,
        "вплив зоряного світла на здоров'я людини": influence_health,
        "відстань між землею та сонцем": planets_distance
    },
    "загальні": {
        "час": time,
        "новий рік": new_year,
        "місяць": month,
        "ваше ім'я": your_name,
        "колядки": {
            "Під ногами сніг рипучий": carol_1,
            "Віє вітер з гір": carol_2,
            "Ой на річці, на Йордані": carol_3,
            "Колядуєм, колядуєм": carol_4,
            "Вифлеємська зірка сяє": carol_5
        },
        "надихаючі цитати": quotation
    }
}

print_greeting()

while True:
    try:
        input_text = get_user_input()
    except KeyboardInterrupt:
        break

    if input_text.lower() == "вихід":
        break

    if input_text.lower() == 'допомога':
        print_help()
        continue

    if input_text.lower() == "назад":
        if len(topic_history) > 0:
            topic_history.pop()
            if len(topic_history) > 0:
                response_message = f"""Ви обрали тему: "{get_current_topic()}". Ви можете задати мені 
питання з наступних тем: {", ".join(topics_dictionary[get_current_topic().lower()].keys())}."""
                print_response(response_message)
                chat_storage("назад", response_message)
            else:
                print_greeting()
        else:
            print_greeting()
    else:
        topic_selection(input_text)

print_response("Радий був поспілкуватися, до зустрічі.")
chat_storage("вихід", "Радий був поспілкуватися, до зустрічі.")
