# GoogleMapsScraper
Scrapes data from Google Maps businesses using Playwright it simulates a user search. A free alternative to Google's map API.

# Output Example
## __Request Body__
__Name:__ Cafe <br>
__District/Area:__ Bostanlı <br>
__City:__ Izmir <br>
__Quantity:__ 20

## Returned JSON

<pre>
  [
    {
      "address": "Bostanlı, 2014. Sk., 35590 Karşıyaka/İzmir",
      "details": ["F34W+M5 Karşıyaka, İzmir"],
      "name": "Sokak Arası Cafe"
    },
    {
      "address": "Bostanlı, Cemal Gürsel Cd. No:470/A, 35540 Karşıyaka/İzmir",
      "details": ["F432+F9 Karşıyaka, İzmir"],
      "name": "Cafe La Vie",
      "phone": "(0232) 364 35 06"
    },
    {
      "address": "Atakent, Şht. Cengiz Topel Cd., 35590 Karşıyaka/İzmir",
      "details": ["facebook.com", "F35V+G7 Karşıyaka, İzmir"],
      "name": "Cafe's Fine Foods - Bostanlı",
      "phone": "(0232) 330 48 46"
    },
    {
      "address": "Bostanlı Mah, Cemal Bülbül Sk. No:27/C, 35590 Karşıyaka/İzmir",
      "details": ["F34W+JR Karşıyaka, İzmir"],
      "name": "The Optimist Co.",
      "phone": "(0232) 330 33 23"
    },
    {
      "address": "Bostanlı, 2010. Sk. 7 A, 35590 Karşıyaka/İzmir",
      "details": ["F442+94 Karşıyaka, İzmir"],
      "name": "Anka Cafe",
      "phone": "0533 471 72 69"
    },
    {
      "address": "Bostanlı, Ahmet Pendikli Sk No:16/B, 35540 Karşıyaka/İzmir",
      "details": ["bostanlicafe.com", "F34X+XP Karşıyaka, İzmir"],
      "name": "Bostanlı Cafe",
      "phone": "0531 211 66 66"
    },
    {
      "address": "Bostanlı Mh, Cemal Gürsel Cd. No:476 D:4A, 35590 Karşıyaka/İzmir",
      "details": ["F34X+3X Karşıyaka, İzmir"],
      "name": "Zoe Coffee.Co",
      "phone": "0507 746 78 65"
    },
    {
      "address": "Bostanlı, Cemal Gürsel Cd. 470-1 C, 35590 Karşıyaka/İzmir",
      "details": ["Menü", "ugglacoffee.com", "F432+G8 Karşıyaka, İzmir"],
      "name": "Uggla Coffee",
      "phone": "0532 678 27 77"
    },
    {
      "address": "Bostanlı, Şehitler Blv No:51/A, 35590 Karşıyaka/İzmir",
      "details": ["F462+5J Karşıyaka, İzmir"],
      "name": "Coffee Shisha",
      "phone": "(0232) 330 30 44"
    },
    {
      "address": "Bostanlı, Bestekar Yusuf Nalkesen Sk. No:12/B, 35590 Karşıyaka/İzmir",
      "details": ["instagram.com", "F35V+7X Karşıyaka, İzmir"],
      "name": "Myth Coffee & More",
      "phone": "0555 251 78 86"
    },
    {
      "address": "Bostanlı, Aşık Veysel Sk no:40/B, 35550 Karşıyaka/İzmir",
      "details": ["ildascafe.com", "F37V+Q5 Karşıyaka, İzmir"],
      "name": "İlda's Cafe",
      "phone": "(0232) 415 46 16"
    },
    {
      "address": "Bostanlı, Pekşen Apartmanı, Cemal Bülbül Sk. No: 21/B, 35590 Karşıyaka/İzmir",
      "details": ["instagram.com", "F34W+XW Karşıyaka, İzmir"],
      "name": "Maneli Cafe",
      "phone": "0553 904 42 91"
    },
    {
      "address": "Bostanlı Mahallesi Nebil Susup Sokak A D:No: 154, 35590 Karşıyaka",
      "details": ["F442+9M Karşıyaka, İzmir"],
      "name": "Locca Cafe",
      "phone": "(0232) 330 11 11"
    },
    {
      "address": "Bostanlı, Cemal Gürsel Cd. No:476/4 D:B, 35590 Karşıyaka/İzmir",
      "details": ["izmirguide.com", "F34X+4W Karşıyaka, İzmir"],
      "name": "Cafe Tömbeki"
    },
    {
      "address": "Bostanlı, 2014. Sk. No:13/A, 35590 Karşıyaka/İzmir",
      "details": ["gochescoffee.com", "F34W+PC Karşıyaka, İzmir"],
      "name": "Goche's Coffee"
    },
    {
      "address": "Bostanlı Vapur İskelesi, Hasan Ali Yücel Blv. No:39, 35590 Karşıyaka",
      "details": ["denizpark.com.tr", "F33W+5Q Karşıyaka, İzmir"],
      "name": "Denizpark Cafe & Restaurant",
      "phone": "(0232) 330 00 29"
    },
    {
      "address": "Bostanlı, Şht. Cengiz Topel Cd. No:4, 35540 Bostanlı/Karşıyaka/İzmir",
      "details": ["recis.com.tr", "F35V+FQ Karşıyaka, İzmir"],
      "name": "RCS Cafe & Restaurant",
      "phone": "(0232) 330 30 43"
    },
    {
      "address": "Bostanlı, Nebil Susup Sk. no:162/a, 35540 Karşıyaka/İzmir",
      "details": ["F442+G8 Karşıyaka, İzmir"],
      "name": "selluka coffee house",
      "phone": "(0232) 416 24 14"
    },
    {
      "address": "Bostanlı, Bestekar Yusuf Nalkesen Sk. 2-1 A, 35590 Karşıyaka/İzmir",
      "details": ["F34V+QQ Karşıyaka, İzmir"],
      "name": "Iro Cafe"
    }
  ]

</pre>
