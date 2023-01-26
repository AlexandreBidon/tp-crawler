# TP 1 : Construire un crawler minimal

## Présentation
**Auteur** : Alexandre Bidon

**Note** : Ce repo contient le code d'un TP du cours d'indexation web. Le sujet du TP est [disponible ici](https://github.com/AlexandreBidon/tp-crawler/blob/master/docs/TP1.pdf).

Ce repo présente une implémentation basique d'un crawler web. L'objectif est de récupérer un certain nombre d'url de pages en respectant les règles du crawling, à savoir :

- respecter la politeness : ne pas effectuer trop de requetes sur un meme site
- Ne pas crawler un site qui nous l'interdit : vérifier le robots.txt

### Comment lancer le crawler

Pour commencer il faut installer les dépendances du projet :

> pip install -r requirements.txt

Il est ensuite possible d'utiliser le crawler avec la commande suivante :

> python3 main.py --min_websites 30

L'argument **min_websites** correspond au nombre minimum de pages à crawler. Il est aussi possible d'utiliser l'argument **start_url** pour choisir la première url à scraper. 

La commande retourne un fichier texte dans le dossier *result*. Ce dossier contient la liste des pages qui ont été trouvées.

### Comment lancer les tests

Il est possible de lancer les tests de la manière suivante :

> python3 -m unittest tests.test_utils

## Fonctionnement

Le crawler est décomposée en deux classes **Crawler** et **SiteScraper**.

- **SiteScraper** : cette classe s'occupe de scraper un seul site. Elle prend en entrée l'url principale d'un site. On commence ensuite par chercher si le site contient un sitemap et on l'utilise pour trouver plus rapidement des pages. Si le site ne contient pas de sitemap on ne retourne que l'url principale. On cherche ensuite sur la page principale des liens pouvant mener vers d'autres sites.

- **Crawler** : cette classe s'occupe de la gestion globale du crawling. On ajoute les nouvelles pages trouvées par les **SiteScraper** dans la liste commune et on crawl de nouveau site.

L'utilisation des sitemaps permet de crawler plus rapidement un site web tout en respectant le robots.txt. Cela permet aussi de respecter la politeness en effectuant trop de requêtes à ce site.

## Limites

### Sitemap

Les sitemaps présentent plusieurs problèmes pour le script actuel :

- **sitemap compressé** : certains sites ont une sitemap en .xml.gz (par exemple twitch.tv). Ce cas de figure n'est actuellement pas pris en compte dans notre script. L'utilisation d'une librairie comme **[gzip](https://docs.python.org/3/library/gzip.html)** pourrait résoudre ce problème.

- **site sans sitemap** : certains sites n'ont pas de sitemap défini dans le fichier robots.txt. Le script actuel utilise uniquement le sitemap pour répertorier les pages d'un site avant de passer au suivant. Les pages de ce site ne sont donc pas ajoutées au répertoire. Il serait possible d'ajouter une nouvelle fonction qui traverse manuellement un site lorsqu'elle ne trouve pas de sitemap. Ce choix n'a pas été retenue afin de traverser un plus grand nombre de site plutot que de se concentrer sur un seul.
De la même manière, le script ne trouve pas les pages qui ne sont pas répertoriées dans le sitemap d'un site.

- **sitemap avec plusieurs langues** : certains sites présentent un grand nombre de sitemap pour chaque langue. Le crawling est donc très long sur ces sites.


## TODO

- ajouter du multithreading pour accélerer le crawling
