"""[Lista aleatoria]"""

"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣯⡷⣟⣯⢿⠽⠿⠽⣾⡷⣟⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣯⡿⣯⡷⣿⠋⠀⠀⡀⠀⠀⠀⠈⢻⣽⣟⣷⣟⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⡿⣯⣷⢿⡯⣟⣷⡄⠀⠀⡀⠀⠀⠀⢀⣼⢷⣻⣷⣻⣽⡿⣷⣟⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣯⡷⣟⡷⣟⡿⣞⣯⡿⣯⢷⣟⣿⣲⣴⡴⣶⣳⡿⣽⢿⣽⢾⣯⣷⢿⣯⣿⣽⣯⣷⡿⣯⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡽⣯⡷⣟⣯⢿⣻⣽⢿⣽⣻⣽⢿⣽⢾⣻⣞⣿⢽⣗⣿⣻⣯⣟⣯⣷⢿⣻⣷⣻⡾⣷⣟⣿⣻⢷⣿⣟⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣞⣯⣟⣷⣻⣯⢿⢽⣳⢿⡽⣾⣻⣾⣻⣽⢿⣽⣻⣾⣻⣽⢷⡿⣾⢯⡿⣾⣟⣿⣞⣯⡿⠋⠀⠀⠀⠀⠀⠉⠻⣽⣾⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣽⢯⣷⣻⠞⠉⠈⠀⠈⠉⠙⠫⣿⢽⣻⣞⡷⣿⡽⣿⣽⢷⣻⣽⣾⣟⣿⣻⣟⣿⣳⣟⣷⢿⣽⣇⠀⠀⠈⠀⠀⠀⠀⢀⣿⡷⣿⢿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡯⣯⣻⣺⣽⣺⣇⠀⠀⠈⢀⠀⠀⠀⠀⣺⡯⣷⢯⣿⣳⣿⣻⡾⣟⣿⣽⡾⣯⣟⣷⢿⣽⢯⡿⣽⣟⣷⢿⣷⣦⣦⣥⣤⣦⣾⡿⣯⣿⡿⣿⣻⡾⣽⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⢜⢕⢗⣳⣳⡳⣗⡯⣶⢤⣄⣀⣠⣠⣴⣺⣽⣽⣽⣻⣞⣷⣟⣾⣻⢿⣽⢾⣻⣽⡯⣟⣯⡿⣽⣻⣽⣾⣻⣟⣷⣟⣷⡿⣯⣿⣳⣿⡿⣯⢿⣽⣳⣟⣯⣟⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⡪⡸⡘⡜⡔⡵⡹⡵⣫⢯⢯⢯⡯⣷⣻⣞⡷⡷⣷⣻⡾⣽⣾⣽⢾⣻⣻⢾⣻⣽⢾⣻⢯⡷⣟⣯⣟⣷⢯⣷⡿⣽⣯⣷⡿⣿⡾⣟⡷⡿⣽⢽⣞⣾⣺⢾⣺⢯⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢪⢊⢢⠱⡡⡣⢣⢣⢫⢪⢳⢹⢝⢾⢽⣺⣞⣯⢿⡯⣷⢿⣻⡾⣾⣻⣽⢯⡿⠛⠚⠉⠙⠙⠻⢽⣗⡿⣾⣻⡷⣿⢿⡾⣷⡿⣟⡿⡽⡯⣟⣽⣳⣳⣳⢯⠟⢾⢽⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⢨⠢⡣⡱⢸⢨⠢⡣⡱⡱⡱⡹⡸⡱⡣⣗⢽⢽⢽⢯⢿⡽⣯⢷⣟⡾⡏⠀⠀⠀⠄⠀⠀⠀⠀⣻⡽⣯⡷⣿⣻⣿⣻⡯⣿⢽⣽⣫⣟⣗⣗⣗⡷⠋⠀⠀⠈⡯⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢪⠢⡣⢣⢪⢊⢆⢇⢣⢕⢜⢌⢎⢪⢪⢪⢪⢪⢳⢹⢝⢽⢽⢝⣟⣾⣻⣽⣤⣀⡀⡀⢀⢀⣠⣴⢿⡽⣷⢿⣟⣯⡷⣯⢯⢷⣻⣺⣺⣺⣺⣺⡺⠀⠀⠀⠀⢀⡯⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢕⢱⢑⠅⠀⠀⠈⠐⠕⡜⡌⡎⡜⡌⡆⡇⡕⡕⢕⢕⢕⢇⢗⢝⢞⢮⢞⣞⢾⢽⣽⣻⢯⡿⣽⢾⣻⣽⣟⡿⣽⡳⡯⣗⡿⣽⣺⣺⣺⣺⡺⣪⡃⠀⠈⠀⢀⡾⡽⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢕⢅⢇⠀⠀⠀⠀⠀⠀⠑⡜⡌⡆⢇⢎⢜⠔⡕⢕⢱⢑⢕⢕⢕⢕⢕⢵⢱⢫⡳⡳⡽⡽⡽⡯⣿⢽⣳⢯⢯⣗⢯⢯⣗⣟⣞⣞⣞⣞⣞⣞⢽⣂⠀⡀⣔⣗⢽⢽⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡣⡱⡸⡠⠀⠀⠀⠀⠀⠀⢸⠰⡑⢕⢱⢘⢜⢸⢘⢌⢎⢢⢣⢱⠱⡱⡱⡱⡱⡱⡹⡜⡽⡽⡽⡽⣽⡺⣝⣗⢗⡯⣗⢗⡵⣳⢵⣳⡳⣳⢵⣻⡺⡽⡽⠚⠊⠫⡯⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡕⢜⢌⢲⢀⠀⠀⠀⢀⢢⢃⢇⢣⢑⢕⠸⡐⡕⡱⡘⡌⡆⢇⢣⠣⡪⡪⡪⡪⡪⣪⢳⣝⣯⣟⢮⢯⡳⡵⣻⡪⠗⢯⣫⢾⢝⡮⣯⣳⣻⡺⣺⠝⠀⠀⠀⠀⣟⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢇⢣⢑⢅⢇⢝⢸⢘⢌⢎⢢⠱⡘⢔⢅⢣⠱⡘⡔⡱⠁⠁⠁⠁⠣⢣⠪⡪⡪⡪⣪⡺⣪⢷⢽⣹⢵⡫⡯⠊⠀⠀⠈⣞⢮⣻⣪⢗⣗⡵⣫⡏⠀⢀⠀⠀⣰⢯⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⡎⡜⢌⢆⢣⢊⢆⢕⢌⠆⡕⢅⠣⡑⡌⢆⢣⠱⡨⡢⠀⠀⠀⠀⠀⠈⠪⡪⡸⣘⢦⢫⢾⣝⣗⣗⢽⡚⠀⠀⠀⠀⢐⣗⢽⣪⣞⢽⣺⡺⡵⡅⠀⠀⠀⣰⡳⡯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⡢⢣⠱⡘⡔⡱⡐⢕⢔⠱⡨⠢⠑⠨⠨⠢⡡⢱⠨⢢⢀⠀⠀⠀⠀⠀⠀⢕⢜⢔⢵⡹⡵⣳⡳⣕⢯⠂⠀⠀⠀⢠⢯⡺⣝⢮⢞⣽⣪⢞⡽⡦⣄⡴⣺⡳⢯⣻⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⡊⢆⢣⠱⡨⢢⢑⢕⠰⡑⢜⠀⠀⠀⠀⠀⠁⠕⢌⠢⡑⢄⠀⠀⠀⠀⠀⡪⡸⡸⡸⡸⣝⡵⡯⣳⢽⢄⠀⡠⡸⣕⢷⢝⣞⢽⣝⣞⢮⣻⡪⣟⡮⠋⠀⠀⠈⣞⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠜⡌⡢⢱⠨⠢⡑⢔⠱⡘⢔⠀⠀⠀⠀⠀⠀⠈⠢⡑⢅⢕⠩⡒⢔⢔⠱⡑⡜⡌⡎⡞⡮⡯⣻⣪⢗⡽⣹⡹⠊⠃⠫⣳⢕⡯⣞⢮⢗⡷⣝⡷⠁⠀⠄⠀⠠⣗⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢘⢔⢘⠀⠀⠀⠈⠐⢑⢌⠢⡑⠄⠀⠀⠀⠀⠀⢨⠨⡂⢆⠣⡊⢆⢪⠸⡨⡢⢣⢣⢫⡺⣝⣗⢗⡽⣪⠇⠀⠀⠀⢀⣗⢯⣞⡵⡯⡯⣞⣗⠇⠀⠁⠀⢀⣞⣗⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡕⡌⡂⠀⠀⠀⠀⠀⠀⠢⡑⠜⢌⠢⢄⠄⡀⡐⢔⢁⠪⡐⡑⡌⢆⢕⠱⡨⢪⠪⡪⡪⣞⣵⣳⡫⡯⠎⠀⠀⠀⠀⣰⡳⣝⣞⢮⢯⢞⡵⡯⡆⠀⢀⣠⣞⢾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢜⢀⠀⠀⠀⠀⠀⠀⢌⢊⠢⡑⢅⠪⢨⠨⢂⠢⡑⢌⠢⡊⡢⠢⡃⡎⡪⢪⢪⡚⡮⣞⣞⢮⣻⠀⠀⠀⢀⣜⢮⢯⡺⡮⡯⣫⢗⡯⡯⣺⣝⢗⣗⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣔⢅⠢⡀⡀⠀⠀⡀⡪⢐⢑⢌⠢⡑⢅⢊⠢⡑⢌⠢⡑⢌⢂⠣⡑⡌⡪⡊⡆⡗⡽⣺⢮⣳⡳⣕⢤⢔⢧⠳⡽⣕⢯⣳⡫⣗⡯⣞⡽⣕⢷⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣵⣈⠢⡡⢑⠌⡐⢅⠢⠢⡑⢌⠢⡡⡑⢌⠢⠑⠈⠐⠡⢑⠌⡆⢕⢜⢜⢜⣝⢾⣕⣗⢽⣪⡳⠉⠀⠀⠈⡾⣕⢷⢽⢕⡯⣞⢾⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣕⡌⠢⡑⢌⢊⢌⠢⡑⠔⢌⠢⠁⠀⠀⠀⠀⠀⠑⢜⢌⢆⢇⢇⢷⢝⣮⡺⣕⠗⠁⠀⠀⠀⢐⡯⣺⢵⡫⡯⣾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣅⡆⠢⡑⢌⠪⡐⡡⠡⠀⠀⠀⠀⠀⠀⠐⡕⢌⢎⢎⢗⡯⣞⢮⣳⠁⠠⠀⠀⢀⡷⣝⢵⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣔⠌⢔⠨⡨⢂⢀⠀⠀⠀⠀⢐⠜⢌⠎⡎⣗⢽⡪⣗⢽⡀⠀⡀⡴⣹⢺⣪⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣂⡢⠡⢂⠢⠠⡐⠔⢅⢣⢱⢱⢳⢝⣝⢮⡳⣝⢽⢕⢯⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣔⣅⠕⢌⠪⡨⢢⠣⡣⣫⢳⢝⡵⣝⢮⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣬⣢⡣⣣⢳⣹⣱⣵⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""
# Note: Los Conjuntos No Poseen Orden al Imprimirse
# Note: Se Imprime en Orden Aleatorio
# Note: Los conjuntos no estan Ordenados

# -- No Puede cambiarse los Elementos
# -- Puede Agregarse Nuevos elementos

# ┌────────────────────────
# │  Conjuntos - Creación e Impresión
# └────────────────────────
thisset = {"apple", "banana", "cherry", "Numero1"}
print(thisset)
# {'banana', 'Numero1', 'apple', 'cherry'} (El orden puede variar)

# ┌────────────────────────
# │  Constructor
# └────────────────────────
thisset = set(("apple", "banana", "cherry"))
brackets  # Esto parece ser una nota o comentario visual en la imagen, no código ejecutable
print(thisset)  # {'cherry', 'apple', 'banana'} (El orden puede variar)

# ┌────────────────────────
# │  Recorra el conjunto e imprima los valores:
# └────────────────────────
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# ┌────────────────────────
# │  Compruebe si "banana" está presente en el set:
# └────────────────────────
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)  # True
