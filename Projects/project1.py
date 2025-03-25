###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("flowers")

q1 = codesters.Square(100, 100, 200, 'red')
q2 = codesters.Square(-100, 100, 200, 'blue')
q3 = codesters.Square(-100, -100, 200, 'green')
q4 = codesters.Square(100,-100,200, 'yellow') 

s1 = codesters.Sprite("Cute cat.jpeg", 100, 100)
s1.set_size(1)
s2 = codesters.Sprite("hamilton.jpeg", -100, 100 )
s2.set_size(0.7)
s3 = codesters.Sprite("taylor.jpeg", 100, -100)
s3.set_size(0.7)
s4 = codesters.Sprite("gossipgirl.jpeg", -100, -100)
s4.set_size(0.7)

message1 = codesters.Text("Grace Desilets", 0, 220,"red")
message2 = codesters.Text("I love cats, the tv show Gossip Girl, Taylor and Hamilton!", 0, -220,"black")
