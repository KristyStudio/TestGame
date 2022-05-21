# Определение персонажей игры.
#Кейли
define kl = Character('Кейли', color="#000")
#Алан
define al = Character('Алан', color="#000")
#Кристина
define kr = Character('Кристи', color="#fac895", what_outlines=[ (1, "#ffffff") ], who_outlines=[ (1, "#000") ])
#Ника
define nk = Character('Ника', color="#000")
#Дарби
define db = Character('Дарби', color="#000")
#Герой
define hr = Character('Генри', color="#fac895", what_outlines=[ (1, "#ffffff") ])

# Игра начинается здесь:
label start:
    scene bg hand
    with fade
    $ renpy.pause(3.0)
    hr "{cps=30}Помню, главный герой книги однажды сказал: \"Чтобы не случилось - я защищу тебя.\" {/cps}"
    extend "{cps=30}Каким же классным он был...{/cps}"

    hr "{cps=27}На его месте я бы просто убежал, поджав хвост, словно прохожий... {/cps}"

    hr "{cps=30}Ни разу не скорчив недовольное лицо, не плача и не насмехаясь над собой, он всегда приходил на помощь, боролся до последнего... {/cps}"
    extend "{cps=27}Он был любим абсолютно всеми... {/cps}"
    extend "{cps=27}Он был героем, очевидно... {/cps}"
    hide text with dissolve

    scene bg withouthand
    with fade
    $ renpy.pause(3.0)
    hr "{cps=27}Наверное, окажись там, я был бы тем самым прохожим…"
    hide text with dissolve

    scene bg most
    with fade

    hr "{cps=27}Ладно, лимит нытья исчерпан, пора домой. {cps=27}"

    "Я неспешно встаю и направляюсь к мосту."

    jump scenetwo

    return
#-----------------------------------День 1----------------------------------
# Сцена 2:
label scenetwo :

    scene bg black

    scene bg roomgg
    with fade

    show kristina test

    kr "Ты и правда самый худший отброс в истории..."

    jump scenethree

    return

# Сцена 3:
label scenethree:

    scene bg yard
    with fade

    show kristina test

    hr "Ну ладно, пошли"

    scene bg square
    with fade

    show kaly test

    hr "Слова героя"

    scene bg school
    with fade

    show kristina test

    hr "Слова героя"

    scene bg square
    with fade

    show kristina test

    hr "Слова героя"

    scene bg yard
    with fade

    show nika test

    hr "Ну ладно, пошли"

    scene bg roomgg
    with fade

    jump scenefour

    return
#-----------------------------------День 2----------------------------------
# Сцена 4:
label scenefour:

    scene bg kafe
    with fade

    hr "Ну ладно, пошли"

    jump scenefive

    return

# Сцена 5:
label scenefive:

    scene bg yard
    with fade

    hr "Не отдал"

    scene bg square
    with fade

    show nika test

    jump scenesix

    return

# Сцена 6:
label scenesix:

    scene bg hall
    with fade

    show nika test

    hr "Не отдал"

    scene bg classk
    with fade

    show nika test

    menu:
        "Куда пойти?"

        "Клубы":
            jump scenemuzOne

        "Столовая":
            jump scenestolOne

        "Библиотека":
            jump scenebibOne

    return

# Сцена муз-клуб 1:
label scenemuzOne:

    scene bg hall
    with fade

    scene bg halltwo
    with fade

    show nika test

    hr "Ну... да..."

    scene bg muz
    with fade

    show kristina test

    kr "Ну... да..."

    jump  VstrechasDarby

    return



# Билет от Алана:
label BiletOtAlana:

    scene bg yard
    with fade

    show kaly happy

    kl "Пошли?"

    hr "Пошли)"

    scene bg school
    with fade

    show alan happy

    al "Вот держи"

    kl "Хмх хм, кого позвать?"

    al "Пошли уже в класс"

    kl "Ладно, потом..."

    scene bg classk
    with fade

    menu:
        "Кого позвать?"

        "Позвать Нику":
            jump ViborNikaSvidanie

        "Позвать Кейли":
            jump ViborKalySvidanie


    return
