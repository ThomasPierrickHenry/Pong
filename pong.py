import pygame as py

py.init()

hauteur = 400
longueur = 500

fenetre = py.display.set_mode((longueur, hauteur))

# Définir la position et la taille des rectangles
x = 25
y = 50
ia_x = 465
ia_y = 50
largeur_rectangle = 10
hauteur_rectangle = 100

# Définir la position et la taille de la balle
balle_x = 200
balle_y = 250
balle_taille = 20

# Définir la vitesse de déplacement du rectangle et de la balle
vitesse = 5
balle_vx = 5
balle_vy = 5

#définir le score
Score_A = 0
Score_B = 0


#fonction set text score
def Set_Score(score_A, score_B): 
    score = " team A : " + str(score_A) + " team B : " + str(score_B)
    py.display.set_caption(score)

#afficher le score en debut de lancement
Set_Score(0,0)


# Créer une instance de la classe Clock
clock = py.time.Clock()

#fonction main



while True:
    # Gestion des événements
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()


 # Gestion des touches fléchées
    touches = py.key.get_pressed()
   
    if touches[py.K_UP]:
        y -= vitesse
    elif touches[py.K_DOWN]:
        y += vitesse

#IA movement
    
    if ia_y > balle_y :
        ia_y -= vitesse
    else :
        ia_y += vitesse
       

#collission 
    rectangle_IA = py.Rect(ia_x, ia_y, largeur_rectangle, hauteur_rectangle)
    rectangle = py.Rect(x, y, largeur_rectangle, hauteur_rectangle)
    balle = py.Rect(balle_x, balle_y, balle_taille, balle_taille)
    but1 = py.Rect(0, 0, 10, hauteur)
    but2 = py.Rect(longueur, 0 , 1, hauteur)
    if rectangle.colliderect(balle):
        balle_vx *= -1

    if rectangle_IA.colliderect(balle):
        """if balle_vx > 0:
            balle_x = rectangle_IA.left - balle_taille
        elif balle_vx < 0:
            balle_x = rectangle_IA.right
        balle_vx *= -1
        if balle_vy > 0:
            balle_y = rectangle_IA.top - balle_taille
        elif balle_vy < 0:
            balle_y = rectangle_IA.bottom"""
        balle_vx *= -1

    if but1.colliderect(balle): 
        Score_A += 1
        Set_Score(Score_A, Score_B)

    if but2.colliderect(balle):
        Score_B += 1
        Set_Score(Score_A, Score_B)



    # Mettre à jour la position de la balle
    balle_x += balle_vx
    balle_y += balle_vy

    # Faire rebondir la balle sur les bords de la fenêtre
    if balle_x < balle_taille // 2 or balle_x > longueur - balle_taille // 2:
        balle_vx = -balle_vx
    if balle_y < balle_taille // 2 or balle_y > hauteur - balle_taille // 2:
        balle_vy = -balle_vy

    # Effacer l'écran
    fenetre.fill((0, 0, 0))

    # Dessiner le rectangle dans la fenêtre et la balle
    py.draw.rect(fenetre, (255, 255, 255), (x, y, largeur_rectangle, hauteur_rectangle))
    py.draw.rect(fenetre, (255, 255, 255), (balle_x, balle_y, balle_taille, balle_taille ))
    py.draw.rect(fenetre, (255, 255, 255), (ia_x, ia_y, largeur_rectangle, hauteur_rectangle))
    """
    py.draw.rect(fenetre, (255, 255, 255), (0, 0, 4, hauteur))
    py.draw.rect(fenetre, (255, 255, 255), (longueur - 4, 0 , 4, hauteur))
    """
    py.display.update()

    py.display.flip()

    # Ralentir la vitesse de tick
    clock.tick(60) # 30 FPS maximum





