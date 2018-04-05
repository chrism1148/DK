import unidecode

accented_characters = u'Málaga', u'é', u'á'
# accented_string is of type 'unicode'

unaccented_characters = unidecode.unidecode(accented_characters)


print(unaccented_characters)