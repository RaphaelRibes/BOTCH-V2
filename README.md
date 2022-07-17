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

## [`admin_old`](plugins/admin_old.py) -> [`admin`](plugins/admin.py)
## [`broadcast_old`](plugins/broadcast_old.py) -> [`broadcast`](plugins/broadcast.py)
