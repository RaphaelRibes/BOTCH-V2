# BOTCH-V2
C'est parti pour retaper toute les fonctionnalités du botch v1.
On part sur de l'optimisation du code et quelques nouveautées.
On va descendre le code plugins par plugins:

## Nouvelle gestion de la [`database`](plugins/database.py)
    La database utilisera peewee qui est une lib d'ORM.
    Comme ça on peut gérer toute la db sous forme d'objet et ça rendra le code bien plus lisible
### Membres:
- `user_id`: l'id de l'utilisateur
- `user_avatar`: lien de l'avatar de l'utilisateur
- `joined_at_timestamp`: timestamp de la date d'arrrivée de l'utilisateur
- `last_message`: contenu du dernier message  ***# "C'est un message|attachment:https://media(cdn).discordapp.net(com)/attachments/..."***
- `last_message_timestamp`: timestamp du dernier message
- `xp`: quantité d'xp que l'utilisateur a gagné
- `case`: historique des conneries qu'à fait le boug (sous la forme "Warn:Reason(when)|Tempban:Reason(when)|Ban:Reason|Mute:Reason(when)|Kick:Reason(when)")
- `baned_until`: date jusqu'à laquelle l'utilisateur est banni (sous la forme %Y-%m-%d %H:%M:%S... *font chier ces ricains*)
- `muted_until`: date jusqu'à laquelle le membre est mute (sous la forme %Y-%m-%d %H:%M:%S... *putains de ricains*)
- `birthday`: date d'anniversaire, il faudra que je fasse la conversion du la date chiante des ricains (%Y-%m-%d) au système normal (%d-%m-%Y)
- `points_sdlm`: score du sdlm (par défaut 0)
- `on_the_server`: boolean qui indique si l'utilisateur est sur le serveur (par défaut True)

### SDLM
Le posteur et l'image en cours du sdlm passe sur le fichier de config parce que flemme

### Starbotch
- `sb_message_id`: id du message dans le starbotch
- `message_id`: id du message original
- `channel_id`: id du channel du message original
- `poster_id`: id du poster du message original
- `stars`: nombre de stars sur le message original

## [`plugins/admin_old`](plugins/admin_old.py) -> [`plugins/admin`](plugins/admin.py)
### Events:
- [x] `on_raw_reaction_add` -> sert pour le report de message.
    - à 3 ❗️: report le message
    - à 7 ❗️: report le message et le supprime

- [ ] `admin group`:
  - [x] `shutdown`: arrête le bot
  - [x] `info`: affiche des informations sur le bot
  - [x] `clear_person <cible> (nombre_de_messages)`: supprime les messages une personne
  - [X] `roles`: affiche les roles du serveur
  - [ ] `mute`: mute un utilisateur
  - [ ] `unmute`: unmute un utilisateur
  - [ ] `ban`: ban un utilisateur
  - [ ] `tempban`: tempban un utilisateur
  - [ ] `unban`: unban un utilisateur
  - [ ] `kick`: kick un utilisateur
  - [ ] `warn`: warn un utilisateur
  - [ ] `unwarn`: unwarn un utilisateur
  - [ ] `case`: affiche les warns d'un utilisateur

- [x] `channel`:
  - [x] `block`: bloque un utilisateur l'accès à l'écriture sur un channel
  - [x] `ban`: ban un utilisateur d'un channel
  - [x] `clear`: remet les droits de l'utilisateur par défaut sur ce channel

### Commands:
## [`plugins/broadcast_old`](plugins/broadcast_old.py) -> [`plugins/broadcast`](plugins/broadcast.py)
## [`DataBaseAccess`](DataBaseAccess.py) -> [`plugins/database`](plugins/database.py)
Rien n'est à garder, on passe sur une db en ORM donc il faut juste faire des méthodes d'accès à la db.
- [x] `get_member`: récupère les données un membre du serveur
- [x] `get_sb_by_id`: récupère les données d'un message dans le starbotch par id
- [x] `get_sb_by_stars`: récupère les données d'un message dans le starbotch par nombre de stars
- [x] `create_sb`: rajoute un msg dans le starbotch
## [`plugins/dev_old`](plugins/dev_old.py) -> [`plugins/dev`](plugins/broadcast.py)
## [`plugins/errors_old`](plugins/errors_old.py) -> [`plugins/errors`](plugins/errors.py)
## [`plugins/general_old`](plugins/general_old.py) -> [`plugins/dev`](plugins/general.py)
## [`plugins/loops_old`](plugins/loops_old.py) -> [`plugins/loops`](plugins/loops.py)
## [`plugins/memes_old`](plugins/memes_old.py) -> [`plugins/dev`](plugins/memes.py)
## [`plugins/sdlm_old`](plugins/sdlm_old.py) -> [`plugins/sdlm`](plugins/sdlm_old.py)
## [`plugins/starbotch_old`](plugins/starbotch_old.py) -> [`plugins/starbotch`](plugins/starbotch.py)
## [`plugins/vocal_old`](plugins/vocal_old.py) -> [`plugins/vocal`](plugins/vocal.py)
