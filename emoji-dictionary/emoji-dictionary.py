ascii_emoji = input('Set Ascii Emoji > ')

emojis_sign = {
    ':)':  'smile',
    ':-)': 'smile',
    ':]':  'smile',
    '=)':  'smile',

    ':(':  'frown',
    ':-(': 'frown',
    ':[':  'frown',
    '=(':  'frown',

    ':D':  'grin',
    ':-D': 'grin',
    '=D':  'grin',
}
emojis_sign_name = emojis_sign.get(ascii_emoji, 'Please Set Only Ascii Emoji')

emojis_explanation = {
    'smile': 'Smile - A yellow face with simple open eyes and a thin closed smile.\n'
             'Conveys a wide range of positive, happy, and friendly sentiments. \n'
             'Its tone can also be patronizing, passive-aggressive, or ironic, \n'
             'as if saying This is fine when it’s really not. 🙂',

    'frown': 'Frown - A classic sad face.\n'
             'A yellow face with simple, open eyes and wide, steep frown.\n'
             'May convey such feelings as moderate concern or disappointment and affectionate sadness,\n'
             'as when missing a loved one. Its sentiment is usually more intense than. 🙁',
    
    'grin': 'A yellow face with simple, open eyes and a broad, open smile, \n' 
            'showing upper teeth and tongue on some platforms. \n' 
            'Often conveys general pleasure and good cheer or humor. 😀 \n'
}
emojis_explanation_text = emojis_explanation.get(emojis_sign_name, "I Don't Know This Emojis")

print(emojis_explanation_text)
