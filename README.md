### Tehtävä 1 (Olio-ohjelmointi)
Luo luokka nimeltä `Weapon` ja sille alustaja, jossa on parametrit `name`, `tier` ja `type`.
Tee luokalle ominaisuudet annetuista parametreista. Tee luokalle funktio nimeltä `increase_tier`, jolla on parametrina uusi taso.
Tee luokalle staattinen muuttuja nimeltä `created` ja nosta määrää aina uuden luokan luonnissa.

Ohjelman tulostuksen tulisi näyttää tältä:
```
Weapon: Wind Katana, Tier: Rare
Weapons created: 1
Weapon: Magma Bomb, Tier: Legendary
Weapons created: 2
Weapon: Wind Katana, Tier: Epic
```
### Tehtävä 2 (Assosisaatio)

Jatkoa edelliseen tehtävään! Luo luokka nimeltä `Build`, jonka parametrit jätetään tyhjäksi. Tee luokan alustajaan sanakirja, jossa on avain-arvoparit
seuraavasti: `"katana": None, "ranged": None, "charm": None, "ghost-weapon-1": None, "ghost-weapon-2": None`. Tee luokalle funktio nimeltä `change_gear` ja sen parametriksi Weapon-olio. Funktio hakee sanakirjasta Weapon-olion `type` avulla oikean aseen ja laittaa olion sen arvoksi. 

> [!TIP]
> Lisää alla oleva funktio Weapon luokkaan (parantaa luettavuutta tulostaessa)
> ```
>  def __repr__(self):
>        return f"Weapon {self.name} is of type {self.tier}"
> ```

Ohjelman tulostuksen tulisi näyttää tältä:
```
{'katana': None, 'ranged': None, 'charm': None, 'ghost-weapon-1': None, 'ghost-weapon-2': None}
{'katana': Weapon Wind Katana is of type Rare, 'ranged': None, 'charm': None, 'ghost-weapon-1': None, 'ghost-weapon-2': None}
```

### Tehtävä 3 (Periytyminen)

Jatkoa aikaisempaan! Luo luokka nimeltä `Character` ja lisää `Build` luokan aliluokaksi. Luokan alustajan parametrinä on `class_name` ja alustetaan nimi sekä kutsutaan yliluokan alustajaa. Luo luokalle myös parametriton funktio nimeltä `show_build` joka tulostaa sanakirjan sisällön.

Ohjelman tulostuksen tulisi näyttää tältä:
```
Assassin class with gear: {'katana': None, 'ranged': None, 'charm': None, 'ghost-weapon-1': None, 'ghost-weapon-2': None}
Assassin class with gear: {'katana': Weapon Wind Katana is of type Rare, 'ranged': None, 'charm': Weapon Assassin Charm is of type Epic, 'ghost-weapon-1': None, 'ghost-weapon-2': None}
```
