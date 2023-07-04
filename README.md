# BOTCH-V2
C'est parti pour retaper toutes les fonctionnalités du botch v1.
On part sur de l'optimisation du code et quelques nouveautées.
On va descendre le code plugins par plugins:

## MAIS POURQUOI T'AS TOUT REFAIT ?!

> TLDR: Parce que j'ai envie de faire un truc propre et que j'ai appris des trucs depuis. Je résume tout en 3 points:

petit warning, pleins de private jokes et autres trucs de la communauté du botch, si vous comprenez pas, c'est normal, je pige la moitié aussi.
### Nouvelle gestion de la database

On passe tout sous peewee, une librairie d'ORM pour python. C'est plus propre et plus simple à utiliser.
On remove complètement DataBaseAccess.py quitte à répéter un peu de code, c'est pas grave, c'est plus simple.

### Discord.py est passé en 2.0

Alors, c'est passé en 2.0 y'a un peu plus d'un an, mais j'étais occupé à cram en médecine... donc 

- slash command, c'est plus propre et plus simple à utiliser surtout pour les ~~monkeys~~ utilisateurs habituels du botch
- des outils pour les modo directement dans discord (ban, kick, mute, etc...), dans des menus déroulants
- poffinage global de l'UI avec les bouttons et les menus déroulants dans les embeds

### Liste de course

- Pâtes crues
- Sel 
- Petits pois
- Sauce à nems 
- Huile 
- Vinaigrette 
- Curry 
- Cube de volaille
- Cumin 
- Safran 
- Ebly
- Noix de muscade 
- Semoule
- Pois chiches
- Poivre 
- Spaghettis crues
- Sauce tomate


## Tables de la nouvelle database
### Membres:
- `user_id` (IntegerField) : id de l'utilisateur
- `user_avatar` (TextField) : lien de l'avatar de l'utilisateur
- `joined_at` (DateField) : date d'arrrivée de l'utilisateur
- `last_message` (TextField) : contenu du dernier message
  - **### "\<text>(Blah blah blah)\<attachment>(https://...)"**
- `last_message_date` (DateField) : date du dernier message
- `xp` (IntegerField) : quantité d'xp que l'utilisateur a gagné
- `birthday` (DateField) : date d'anniversaire

### Case
- `user_id` (IntegerField) : id de l'utilisateur
- `case_id` (IntegerField) : id de la case
- `case_date` (DateField) : date de la case
- `case_reason` (TextField) : raison de la case
- `case_mod` (IntegerField) : id du modérateur qui a fait la case
- `case_type` (IntegerField) : type de la case (warn, mute, ban, kick, tempban)
- `case_duration` (IntegerField) : durée de la case (en minutes) (0 si pas de durée)
- `case_active` (BooleanField) : si la case est active ou non

### SDLM
- `user_id` (IntegerField) : l'id de l'utilisateur
- `message_id` (IntegerField) : id du message dans le jdsdlm
- `posteur` (BooleanField) : si l'utilisateur est le posteur du message

### Starbotch
- `sb_message_id` (IntegerField) : id du message dans le starbotch
- `message_id` (IntegerField) : id du message original
- `channel_id` (IntegerField) : id du channel du message original
- `posteur_id` (IntegerField) : id du poster du message original
- `stars` (IntegerField)  : nombre de stars sur le message original

## [`plugins/admin_old`](plugins/admin_old.py) -> [`plugins/admin`](plugins/admin.py)
### Events:
- [ ] `on_raw_reaction_add` -> sert pour le report de message.
    - à 3 ❗️ : report le message
    - à 7 ❗️ : report le message et le supprime
### Commands:
- [ ] `admin group`:
  - [ ] `shutdown`: arrête le bot
  - [ ] `info`: affiche des informations sur le bot
  - [ ] `clear_person <cible> (nombre_de_messages)`: supprime les messages une personne
  - [ ] `roles`: affiche les roles du serveur
  - [ ] `mute`: mute un utilisateur
  - [ ] `unmute`: unmute un utilisateur
  - [ ] `ban`: ban un utilisateur
  - [ ] `tempban`: tempban un utilisateur
  - [ ] `unban`: unban un utilisateur
  - [ ] `kick`: kick un utilisateur
  - [ ] `warn`: warn un utilisateur
  - [ ] `unwarn`: unwarn un utilisateur
  - [ ] `case`: affiche les warns d'un utilisateur

- [ ] `channel group`:
  - [ ] `block`: bloque un utilisateur l'accès à l'écriture sur un channel
  - [ ] `ban`: ban un utilisateur d'un channel
  - [ ] `clear`: remet les droits de l'utilisateur par défaut sur ce channel

## [`plugins/broadcast_old`](plugins/broadcast_old.py) -> [`plugins/broadcast`](plugins/broadcast.py)
### Events:
- [ ] `on_message`: pour le msg de confirmation, être sûr de pas ping 1k personne pour r

### Commands:
- [ ] `broadcast`:
  - [ ] `annonce`: envoie un message dans le channel d'annonce
  - [ ] `sdlm`: envoie un message à tous les participants du jdsdlm
  - [ ] `example`: envoie un message d'exemple

## [`plugins/dev_old`](plugins/dev_old.py) -> [`plugins/dev`](plugins/broadcast.py)
- [ ] `reload`: reload les plugins ou le plugin si précisé
- [ ] `mp`: envoie un mp à un utilisateur
- [ ] `ping`: pong !

## [`plugins/errors_old`](plugins/errors_old.py) -> [`plugins/errors`](plugins/errors.py)
flm

## [`plugins/general_old`](plugins/general_old.py) -> [`plugins/general`](plugins/general.py)
### Events:
- [ ] `on_message`:
  - check si quelqu'un ping everyone pour l'harceler en dm
  - compte les boris et rajoute au compteur de boris (je suis meme pas sûr que ça marche)

### Commands:
- [ ] `citation`: affiche une citation aléatoire
- [ ] `tipeee`: affiche le lien tipeee
- [ ] `info`: affiche des informations sur le bot
- [ ] `suntzu`: affiche une citation de Sun Tzu

## [`plugins/loops_old`](plugins/loops_old.py) -> [`plugins/loops`](plugins/loops.py)
### Events:
- [ ] `do_a_backflip`: fait des backups de la database toutes les 24h

### Commands:
- [ ] `loop`:
  - [ ] `reload`: démarre une loop
  - [ ] `doabackup`: fait une backup de la database
  - 
## [`plugins/memes_old`](plugins/memes_old.py) -> [`plugins/memes`](plugins/memes.py)
Je crois que ça se base sur l'api de reddit et vu que c'est finito, on verra plus tard
### Commands:
- [ ] `meme`: affiche un meme aléatoire

## [`plugins/rolereact_old`](plugins/rolereact_old.py) -> [`plugins/rolereact`](plugins/rolereact.py)
### Events:
- [ ] `on_raw_reaction_add`: ajoute un role à un utilisateur
- [ ] `on_raw_reaction_remove`: enlève un role à un utilisateur

### Commands:
- [ ] `rolereact`:
  - [ ] `example`: affiche un exemple de message rolereact
  - [ ] `setup`: setup un message rolereact
  - [ ] `delete`: supprime un message rolereact
  - [ ] `status`: affiche les msg de rolereact (affiche les role du message si message précisé)
  - [ ] `add_role`: ajoute un role au message
  - [ ] `remove_role`: enlève un role au message
  - 
## [`plugins/sdlm_old`](plugins/sdlm_old.py) -> [`plugins/sdlm`](plugins/sdlm_old.py)
### Events:
- [ ] `on_raw_reaction_add`: valide le point et passe le role de posteur au gagnant
- [ ] `on_member_ban`: reset le score du banni
- [ ] `on_message`: si le posteur post une image, elle se fait pin et devient l'indice principal

### Commands:
- [ ] `sdlm`:
  - [ ] `leaderboard`: affiche le leaderboard
  - [ ] `score`: affiche le score du joueur
  - [ ] `tienskop1`: passe le role de posteur au joueur
  - [ ] `posteur`: affiche le posteur actuel
  - [ ] `load_backup`: charge une backup
  - [ ] `reload`: reload le jeu (bug après le reload du plugin, à voir si je peux faire qqch)
  - [ ] `set_img`: set l'image de l'indice

## [`plugins/starbotch_old`](plugins/starbotch_old.py) -> [`plugins/starbotch`](plugins/starbotch.py)
### Events:
- [ ] `on_raw_reaction_add`: tout le dawa quand on le met dans le starbotch (ou update le nombre de stars)
- [ ] `on_raw_reaction_remove`: tout le dawa quand on le retire du starbotch (ou update le nombre de stars)

### Commands:
- [ ] `starbotch`:
  - [ ] `leaderboard`: affiche le leaderboard
  - [ ] `reload`: reload le starbotch (bug après le reload du plugin, à voir si je peux faire qqch)
  - [ ] `random`: affiche un message random du starbotch

## [`plugins/vocal_old`](plugins/vocal_old.py) -> [`plugins/vocal`](plugins/vocal.py)
Faut coder un bot music, on verra si ça tient tjrs. Ou je calerai un synthétiseur vocal dessus.