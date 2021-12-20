import unicodedata
import requests
from bs4 import BeautifulSoup
import random

detective = ['http://samlib.ru/k/kac_jurgen_alekseewich/todd23jropa.shtml',
             'http://samlib.ru/k/kac_jurgen_alekseewich/todd23jropaipa1-13.shtml',
             'http://samlib.ru/k/kamjusha_a/daunshifter.shtml',
             'http://samlib.ru/s/starickij_d/11119.shtml',
             'http://samlib.ru/k/kalifulow_nikolaj_mihajlowich/yu3.shtml',
             'http://samlib.ru/e/esfirx_l/osobayriskovannaymissiaymarkizistringer.shtml',
             'http://samlib.ru/e/esfirx_l/raspravavzamkebelforsbruk.shtml',
             'http://samlib.ru/k/kalifulow_nikolaj_mihajlowich/01-c.shtml',
             'http://samlib.ru/r/ramira_s/778.shtml',
             'http://samlib.ru/r/rozhkowa/prichinamoejsmerti.shtml',
             'http://samlib.ru/a/aleks_bell/a_bely_slon2.shtml',
             'http://samlib.ru/k/kseniapv16/beregis.shtml',
             'http://samlib.ru/w/wasjukowskaja_o_o/inkubator_0002.shtml',
             'http://samlib.ru/w/wolgina_alena/ann_justin.shtml',
             'http://samlib.ru/p/pereguda_o_w/schastlivyjsluchaj.shtml',
             'http://samlib.ru/m/marija_knjazewa/takajawotprincessa13022015.shtml',
             'http://samlib.ru/i/iwanowa_w_e/ko-3.shtml',
             'http://samlib.ru/k/kalifulow_nikolaj_mihajlowich/yu2.shtml',
             'http://samlib.ru/d/dzhozef_p/zhiznxsmertxiprochieneprijatnosti.shtml',
             'http://samlib.ru/m/milowa_k_a/kukolnayaistoriya.shtml',
             'http://samlib.ru/s/starickij_d/11119.shtml']

fantastic = ['http://samlib.ru/s/seraja_z/carter.shtml',
             'http://samlib.ru/o/orlow_wadim_wiktorowich/matrix.shtml',
             'http://samlib.ru/b/bordukow_s_m/wvipzalekosmoporta-3.shtml',
             'http://samlib.ru/k/kangin_a_i/teni_shenivashady_1.shtml',
             'http://samlib.ru/g/golowteewa_e_w/nowajaeradocx.shtml',
             'http://samlib.ru/k/kaminjar_d_g/vitokiii-1.shtml',
             'http://samlib.ru/m/mah_m/mjglava2.shtml',
             'http://samlib.ru/k/kuskow_s_a/cgp-0330.shtml',
             'http://samlib.ru/k/kibalxchich_f/036.shtml',
             'http://samlib.ru/p/prosin_w_i/dolgogdanny_den.shtml',
             'http://samlib.ru/k/kuskow_s_a/cgp-0328.shtml',
             'http://samlib.ru/h/harchenko_aleksandr_wladimirowich/rails02.shtml',
             'http://samlib.ru/k/kibalxchich_f/043.shtml',
             'http://samlib.ru/p/piwnickaja_e/kript35.shtml',
             'http://samlib.ru/a/askerbekow_e_b/mkns2-7.shtml',
             'http://samlib.ru/k/kibalxchich_f/037.shtml',
             'http://samlib.ru/b/babichewa_o_a/shepotdrewnihdjun.shtml',
             'http://samlib.ru/s/sugralinow_d_s/levelupknockout.shtml',
             'http://samlib.ru/m/mashoshin_a_w/005mid.shtml',
             'http://samlib.ru/e/eduard_k/deliveryorder.shtml',
             'http://samlib.ru/m/mashoshin_a_w/900dostojnoe.shtml'
             ]

valid = [['http://samlib.ru/l/lerh_i_a/iv_05.shtml',
          'http://samlib.ru/h/hinewich_a_j/dzhore_3_p_28.shtml',
          'http://samlib.ru/b/bor_w_a/nw_fg_1.shtml',
          'http://samlib.ru/h/husnullin_a_s/sav.shtml',
          'http://samlib.ru/k/kurguzow_j_m/uk_5.shtml',
          'http://samlib.ru/z/zubachewa_t_n/tetrad77.shtml',
          'http://samlib.ru/s/shaurow_e_w/dokazatelstvo.shtml'],
         ['http://samlib.ru/w/wolkowa_a_n/cenaswobod.shtml',
          'http://samlib.ru/d/dashewskaja_a_w/007-5.shtml',
          'http://samlib.ru/t/temsin/obytowojpolxzeoruzhija.shtml',
          'http://samlib.ru/m/murzin_gennadij_iwanowich/25gi.shtml',
          'http://samlib.ru/l/lxwowa_l_a/lla666-31.shtml',
          'http://samlib.ru/a/aleksanda_a_c/studenetka30.shtml',
          ]]


def write_txt(url, k):

    page = requests.get(url)
    content = page.content.decode('cp1251').encode('utf8')
    html = BeautifulSoup(content, 'html.parser')
    proizv = html.dd.text.split('Комментарии')[0]
    proizv = unicodedata.normalize("NFKD", proizv)
    name = '%s_d.txt' % (k)
    with open('valid/%s' % (name), 'w', encoding='utf-8') as file:
        file.write(proizv)


for k, i in enumerate(valid[1]):
    write_txt(i, k)
    print(k)
