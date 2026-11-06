# New catalogue items from Manu's stock list (Nov 2026). Text-only for now: img/soon.jpg is a "photo coming soon" tile.
# Local names are first drafts (hi/ml/ta, some te/kn) and need a native-speaker check. Missing languages fall back to Hindi/trade name.
P = lambda slug, name, sub, cat, c, grade=False: dict(slug=slug, name=name, sub=sub, grade=grade, cat=cat, c=c, img='img/soon.jpg')
C = lambda en, bot, sa, names, aka=(), trade=None: dict(en=en, trade=trade or en, bot=bot, sa=sa, names=names, aka=list(aka), search=[en, *aka, *names.values()], note='')

NEW_SPICES = [  # inserted after Allspice
    P('cinnamon', 'Cinnamon', 'Bark', 'spices', 'cinnamon'),
    P('dry-ginger', 'Dry Ginger', 'Zingiber officinale', 'spices', 'dry_ginger'),
    P('cardamom', 'Cardamom', 'Dry · green', 'spices', 'cardamom', True),
    P('cardamom-seeds', 'Cardamom Seeds', 'Decorticated seeds', 'spices', 'cardamom', True),
    P('green-pepper', 'Green Pepper', 'Piper nigrum · green', 'spices', 'black_pepper', True),
    P('white-pepper', 'White Pepper', 'Piper nigrum · white', 'spices', 'black_pepper', True),
    P('star-anise', 'Star Anise', 'Illicium verum', 'spices', 'star_anise'),
    P('vanilla', 'Vanilla', 'Vanilla planifolia · beans', 'spices', 'vanilla'),
    P('black-sesame', 'Black Sesame', 'Sesamum indicum', 'spices', 'black_sesame'),
    P('bay-leaf', 'Bay Leaf', 'Cinnamomum tamala', 'spices', 'bay_leaf'),
    P('clove-stem', 'Clove Stem', 'Clove sticks', 'spices', 'clove_stem'),
    P('tamarind-seedless', 'Tamarind (Seedless)', 'Cleaned, seedless', 'spices', 'tamarind', True),
    P('tamarind-with-seed', 'Tamarind (with Seed)', 'Whole pods, seeded', 'spices', 'tamarind', True),
    P('tamarind-seed', 'Tamarind Seed', 'Tamarindus indica', 'spices', 'tamarind', True),
]
NEW_HERBAL = [  # appended at the end
    P('chittaratta', 'Chittaratta (Lesser Galangal)', 'Alpinia calcarata', 'herbal', 'chittaratta'),
    P('maramanjal', 'Maramanjal (Tree Turmeric)', 'Coscinium fenestratum', 'herbal', 'maramanjal'),
    P('idampiri-valampiri', 'Idampiri Valampiri', 'Helicteres isora', 'herbal', 'idampiri'),
    P('soapnut', 'Soapnut (Reetha)', 'Sapindus spp.', 'herbal', 'soapnut'),
    P('shikakai', 'Shikakai', 'Acacia concinna', 'herbal', 'shikakai'),
    P('thethankottai', 'Thethankottai (Clearing Nut)', 'Strychnos potatorum', 'herbal', 'thethankottai'),
    P('neervalam', 'Neervalam (Croton Seed)', 'Croton tiglium', 'herbal', 'neervalam'),
    P('padakizhangu', 'Padakizhangu (Pareira Root)', 'Cyclea peltata', 'herbal', 'padakizhangu'),
    P('dry-amla', 'Dry Amla (Nellikka)', 'Phyllanthus emblica', 'herbal', 'dry_amla'),
    P('pachotti-tholi', 'Pachotti Tholi (Lodhra Bark)', 'Symplocos racemosa', 'herbal', 'pachotti'),
    P('koova-starch', 'Koova Starch (Arrowroot)', 'Powder', 'herbal', 'koova'),
    P('black-dammar', 'Black Dammar (Thelli)', 'Canarium strictum · resin', 'herbal', 'black_dammar'),
    P('marotti-oil', 'Marotti Oil (Chalmogra Oil)', 'Hydnocarpus oil', 'herbal', 'marotti', True),
]
NEW_COMM = {
 'cinnamon': C('Cinnamon', '[confirm species]', 'Tvak', dict(hi='Dalchini', ml='Karuvapatta', ta='Pattai', te='Dalchina chekka', kn='Chakke'), ['Cassia', 'Dalchini']),
 'dry_ginger': C('Dry Ginger', 'Zingiber officinale', 'Shunthi', dict(hi='Sonth', ml='Chukku', ta='Sukku', te='Sonthi', kn='Sonthi'), ['Sukku', 'Saunth']),
 'cardamom': C('Cardamom', 'Elettaria cardamomum', 'Ela', dict(hi='Elaichi', ml='Elakka', ta='Elakkai', te='Yalakulu', kn='Elakki'), ['Elachi', 'Cardamon']),
 'star_anise': C('Star Anise', 'Illicium verum', '', dict(hi='Chakraphool', ml='Thakkolam', ta='Annasi poo', te='Anasa puvvu'), ['Chakri phool']),
 'vanilla': C('Vanilla', 'Vanilla planifolia', '', dict(hi='Vanila', ml='Vanila', ta='Venila', te='Venila', kn='Venilla'), ['Vanilla beans']),
 'black_sesame': C('Black Sesame', 'Sesamum indicum', 'Tila', dict(hi='Til', ml='Ellu', ta='Ellu', te='Nuvvulu', kn='Ellu'), ['Gingelly', 'Til', 'Kala til']),
 'bay_leaf': C('Bay Leaf', 'Cinnamomum tamala', 'Tamalapatra', dict(hi='Tej patta', ml='Edana ela', ta='Birinji ilai'), ['Tejpatta', 'Indian bay leaf']),
 'clove_stem': C('Clove Stem', 'Syzygium aromaticum (stalks)', '', dict(hi='Laung ki dandi', ml='Grambu thandu', ta='Kirambu thandu'), ['Clove sticks', 'Lavang kadi']),
 'tamarind': C('Tamarind', 'Tamarindus indica', 'Amlika', dict(hi='Imli', ml='Valanpuli', ta='Puli', te='Chintapandu', kn='Hunase'), ['Puli', 'Puli kuru']),
 'chittaratta': C('Chittaratta (Lesser Galangal)', 'Alpinia calcarata', '', dict(hi='Chhota kulanjan', ml='Chittaratta', ta='Sitrarathai'), ['Kulanjan']),
 'maramanjal': C('Maramanjal (Tree Turmeric)', 'Coscinium fenestratum', '', dict(ml='Maramanjal', ta='Maramanjal'), ['Mara manjal']),
 'idampiri': C('Idampiri Valampiri', 'Helicteres isora', 'Avartani', dict(hi='Marorphali', ml='Idampiri valampiri'), ['Valampiri', 'Indian screw tree']),
 'soapnut': C('Soapnut (Reetha)', 'Sapindus spp.', 'Arishtaka', dict(hi='Reetha', ta='Poonthi kottai', te='Kunkudu kaya', kn='Antuvala kayi'), ['Reetha', 'Ritha']),
 'shikakai': C('Shikakai', 'Acacia concinna', '', dict(hi='Shikakai', ml='Cheeyakkai', ta='Seekakai', te='Seekaya', kn='Shige kayi'), ['Seekakai', 'Sheekakai']),
 'thethankottai': C('Thethankottai (Clearing Nut)', 'Strychnos potatorum', 'Kataka', dict(hi='Nirmali', ml='Thettamparal', ta='Thetran kottai'), ['Thethamkottai', 'Nirmali']),
 'neervalam': C('Neervalam (Croton Seed)', 'Croton tiglium', 'Jayapala', dict(hi='Jamalgota', ml='Neervalam', ta='Nervalam'), ['Jamalgota', 'Nervalam']),
 'padakizhangu': C('Padakizhangu (Pareira Root)', 'Cyclea peltata', 'Patha', dict(hi='Patha', ml='Padakizhangu'), ['Padathali', 'Pada kizhangu']),
 'dry_amla': C('Dry Amla (Nellikka)', 'Phyllanthus emblica', 'Amalaki', dict(hi='Amla', ml='Nellikka', ta='Nellikkai', te='Usirikaya', kn='Nellikayi'), ['Amla', 'Indian gooseberry', 'Nellikka']),
 'pachotti': C('Pachotti Tholi (Lodhra Bark)', 'Symplocos racemosa', 'Lodhra', dict(hi='Lodh', ml='Pachotti'), ['Lodhra', 'Lodh']),
 'koova': C('Koova Starch (Arrowroot)', '[confirm species]', 'Tavakshiri', dict(hi='Tikhur', ml='Koova'), ['Arrowroot', 'Koova podi']),
 'black_dammar': C('Black Dammar (Thelli)', 'Canarium strictum', '', dict(hi='Kala dhoop', ml='Thelli', ta='Karunkungiliyam'), ['Thelli', 'Dammar']),
}
for _p in NEW_SPICES:
    if _p['slug']=='cinnamon': _p['img']='img/q_cinn.jpg'  # AI-generated image, used with owner's OK; replace with Manu's own photo

AI_IMG = ['dry-ginger', 'cardamom', 'cardamom-seeds', 'green-pepper', 'white-pepper', 'star-anise', 'vanilla', 'black-sesame', 'bay-leaf', 'clove-stem', 'tamarind-seedless', 'tamarind-with-seed', 'tamarind-seed']
for _p in NEW_SPICES:
    if _p['slug'] in AI_IMG: _p['img'] = 'img/q_%s.jpg' % _p['slug']
