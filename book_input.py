import requests


#years=&brand=5714&model=5714-5872&city=All&op=CHECK+INVENTORY%3Cspan+class%3D%22icon+glyphicon+glyphicon-arrow-right+custom-form-glyph-arrow%22%3E%3C%2Fspan%3E&form_build_id=form-zUn6w25DY4TZH9Vc7p-U4LIPrxuhVUDMbUIlOQCXAzM&form_id=search_site_parts_form

headers = {
'Host': 'www.kennyupull.com',
'Connection': 'keep-alive',
'Content-Length': 8182,
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Origin': 'http://www.kennyupull.com',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'http://www.kennyupull.com/en/car-parts',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,be;q=0.7'
#'Cookie: '__smVID=19534a26b3a1aa0e92bffe0852b5715af396a8d8c8eff067078c9ae0bd6c16ff; __smVID=19534a26b3a1aa0e92bffe0852b5715af396a8d8c8eff067078c9ae0bd6c16ff; _ga=GA1.2.364122427.1522003929; SESS9cbce6802911a10fa99784a3bbb6efdf=VSHpHqrd_jCK6v80yk5cyYZn-tg7dyVMPzXnpwuyaUo; has_js=1; _gid=GA1.2.1109761580.1524754323; _gat=1; __smToken=iCRIZOmEziR1R4MCSIJvu3Ew'
}


data = {
'field_car_year_value': '', 
'field_car_brand_tid': 5714,
'field_car_model_tid': 5968,
'sort_by': 'field_arrival_date_value',
'view_name': 'car_parts_view',
'view_display_id': 'block',
'view_args': '',
'view_path': 'node/7',
'view_base_path': '', 
'view_dom_id': 'c3436d8d6d285a411b8c3d3dcafb9f91',
'pager_element': 0
}

response = requests.post(url = 'http://www.kennyupull.com/en/views/ajax', data = data)

print(response)
print(response.text)

