import requests

s = requests.session()

auth_data = {
    'log':'admin',
    'pwd':'Shahwan@707070#80'

}

res_login = s.post("https://www.shahwan.net/wp-login.php?loggedout=true&wp_lang=en_US",data=auth_data)
# desired_page = s.get("https://www.shahwan.net/wp-admin/admin.php?page=forminator-entries&form_type=forminator_forms&form_id=8459",auth=('Admin','Shahwan@707070#80'))
desired_page_2 = s.get("https://www.shahwan.net/wp-admin/admin.php?page=forminator")
print(res_login.url)
print(desired_page_2)

