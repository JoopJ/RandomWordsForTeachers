wordsOriginal = """My baby don't mess around
Because she loves me so, and this I know for sure (Uh)
But does she really wanna
But can't stand to see me walk out the door? (Ah)
Don't try to fight the feeling
'Cause the thought alone is killing me right now (Uh)
Thank God for Mom and Dad
For sticking two together 'cause we don't know how (C'mon)

Hey ya! Hey ya!
Hey ya! Hey ya!
Hey ya! Hey ya!
Hey ya! Hey ya!

You think you've got it, oh, you think you've got it
But “got it” just don't get it 'til there's nothing at all (Ah!)
We get together, oh, we get together
But separate's always better when there's feelings involved (Ah)
If what they say is “Nothing is forever”
Then what makes, then what makes, then what makes
Then what makes, what makes, what makes love the exception?
So why oh, why oh, why oh, why oh, why oh
Are we so in denial when we know we're not happy here?
Y'all don't want to hear me, you just want to dance

Hey ya! (Uh-oh) Hey ya! (Uh-oh)
Don't want to meet your daddy
Hey ya! (Uh-oh)
Just want you in my Caddy (Uh-oh)
Hey ya! (Uh-oh)
Don't want to meet your mama (Uh-oh)
Hey ya! Uh-oh
Just want to make you cumma (Uh-oh)
Hey ya! Uh-oh
I'm, I'm, I'm, I'm just being honest (Uh-oh)
Hey ya!
I'm just being honest

Hey, alright now, alright now, fellas (Yeah?)
Now, what's cooler than being cool? (Ice Cold!)
I can't hear ya
I say what's, what's cooler than being cool? (Ice Cold!)
Alright, alright, alright, alright, alright, alright, alright, alright
Alright, alright, alright, alright, alright, alright
Okay now, ladies (Yeah?)
Now, we gon' break this thing down in just a few seconds
Now don't have me break this thing down for nothing
Now I want to see y'all on your baddest behavior
Lend me some sugar, I am your neighbor
Ah, here we go!

Shake it, sh-shake it, shake it, sh-shake it (Uh-oh)
Shake it, sh-shake it, Shake it, shake it, sh-shake it (Uh-oh)
Shake it like a Polaroid picture, hey ya!
Shake it, sh-shake it, shake it, sh-shake it
Shake it, shake it (okay), shake it, sugar
Shake it like a Polaroid picture

Now all the Beyoncés and Lucy Lius
And baby dolls, get on the floor
You know what to do, oh, you know what to do
You know what to do

Hey ya! (Uh-oh) Hey ya! (Uh-oh)
Hey ya! (Uh-oh) Hey ya! (Uh-oh, hey ya!)
Hey ya! (Uh-oh) Hey ya! (Oh, oh, uh-oh)
Hey ya! (Uh-oh) Hey ya! (Uh-oh)"""

############################

words = """My baby don't mess around Because she loves me so, and this I know for sure (Uh) But does she really wanna But can't stand to see me walk out the door? (Ah) Don't try to fight the feeling 'Cause the thought alone is killing me right now (Uh) Thank God for Mom and Dad For sticking two together 'cause we don't know how (C'mon) You think you've got it, oh, you think you've got it But “got it” just don't get it 'til there's nothing at all (Ah!) We get together, oh, we get together But separate's always better when there's feelings involved (Ah) If what they say is “Nothing is forever” Then what makes, then what makes, then what makes Then what makes, what makes, what makes love the exception? So why oh, why oh, why oh, why oh, why oh Are we so in denial when we know we're not happy here? Y'all don't want to hear me, you just want to dance Hey, alright now, alright now, fellas (Yeah?) Now, what's cooler than being cool? (Ice Cold!) I can't hear ya I say what's, what's cooler than being cool? (Ice Cold!) Alright, alright, alright, alright, alright, alright, alright, alright Alright, alright, alright, alright, alright, alright Okay now, ladies (Yeah?) Now, we gon' break this thing down in just a few seconds Now don't have me break this thing down for nothing Now I want to see y'all on your baddest behavior Lend me some sugar, I am your neighbor Ah, here we go! Now all the Beyoncés and Lucy Lius And baby dolls, get on the floor You know what to do, oh, you know what to do You know what to do"""

###############################

specialWords = """
Hey ya! Hey ya!
Hey ya! Hey ya!
Hey ya! Hey ya!
Hey ya! Hey ya!

Hey ya! (Uh-oh) Hey ya! (Uh-oh)
Don't want to meet your daddy
Hey ya! (Uh-oh)
Just want you in my Caddy (Uh-oh)
Hey ya! (Uh-oh)
Don't want to meet your mama (Uh-oh)
Hey ya! Uh-oh
Just want to make you cumma (Uh-oh)
Hey ya! Uh-oh
I'm, I'm, I'm, I'm just being honest (Uh-oh)
Hey ya!
I'm just being honest

Shake it, sh-shake it, shake it, sh-shake it (Uh-oh)
Shake it, sh-shake it, Shake it, shake it, sh-shake it (Uh-oh)
Shake it like a Polaroid picture, hey ya!
Shake it, sh-shake it, shake it, sh-shake it
Shake it, shake it (okay), shake it, sugar
Shake it like a Polaroid picture

Hey ya! (Uh-oh) Hey ya! (Uh-oh)
Hey ya! (Uh-oh) Hey ya! (Uh-oh, hey ya!)
Hey ya! (Uh-oh) Hey ya! (Oh, oh, uh-oh)
Hey ya! (Uh-oh) Hey ya! (Uh-oh)

"""

import random

numTeachers = 35

def FormatWords(words):
  words = words.split(" ")
  random.shuffle(words)
  return(words)

def AddWords(words, numTeachers):
  teachersWords = []


  for teacher in range(numTeachers):
    teachersWords.append([])
    for _ in range(wordsPerTeacher):
      teachersWords[teacher].append(words.pop())

  return teachersWords

def PrintTeachersWords(teachersWords):
  for x in range(0, len(teachersWords)):
    print(x+1,teachersWords[x])


words = FormatWords(words)

wordsPerTeacher = len(words)//numTeachers

teachersWords = AddWords(words, numTeachers)

PrintTeachersWords(teachersWords)












