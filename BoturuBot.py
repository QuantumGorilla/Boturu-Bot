import logging, os, telegram
from telegram.ext import Updater, CommandHandler
import nekos, requests, re, random, sys

#Config logging

logging.basicConfig(
    level = logging.INFO, format="%(asctime) - %(name)s - %(levelname)s - %(message)s,"
)

logger = logging.getLogger()

#Ask Token
TOKEN = os.getenv("TOKEN")
mode = os.getenv("MODE")

if mode == "dev":
    def run(updater):
        updater.start_polling()
        updater.idle()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT","8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
        updater.bot.set_webhook(f"https://{HEROKU_APP_NAME}.herokuapp.com/{TOKEN}")
else:
    logger.info('Mode not specified.')
    sys.exit()

def taskete(update, context):
     update.message.reply_text("""
                              Senpai, estos son los comandos u//u: \n /taskete - Mostrar los comandos \n /doggo - Foto random de un doggo \n /neko - Foto random de un neko \n /hentai - NSFW ;) \n /dollar - Every dollar spent on... \n /oilo - Oilo \n /pat - uwu \n /baka - Baka >_< \n /hey - Hey, loco, que pasa valemia \n /navidad - la navidad es todo aquello \n /quien - Quién monda es Dorian? \n /buenosdias - Ohayo, darin! (Chayanne) \n /buenasnoches - Piolin te desea buenas noches \n /princesas - Comando especial para Valeria \n /noticias - Noticias iconicas de Colombia \n /despegala - Despegala, cachón \n /metienesque - Me tienes que sopletear \n /comedia - Donco media \n /mimir - Hora de mimir \n /die - I just wanna die \n /uypah - Uy, pah, lo dijiteeeeeeeee \n /respete - No, señor, respete \n /escribebien - Escribe bien, cachón \n /no - No \n /yes - Sí \n /simp - SIMP \n /ayno - Ay, no, eso sí jamás \n /bye - La despego \n /perro - Perro con perro \n /cagaste - Cagaste, master \n /fino - Fino, mi rey
                              """)

def get_url(identifier):
    if identifier == 0:
        contents = requests.get('https://random.dog/woof.json').json()
        url = contents['url']
        return url
    else:
        contents = requests.get('http://aws.random.cat//meow').json()
        url = contents['file']
        return url

def get_image_url(identifier):
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url(identifier)
        if identifier == 0:
            file_extension = re.search("([^.]*)$", url).group(1).lower()
        else:
            file_extension = re.search("([^.]*)$", url).group(0).lower()
    return url

def doggo(update, context):
    url = get_image_url(0)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def neko(update, context):
    url = get_image_url(1)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def random_target():
    possible = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
                'cum', 'erokemo', 'les', 'lewdk', 'lewd', 'eroyuri', 'eron', 
                'cum_jpg', 'nsfw_neko_gif', 'solo', 'anal', 'blowjob', 'pussy', 
                'tits', 'holoero', 'pussy_jpg', 'femdom', 'spank', 'erok', 'boobs',
                'ero']
    return random.choice(possible)

def hentai(update, context):
    context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=nekos.img(random_target()))

def dollar(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('gecg'))

def oilo(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('smug'))
    
def pat(update, context):
    reply_user = update.message.reply_to_message
    user = update.message.from_user
    if reply_user == None:
        if len(context.args) != 0:
            word = ' '
            context.bot.send_message(chat_id=update.effective_chat.id, text='@' + user['username'] + ' is patting ' + word.join(context.args) + ' uwu')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('pat'))
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('pat'))
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='@' + user['username'] + ' is patting ' + reply_user.from_user['first_name'] + ' uwu')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('pat'))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='@' + user['username'] + ' is patting ' + reply_user.from_user['first_name'] + ' ' + '(@'+ reply_user.from_user['username'] + ')' + ' uwu')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('pat'))

def baka(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = ' '
            context.bot.send_message(chat_id=update.effective_chat.id, text='B-b-baka, ' + word.join(context.args) + ' ! >_<')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='B-b-baka, ' + reply_user.from_user['first_name'] + ' ! >_<')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='B-b-baka, ' + reply_user.from_user['first_name'] + '(@' + reply_user.from_user['username'] + ')'+ ' ! >_<')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=nekos.img('baka'))
    
def hey(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Hey.mp4', 'rb'), supports_streaming=True)

def navidad(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Feliz navidad, s-senpai! uwu')
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('./media/Navidad.mp3', 'rb'))

def quien(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Quién?')
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Quien.mp4', 'rb'), supports_streaming=True)

def buenosdias(update,context):
    file = random.choice(os.listdir('media/chayanne'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/chayanne/'+file, 'rb'))
    
def buenasnoches(update, context):
    file = random.choice(os.listdir('media/buenas_noches'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/buenas_noches/'+file, 'rb'))

def princesas(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Princesas.mp4', 'rb'), supports_streaming=True)

def noticias(update, context):
    file = random.choice(os.listdir('media/noticias'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/noticias/'+file, 'rb'))
    
def despegala(update, context):
    try:    
        reply_user = update.message.reply_to_message
        if reply_user != None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Omae wa mou... Shindeiru')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/Shindeiru.png', 'rb'))
            context.bot.kickChatMember(chat_id=update.effective_chat.id, user_id=reply_user.from_user['id'])
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='No mandaste a despegarla a nadie, cachón')
    except:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/Hina-fail-ban.jpg', 'rb'))
        context.bot.send_message(chat_id=update.effective_chat.id, text='Hpta, el cv es admin')

def butifarra(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = ' '   
            context.bot.send_message(chat_id=update.effective_chat.id, text='Hey, ' + word.join(context.args))
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Butifarra.mp4', 'rb'), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Butifarra.mp4', 'rb'), supports_streaming=True)
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Hey, ' + reply_user.from_user['first_name'])
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Butifarra.mp4', 'rb'), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Hey, ' + reply_user.from_user['first_name'] + ' ' + '(@' + reply_user.from_user['username']+')')        
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Butifarra.mp4', 'rb'), supports_streaming=True)

def comedia(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir('media/comedia'))
    if reply_user == None:
        if len(context.args) != 0:
            word = ' '
            context.bot.send_message(chat_id=update.effective_chat.id, text='Jajaja cule chiste hpta, ' + word.join(context.args) + ', cv')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/comedia/'+file, 'rb'))
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/comedia/'+file, 'rb'))
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Jajaja cule chiste hpta, ' + reply_user.from_user['first_name'] + ', cv')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/comedia/'+file, 'rb'))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Jajaja cule chiste hpta, ' + reply_user.from_user['first_name'] + ' ' + '(@' + reply_user.from_user['username']+')' + ', cv')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/comedia/'+file, 'rb'))

def mimir(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hora de mimir! uwu')
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Mimir.mp4', 'rb'), supports_streaming=True)

def die(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Solo quiero morir :(')
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Die.mp4', 'rb'), supports_streaming=True)

def trece(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = ' '
            context.bot.send_message(chat_id=update.effective_chat.id, text='Uy, pah, LO DIJITEEEEEE ' + '(' + word.join(context.args) + ')')
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Trece.mp4', 'rb'), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Trece.mp4', 'rb'), supports_streaming=True)
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Uy, pah, LO DIJITEEEEEE ' + '(' + reply_user.from_user['first_name'] + ')')
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Trece.mp4', 'rb'), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Uy, pah, LO DIJITEEEEEE ' + '(@' + reply_user.from_user['username'] + ')')
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Trece.mp4', 'rb'), supports_streaming=True)

def respete(update, context):
    reply_user = update.message.reply_to_message
    if reply_user == None:
        if len(context.args) != 0:
            word = ' '
            context.bot.send_message(chat_id=update.effective_chat.id, text='Respeta, ' + word.join(context.args) + ', cachón')
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Respete.mp4', 'rb'), supports_streaming=True)
        else:
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Respete.mp4', 'rb'), supports_streaming=True)
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Respeta, ' + reply_user.from_user['first_name'] + ', cachón')
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Respete.mp4', 'rb'), supports_streaming=True)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Respeta, '+ reply_user.from_user['first_name'] + ' (@' + reply_user.from_user['username'] + '), cachón')
            context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Respete.mp4', 'rb'), supports_streaming=True)

def escribeBien(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Escribe bien, cachón')
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/EscribeBien.mp4', 'rb'), supports_streaming=True)

def no(update,context):
    file = random.choice(os.listdir('media/no'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/no/'+file, 'rb'))
    
def yes(update, context):
    file = random.choice(os.listdir('media/yes'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/yes/'+file, 'rb'))

def simp(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir('media/simp'))
    if reply_user == None:
        if len(context.args) != 0:
            word = ' '
            context.bot.send_message(chat_id=update.effective_chat.id, text='SIMP, ' + word.join(context.args))
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/simp/'+file, 'rb'))
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/simp/'+file, 'rb'))
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='SIMP, ' + reply_user.from_user['first_name'])
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/simp/'+file, 'rb'))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='SIMP, '+ reply_user.from_user['first_name'] + ' (@' + reply_user.from_user['username'] + ')')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/simp/'+file, 'rb'))

def ayno(update, context):
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Ayno.mp4', 'rb'), supports_streaming=True)  

def bye(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='La despego, chao, cachones')
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Bye.mp4', 'rb'), supports_streaming=True)

def perro(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Perro con perro, perro con perro')
    context.bot.send_video(chat_id=update.effective_chat.id, video=open('./media/Perro.mp4', 'rb'), supports_streaming=True)

def cagaste(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir('media/cagaste'))
    if reply_user == None:
        if len(context.args) != 0:
            word = ' '
            context.bot.send_message(chat_id=update.effective_chat.id, text='Cagaste, ' + word.join(context.args))
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/cagaste/'+file, 'rb'))
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/cagaste/'+file, 'rb'))
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Cagaste, ' + reply_user.from_user['first_name'])
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/cagaste/'+file, 'rb'))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Cagaste, '+ reply_user.from_user['first_name'] + ' (@' + reply_user.from_user['username'] + ')')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/cagaste/'+file, 'rb'))

def fino(update, context):
    reply_user = update.message.reply_to_message
    file = random.choice(os.listdir('media/fino'))
    if reply_user == None:
        if len(context.args) != 0:
            word = ' '
            context.bot.send_message(chat_id=update.effective_chat.id, text='Fino, mi rey (' + word.join(context.args) + ')')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/fino/'+file, 'rb'))
        else:
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/fino/'+file, 'rb'))
    else:
        if reply_user.from_user['username'] == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Fino, mi rey (' + reply_user.from_user['first_name'] + ')')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/fino/'+file, 'rb'))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='Fino, mi rey (@'+ reply_user.from_user['username'] + ')')
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('./media/fino/'+file, 'rb'))

def main():
    Boturu = telegram.Bot(token = TOKEN)
    updater = Updater(Boturu.token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('taskete', taskete))
    dp.add_handler(CommandHandler('doggo', doggo))
    dp.add_handler(CommandHandler('neko', neko))
    dp.add_handler(CommandHandler('hentai', hentai))
    dp.add_handler(CommandHandler('dollar', dollar))
    dp.add_handler(CommandHandler('oilo', oilo))
    dp.add_handler(CommandHandler('pat', pat))
    dp.add_handler(CommandHandler('baka', baka))
    dp.add_handler(CommandHandler('hey', hey))
    dp.add_handler(CommandHandler('navidad', navidad))
    dp.add_handler(CommandHandler('quien', quien))
    dp.add_handler(CommandHandler('buenosdias', buenosdias))
    dp.add_handler(CommandHandler('buenasnoches', buenasnoches))
    dp.add_handler(CommandHandler('princesas', princesas))
    dp.add_handler(CommandHandler('noticias', noticias))
    dp.add_handler(CommandHandler('despegala', despegala))
    dp.add_handler(CommandHandler('metienesque', butifarra))
    dp.add_handler(CommandHandler('comedia', comedia))
    dp.add_handler(CommandHandler('mimir', mimir))
    dp.add_handler(CommandHandler('die', die))
    dp.add_handler(CommandHandler('uypah', trece))
    dp.add_handler(CommandHandler('respete', respete))
    dp.add_handler(CommandHandler('escribebien', escribeBien))
    dp.add_handler(CommandHandler('no', no))
    dp.add_handler(CommandHandler('yes', yes))
    dp.add_handler(CommandHandler('simp', simp))
    dp.add_handler(CommandHandler('ayno', ayno))
    dp.add_handler(CommandHandler('bye', bye))
    dp.add_handler(CommandHandler('perro', perro))
    dp.add_handler(CommandHandler('cagaste', cagaste))
    dp.add_handler(CommandHandler('fino', fino))
    run(updater)
    
if __name__ == '__main__':
    main()
