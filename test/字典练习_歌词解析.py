music_lrc = """
01 - Das ganz normale Leben

[00:24.40]Dies Zeit hat keinen Namen
[00:26.94]und keine echten Ideale
[00:29.57]doch wir irren durch unser Leben
[00:32.28]auf der Suche nach Erinnerungen.
[00:35.67]Um festzuhalten was schön ist
[00:37.73]obwohl hier garnichts geschehn ist.
[00:46.18]Dabei scheint es allzu leich
[00:48.15]einen eigenen Platz zu finden.
[00:50.82]Diesen Wahnsinn zu vergessen
[00:53.11]inmitten guter Menschen
[00:55.68]doch der Alltag macht uns platt
[00:58.34]mit jedem neuen Tag.
[01:06.03]Das sind felsenharte Zeiten
[01:08.74]das ist die Opfer der Verrückten.
[01:11.46]Nach Jahren der Verschwendung
[01:13.98]ist das Reality in Echtzeit
[01:17.01]Das ist das ganz normale Leben
[01:19.27]so passiert das jetzt eben
[01:27.17]und du hälst mich an den Händen
[01:29.73]weil du weißt dass das gut tut
[01:32.79]wenn man jemanden halt gibt
[01:35.73]der längst nicht mehr sicher steht
[01:37.81]ein Freund in solchen Momenten
[01:40.39]ein Freund mit Herz und Händen

[01:48.34]Denn manchmal frag ich mich
[01:50.08]wer bin ich hier,
[01:51.87]was mach ich hier,
[01:54.75]und wofür
[02:00.20]wer bin ich hier,
[02:02.34]was mach ich hier,
[02:05.03]und wofür
[02:32.79]Man kann sicher nicht behaupten
[02:32.79]dass es besser wird,
[02:34.50]wenn es anders wird
[02:36.02]aber anders muss es werden
[02:37.75]wenn es gut werden soll
[02:40.01]das fällt dir ein in dem Moment
[02:42.82]wo du den Weg nicht kennst, nur rennst
[02:47.50]und du rennst davon
[02:49.13]und dabei lieb ich dich so sehr
[02:54.57]mit jedem neuen Morgen
[02:56.67]deine Ängste und Hoffnungen
[02:58.99]und deine ganzen Sorgen
[03:01.77]und dass du für mich da bist
[03:04.30]obwohl das gar nicht immer leicht ist

[03:12.10]Denn manchmal frag ich mich
[03:13.95]wer bin ich hier,
[03:15.69]was macha ich hier,
[03:18.66]und wofür
[03:24.72]wer bin ich hier,
[03:26.23]was macha ich hier,
[03:28.77]und wofür

[03:57.27]das ist das ganz normale Leben
[03:59.16]so passiert das jetzt eben
"""

lrc_dict = {}

music_lrc_list = music_lrc.splitlines()  # 按行切割
print(music_lrc_list)
for lrc_line in music_lrc_list:
    lrc_line_list = lrc_line.split("]")
    print("lrc_line_list=", lrc_line_list)
    index = 0


    """
    
    
        for index in range(len(music_lrc_list) - 1):
        print(len(music_lrc_list))
        time_str = lrc_line_list[index][1:]
        print(time_str)
        time_list = time_str.split(":")
        # time1 = time_list[0] * 60 + time_list[1]
        # lrc_dict[time1] = lrc_line_list[-1]
print(lrc_dict)
    """



