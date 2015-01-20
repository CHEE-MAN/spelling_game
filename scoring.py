points=1
def scoring():
    if user_answer==answer:
        score+=points
        scorestreak+=1
    if user_answer!=answer:
        scorestreak=1
    if scorestreak==5:
        points=2
    if scorestreak==10:
        points=3
    if scorestreak==20:
        points=4
    if scorestreak==40:
        points=5