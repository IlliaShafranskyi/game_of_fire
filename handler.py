def validate_phrase(phrase):
    phrases = []
    if(phrase == "А ты зачем спрашиваешь, старик?"):
        main_phrase = "Тут по деревне весточка пробежала, что кто-то на имя Бейзел хочет захватить власть в городе"
        phrase1 = "Расскажи об этом больше"
        phrase2 = "Мне некогда слушать твои бредни"
        phrase3 = "Тебя приставил кто-то следить за мной?"
        phrases = [main_phrase, [phrase1, phrase2, phrase3]]
        return phrases
    
    if(phrase == "Ищу семью, может вы знаете?"):
        main_phrase = "А что случилось с твоей семьей?"
        phrase1 = "Мою семью похители, я ищу их."
        phrase2 = "Не твое дело, чайка ободранная."
        phrase3 = "Где Бар у Грезли?"
        phrases = [main_phrase, [phrase1, phrase2, phrase3]]
        return phrases
