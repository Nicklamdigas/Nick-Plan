def main():
   sentence = input()
   converted_sentence = convert(sentence)
   print(converted_sentence)

def convert(sentence):
   sentence = sentence.replace(":)", "🙂")
   sentence = sentence.replace(":(", "🙁")
   return sentence

main()






def convert(sentence):
   #THis is a map of what to find and what to replace it with
   emojis = {
      ":)":"🙂",
      ":(":"🙁"
   }
   #we loop through the dictionary and replace each one
   for emoticon in emojis:
      sentence = sentence.replace(emoticon, emojis[emoticon])
    return sentence