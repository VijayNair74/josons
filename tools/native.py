# Native-script spellings of the confirmed local names in names.py (same "/" separators).
# Written by Claude from general knowledge: needs a native-speaker pass, especially or / as / kok / the trade-only names.
NATIVE = {
"turmeric": dict(hi="हल्दी", ml="മഞ്ഞൾ", ta="மஞ்சள்", te="పసుపు", kn="ಅರಿಶಿನ", mr="हळद", kok="हळद", gu="હળદર", bn="হলুদ", **{"or": "ହଳଦୀ"}, **{"as": "হালধি"}, pa="ਹਲਦੀ"),
"black_pepper": dict(hi="काली मिर्च", ml="കുരുമുളക്", ta="மிளகு", te="మిరియాలు", kn="ಕರಿಮೆಣಸು", mr="काळी मिरी", kok="मिरें", gu="કાળા મરી", bn="গোলমরিচ", **{"or": "ଗୋଲମରିଚ"}, **{"as": "জালুক"}, pa="ਕਾਲੀ ਮਿਰਚ"),
"long_pepper": dict(hi="पिपली", ml="തിപ്പലി", ta="திப்பிலி", te="పిప్పళ్ళు", kn="ಹಿಪ್ಪಲಿ", mr="पिंपळी", gu="લીંડી પીપર", bn="পিপুল", **{"or": "ପିପଲି"}, **{"as": "পিপলি"}, pa="ਪਿੱਪਲੀ"),
"pepper_stem": dict(hi="चव्य / चाब", ml="ചവ്യം / കാട്ടുതിപ്പലി", mr="चवक", gu="ચવક"),
"allspice": dict(ml="സർവസുഗന്ധി", kn="ಸರ್ವಸುಗಂಧಿ"),
"cloves": dict(hi="लौंग", ml="ഗ്രാമ്പൂ", ta="கிராம்பு", te="లవంగాలు", kn="ಲವಂಗ", mr="लवंग", kok="लोवंग", gu="લવિંગ", bn="লবঙ্গ", **{"or": "ଲବଙ୍ଗ"}, **{"as": "লং"}, pa="ਲੌਂਗ"),
"mace": dict(hi="जावित्री", ml="ജാതിപത്രി", ta="ஜாதிபத்திரி", te="జాపత్రి", kn="ಜಾಪತ್ರೆ", mr="जायपत्री", gu="જાવંત્રી", bn="জৈত্রী", pa="ਜਾਵਿੱਤਰੀ"),
"nutmeg": dict(hi="जायफल", ml="ജാതിക്ക", ta="ஜாதிக்காய்", te="జాజికాయ", kn="ಜಾಯಿಕಾಯಿ", mr="जायफळ", kok="जायफळ", gu="જાયફળ", bn="জায়ফল", **{"or": "ଜାଇଫଳ"}, **{"as": "জায়ফল"}, pa="ਜਾਇਫਲ"),
"wild_turmeric": dict(hi="जंगली हल्दी", ml="കസ്തൂരിമഞ്ഞൾ", ta="கஸ்தூரி மஞ்சள்", te="కస్తూరి పసుపు", kn="ಕಸ್ತೂರಿ ಅರಿಶಿನ", bn="বন হলুদ"),
"ambahaldi": dict(hi="आंबा हल्दी", ml="ആമ്പഹൾദി", mr="आंबेहळद", gu="આંબા હળદર", pa="ਅੰਬਾ ਹਲਦੀ"),
"galangal": dict(hi="कुलंजन", ml="അരത്ത / പേരരത്ത", ta="பேரரத்தை", mr="कोलिंजन", gu="કુલિંજન", bn="কুলঞ্জন", **{"or": "କୁଳଞ୍ଜନ"}, pa="ਕੁਲੰਜਨ"),
"zedoary": dict(hi="कचूर", ml="കച്ചോരം", ta="கிச்சிலிக் கிழங்கு", te="కచోరము", kn="ಕಚೋರ", mr="कचोरा", gu="કચૂરો", bn="শটি", pa="ਕਚੂਰ"),
"kudampuli": dict(hi="कोकम", ml="കുടംപുളി / പിണംപുളി", ta="குடம்புளி", kn="ಉಪ್ಪಗೆ", kok="कोकम", mr="कोकम", gu="કોકમ"),
"arecanut": dict(hi="सुपारी", ml="അടയ്ക്ക", ta="பாக்கு / கொட்டைப்பாக்கு", te="వక్క", kn="ಅಡಿಕೆ", mr="सुपारी", gu="સોપારી", bn="সুপারি / গুয়া", **{"or": "ଗୁଆ"}, **{"as": "তামোল"}, pa="ਸੁਪਾਰੀ"),
"coffee": dict(hi="कॉफ़ी बीज", ml="കാപ്പിക്കുരു", ta="காபி கொட்டை", te="కాఫీ గింజలు", kn="ಕಾಫಿ ಬೀಜ", mr="कॉफी बिया", gu="કોફી", bn="কফি", **{"or": "କଫି"}, **{"as": "কফি"}, pa="ਕੌਫ਼ੀ"),
"cocoa": dict(hi="कोको बीज", ml="കൊക്കോക്കുരു", ta="கொக்கோ", te="కోకో", kn="ಕೊಕೊ", mr="कोको", gu="કોકો", bn="কোকো", **{"or": "କୋକୋ"}, pa="ਕੋਕੋ"),
"cashew": dict(hi="काजू (कच्चा)", ml="കശുവണ്ടി / അണ്ടി", ta="முந்திரிக் கொட்டை", te="జీడి గింజలు", kn="ಗೇರು ಬೀಜ", mr="काजू बी", kok="काजू बी", gu="કાજુ", bn="কাজু বাদাম", **{"or": "କାଜୁ"}, **{"as": "কাজু"}, pa="ਕਾਜੂ"),
"samudraphal": dict(hi="समुद्रफल", mr="समुद्रफळ", gu="સમુદ્રફળ", bn="হিজল", pa="ਸਮੁੰਦਰਫਲ"),
"triphal": dict(hi="तेजफल / तिरफल", ml="മുള്ളിലം", ta="இறச்சை", te="రాచమాను", kn="ಜುಮ್ಮಿನ ಕಾಯಿ / ಕಡುಮೆಣಸು", mr="तिरफळ / चिरफळ", kok="तिरफळ", **{"as": "বাজাৰমণি"}),
"poolamuttu": dict(ml="പൂളമുട്ട്", kn="ಮರಾಠಿ ಮೊಗ್ಗು", ta="மராட்டி மொக்கு"),
"marotti": dict(hi="चालमोगरा", ml="മരോട്ടിക്കുരു", ta="மரவெட்டை / நீராடிமுத்து", te="నీరడి విత్తులు", kn="ತೊರಟ್ಟಿ / ಗರುಡಫಲ", mr="कडू कवठ", gu="ચાલમોગરા", bn="চালমুগরা", **{"or": "ଚାଲମୁଗ୍ରା"}, **{"as": "চালমুগ্রা"}, pa="ਚਾਲਮੋਗਰਾ"),
"nux_vomica": dict(hi="कुचला", ml="കാഞ്ഞിരക്കുരു", ta="எட்டி", te="ముష్టి", kn="ಕಾಸರಕ / ಕಂಜೀರ", mr="काजरा", kok="काझ्रो", gu="ઝેર કોચલા", bn="কুচিলা", **{"or": "କଚିଳା"}, **{"as": "কুচিলা"}, pa="ਕੁਚਲਾ"),
"cocculus": dict(hi="काकमारी", ml="പൊള്ളക്കുരു", ta="காக்கைக்கொல்லி", te="కాకమారి", kn="ಕಾಕಮಾರಿ / ಚಿಪ್ಪುಲ ಕಾಯಿ", mr="काकमारी", pa="ਕਾਕਮਾਰੀ"),
"rampatri": dict(hi="रामपत्री / जंगली जावित्री", ml="കാട്ടുപത്രി", mr="रामपत्री", gu="રામપત્રી", pa="ਰਾਮਪਤਰੀ"),
"ramgot": dict(hi="रामगोट / जंगली जायफल", pa="ਰਾਮਗੋਟ"),
"cycas": dict(hi="मदन मस्त का फूल", ml="മദനകാമ പൂ / ഈന്ത് പൂ", ta="மதன காம ராஜா", te="మదన కామాక్షి", kn="ಗೊಡ್ಡು ಈಚಲು"),
"nagkesar": dict(hi="नागकेसर", te="నాగకేసరాలు", mr="नागकेशर / सुरंगी", gu="નાગકેસર", bn="নাগেশ্বর / নাগকেশর", **{"as": "নাহৰ"}, pa="ਨਾਗਕੇਸਰ"),
}
# Sanskrit names in Devanagari, keyed by the Latin spelling in names.py
SA = {"Haridra": "हरिद्रा", "Maricha": "मरिच", "Pippali": "पिप्पली", "Chavya / Chavika": "चव्य / चविका", "Lavanga": "लवङ्ग",
      "Jatipatri": "जातिपत्री", "Jatiphala": "जातिफल", "Vana haridra": "वनहरिद्रा", "Kulanjana": "कुलञ्जन", "Shati / Karchura": "शटी / कर्चूर",
      "Vrikshamla": "वृक्षाम्ल", "Puga": "पूग", "Kajutaka": "काजूतक", "Hijjala": "हिज्जल", "Tuvaraka": "तुवरक",
      "Kupilu / Vishatinduka": "कुपीलु / विषतिन्दुक", "Kakamari": "काकमारी", "Hintala": "हिन्ताल", "Nagakeshara": "नागकेशर"}

# Qualifiers that tell apart products sharing one local name (mace flower vs slice, nutmeg grades, arecanut grades, coffee).
# Product name -> qualifier key; key -> {lang: script}. Same caveat: needs a native-speaker check.
PQ = {"Mace Flower": "whole", "Mace Slice": "slice", "Nutmeg with Shell": "shell", "Nutmeg Splits": "splits",
      "Nutmeg Shell Seconds": "shellsec", "Badala Arecanut": "second", "Mysore Arecanut": "mysore", "Coffee with Shell": "shell"}
QUAL = {
 "whole": dict(hi="साबुत", ml="മുഴുവൻ", ta="முழு", te="పూర్తి", kn="ಪೂರ್ಣ", mr="अख्खी", kok="संपूर्ण", gu="આખી", bn="আস্ত", **{"or": "ଗୋଟା"}, **{"as": "গোটা"}, pa="ਸਾਬਤ"),
 "slice": dict(hi="टुकड़ा", ml="കഷണം", ta="துண்டு", te="ముక్క", kn="ತುಂಡು", mr="तुकडा", kok="तुकडो", gu="ટુકડો", bn="টুকরা", **{"or": "ଖଣ୍ଡ"}, **{"as": "টুকুৰা"}, pa="ਟੁਕੜਾ"),
 "shell": dict(hi="छिलके सहित", ml="തോടോടെ", ta="ஓட்டுடன்", te="పొట్టుతో", kn="ಸಿಪ್ಪೆಯೊಂದಿಗೆ", mr="कवचासह", kok="कवचासकट", gu="છાલ સહિત", bn="খোসাসহ", **{"or": "ଖୋଳା ସହିତ"}, **{"as": "খোলাসহ"}, pa="ਛਿਲਕੇ ਸਮੇਤ"),
 "splits": dict(hi="टूटे टुकड़े", ml="പൊട്ടിയത്", ta="உடைந்தது", te="పగిలినవి", kn="ಒಡೆದದ್ದು", mr="तुकडे", kok="तुकडे", gu="તૂટેલા ટુકડા", bn="ভাঙা", **{"or": "ଭଙ୍ଗା"}, **{"as": "ভঙা"}, pa="ਟੁੱਟੇ ਟੁਕੜੇ"),
 "shellsec": dict(hi="छिलका (दूसरी श्रेणी)", ml="തോട് (രണ്ടാംതരം)", ta="ஓடு (இரண்டாம் தரம்)", te="పొట్టు (రెండవ రకం)", kn="ಸಿಪ್ಪೆ (ಎರಡನೇ ದರ್ಜೆ)", mr="कवच (दुय्यम)", kok="कवच (दुय्यम)", gu="છાલ (બીજી ગુણવત્તા)", bn="খোসা (দ্বিতীয় মানের)", **{"or": "ଖୋଳ (ଦ୍ୱିତୀୟ ଶ୍ରେଣୀ)"}, **{"as": "খোলা (দ্বিতীয় মানৰ)"}, pa="ਛਿਲਕਾ (ਦੂਜੀ ਕਿਸਮ)"),
 "second": dict(hi="दूसरी श्रेणी", ml="രണ്ടാംതരം", ta="இரண்டாம் தரம்", te="రెండవ రకం", kn="ಎರಡನೇ ದರ್ಜೆ", mr="दुय्यम", kok="दुय्यम", gu="બીજી ગુણવત્તા", bn="দ্বিতীয় মানের", **{"or": "ଦ୍ୱିତୀୟ ଶ୍ରେଣୀ"}, **{"as": "দ্বিতীয় মানৰ"}, pa="ਦੂਜੀ ਕਿਸਮ"),
 "mysore": dict(hi="मैसूर", ml="മൈസൂർ", ta="மைசூர்", te="మైసూరు", kn="ಮೈಸೂರು", mr="म्हैसूर", kok="म्हैसूर", gu="મૈસૂર", bn="মহীশূর", **{"or": "ମହୀଶୂର"}, **{"as": "মহীশূৰ"}, pa="ਮੈਸੂਰ"),
}

# ---- Nov 2026: items added from Manu's stock list (first drafts, need a native-speaker check) ----
NATIVE.update({
 "cinnamon": dict(hi="दालचीनी", ml="കറുവപ്പട്ട", ta="பட்டை", te="దాల్చిన చెక్క", kn="ಚಕ್ಕೆ"),
 "dry_ginger": dict(hi="सोंठ", ml="ചുക്ക്", ta="சுக்கு", te="శొంఠి", kn="ಸೊಂಠಿ"),
 "cardamom": dict(hi="इलायची", ml="ഏലക്ക", ta="ஏலக்காய்", te="యాలకులు", kn="ಏಲಕ್ಕಿ"),
 "star_anise": dict(hi="चक्रफूल", ml="തക്കോലം", ta="அன்னாசிப்பூ", te="అనాసపువ్వు"),
 "vanilla": dict(hi="वनीला", ml="വാനില", ta="வெனிலா", te="వెనిలా", kn="ವೆನಿಲ್ಲಾ"),
 "black_sesame": dict(hi="तिल", ml="എള്ള്", ta="எள்", te="నువ్వులు", kn="ಎಳ್ಳು"),
 "bay_leaf": dict(hi="तेज पत्ता", ta="பிரிஞ்சி இலை"),
 "clove_stem": dict(hi="लौंग की डंडी", ml="ഗ്രാമ്പൂ തണ്ട്", ta="கிராம்பு தண்டு"),
 "tamarind": dict(hi="इमली", ml="വാളൻപുളി", ta="புளி", te="చింతపండు", kn="ಹುಣಸೆ"),
 "chittaratta": dict(hi="छोटा कुलंजन", ml="ചിറ്റരത്ത", ta="சிற்றரத்தை"),
 "maramanjal": dict(ml="മരമഞ്ഞൾ", ta="மரமஞ்சள்"),
 "idampiri": dict(hi="मरोड़फली", ml="ഇടമ്പിരി വലമ്പിരി"),
 "soapnut": dict(hi="रीठा", ta="பூந்திக்கொட்டை", te="కుంకుడు కాయ", kn="ಅಂಟುವಾಳ"),
 "shikakai": dict(hi="शिकाकाई", ml="ചീയക്ക", ta="சீயக்காய்", te="శీకాయ", kn="ಶೀಗೆಕಾಯಿ"),
 "thethankottai": dict(hi="निर्मली", ml="തേറ്റാമ്പരൽ", ta="தேற்றான் கொட்டை"),
 "neervalam": dict(hi="जमालगोटा", ml="നീർവാളം", ta="நெர்வாளம்"),
 "padakizhangu": dict(hi="पाठा", ml="പാടക്കിഴങ്ങ്"),
 "dry_amla": dict(hi="आंवला", ml="നെല്ലിക്ക", ta="நெல்லிக்காய்", te="ఉసిరికాయ", kn="ನೆಲ್ಲಿಕಾಯಿ"),
 "pachotti": dict(hi="लोध", ml="പാച്ചോറ്റി"),
 "koova": dict(hi="तीखुर", ml="കൂവ"),
 "black_dammar": dict(hi="काला धूप", ml="തെള്ളി", ta="கருங்குங்கிலியம்"),
})
SA.update({"Tvak": "त्वक्", "Shunthi": "शुण्ठी", "Ela": "एला", "Tila": "तिल", "Tamalapatra": "तमालपत्र", "Amlika": "अम्लिका", "Avartani": "आवर्तनी",
           "Arishtaka": "अरिष्टक", "Kataka": "कतक", "Jayapala": "जयपाल", "Patha": "पाठा", "Amalaki": "आमलकी", "Lodhra": "लोध्र", "Tavakshiri": "तवक्षीरी"})
PQ.update({"Cardamom Seeds": "seeds", "Green Pepper": "green", "White Pepper": "white", "Tamarind (Seedless)": "seedless", "Tamarind (with Seed)": "seeded",
           "Tamarind Seed": "seedonly", "Marotti Oil (Chalmogra Oil)": "oil"})
QUAL.update({
 "seeds": dict(hi="बीज", ml="വിത്ത്", ta="விதை", te="గింజలు", kn="ಬೀಜ"),
 "green": dict(hi="हरी", ml="പച്ച", ta="பச்சை", te="పచ్చి", kn="ಹಸಿರು", mr="हिरवी", gu="લીલા", bn="সবুজ", pa="ਹਰੀ"),
 "white": dict(hi="सफ़ेद", ml="വെള്ള", ta="வெள்ளை", te="తెల్ల", kn="ಬಿಳಿ", mr="पांढरी", kok="धवी", gu="સફેદ", bn="সাদা", **{"or": "ଧଳା"}, **{"as": "বগা"}, pa="ਚਿੱਟੀ"),
 "seedless": dict(hi="बिना बीज", ml="കുരുവില്ലാത്ത", ta="கொட்டையில்லாத", te="గింజలు లేని", kn="ಬೀಜರಹಿತ"),
 "seeded": dict(hi="बीज सहित", ml="കുരുവോടെ", ta="கொட்டையுடன்", te="గింజలతో", kn="ಬೀಜಸಹಿತ"),
 "seedonly": dict(hi="बीज", ml="കുരു", ta="கொட்டை", te="గింజ", kn="ಬೀಜ"),
 "oil": dict(hi="तेल", ml="എണ്ണ", ta="எண்ணெய்", te="నూనె", kn="ಎಣ್ಣೆ", mr="तेल", kok="तेल", gu="તેલ", bn="তেল", **{"or": "ତେଲ"}, **{"as": "তেল"}, pa="ਤੇਲ"),
})

NATIVE.update({
 "cotton_seed": dict(hi="बिनौला", ml="പരുത്തിക്കുരു", ta="பருத்தி விதை", te="పత్తి గింజలు", kn="ಹತ್ತಿ ಬೀಜ"),
 "rubber_seed": dict(hi="रबर के बीज", ml="റബ്ബർ കുരു", ta="ரப்பர் விதை", te="రబ్బరు గింజలు", kn="ರಬ್ಬರ್ ಬೀಜ"),
 "silk_cotton": dict(hi="सेमल की रुई", ml="ഇലവ് പഞ്ഞി", ta="இலவம் பஞ்சு", te="బూరుగ పత్తి", kn="ಬೂರುಗ ಹತ್ತಿ"),
})
SA.update({"Karpasa-beeja": "कार्पास-बीज"})
