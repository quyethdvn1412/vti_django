from django.shortcuts import render
from datetime import datetime

# Create your views here.

def show_info(request, name):
    info = {
        'countries': [
            'Viet Nam',
            'England',
            'Japan',
            'United States',
        ],
        'now': datetime.now()
    }
    return render(request, name + '.html', info)

def country_info(request, country_name):
    info = {
            "Viet Nam": "Việt Nam, tên gọi chính thức là Cộng hòa Xã hội Chủ nghĩa Việt Nam, là một quốc gia nằm ở cực Đông của bán đảo Đông Dương thuộc khu vực Đông Nam Á, giáp với Lào, Campuchia, Trung Quốc, biển Đông và vịnh Thái Lan.",
            "England": "Anh hay Anh Xứ (phân biệt với nước Anh/vương quốc Anh) (tiếng Anh: England, /ˈɪŋɡ.lənd/) là một quốc gia thuộc Vương quốc Liên hiệp Anh và Bắc Ireland.[7][8][9] Quốc gia này có biên giới trên bộ với Scotland về phía bắc và với Wales về phía tây. Biển Ireland nằm về phía tây bắc và biển Celtic nằm về phía tây nam của Anh. Anh tách biệt khỏi châu Âu lục địa qua biển Bắc về phía đông và eo biển Manche về phía nam. Anh nằm tại miền trung và miền nam đảo Anh và chiếm khoảng 5/8 diện tích của đảo; ngoài ra còn có trên 100 đảo nhỏ.",
            "Japan": "Nhật Bản (Nhật: 日本 Hepburn: Về âm thanh nàyNihon hoặc Về âm thanh nàyNippon?), trong khẩu ngữ thường được gọi tắt là Nhật, tên đầy đủ là Nhật Bản Quốc (日本国 Nihon-koku hoặc Nippon-koku?)[16], là một quốc gia và đảo quốc có chủ quyền nằm ở khu vực Đông Á. Quốc gia này nằm bên rìa phía đông của biển Nhật Bản và biển Hoa Đông, phía tây giáp với bán đảo Triều Tiên qua biển Nhật Bản, phía bắc giáp với vùng Viễn Đông của Liên bang Nga theo biển Okhotsk và phía nam giáp với đảo Đài Loan qua biển Hoa Đông. Nhật Bản là một phần của vành đai lửa và trải dài trên một quần đảo bao gồm 6852 đảo nhỏ có tổng diện tích 377.975 km vuông (145.937 sq mi); trong đó 5 hòn đảo chính bao gồm Hokkaido, Honshu, Shikoku, Kyushu, và Okinawa. Tokyo là đô thị lớn nhất nước này; các thành phố lớn bao gồm Yokohama, Osaka, Nagoya, Sapporo, Fukuoka, Kobe và Kyoto.",
            "United States": "Hợp chúng quốc Hoa Kỳ[17][19][20] (tiếng Anh: The United States of America, United States of America, USA hoặc U. S. A.), thường được gọi là Hoa Kỳ (tiếng Anh: United States, US hoặc U. S.) hay Mỹ (tiếng Anh: America) là một quốc gia cộng hòa lập hiến liên bang thuộc châu Mỹ, nằm tại Tây Bán cầu, lãnh thổ bao gồm 50 tiểu bang và một đặc khu liên bang (trong đó có 48 tiểu bang lục địa), thủ đô là Washington, D.C., thành phố lớn nhất là New York. Hoa Kỳ nằm ở giữa Bắc Mỹ, giáp biển Thái Bình Dương ở phía tây, Đại Tây Dương ở phía đông, Canada ở phía bắc và México ở phía nam. Tiểu bang Alaska nằm trong vùng tây bắc của lục địa Bắc Mỹ, giáp với Canada ở phía đông và Nga ở phía tây qua eo biển Bering. Tiểu bang Hawaii nằm giữa Thái Bình Dương. Hoa Kỳ có 14 vùng lãnh thổ trực thuộc nằm rải rác trong vùng biển Caribe và Thái Bình Dương cùng 326 Biệt khu thổ dân châu Mỹ.",
    }
    country_info = info[country_name]
    return render(request, 'country-info-detail.html', {"country_info": country_info})

    