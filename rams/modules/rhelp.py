from config import CMD_HANDLER as cmd
from .help import add_command_help

add_command_help(
    "dm",
    [
        ["dm", "mengirim pesan ke chat pribadi (contoh: `.dm @thisrama Hii`."],
    ],
)

add_command_help(
    "tag",
    [
        ["admins", "Get chats Admins list."],
        ["kickdel", "To Kick deleted Accounts."],
        [
            "everyone `or` {cmd}tagall",
            "to mention Everyone ",
        ],
        [
            "botlist",
            "To get Chats Bots list",
        ],
    ],
)

add_command_help(
    "admin",
    [
        ["ban <reply/username/userid> <alasan>", "Membanned member dari grup."],
        [
            "unban <reply/username/userid> <alasan>",
            "Membuka banned member dari grup.",
        ],
        [f"kick <reply/username/userid>", "Mengeluarkan pengguna dari grup."],
        [
            f"promote atau {cmd}fullpromote",
            "Mempromosikan member sebagai admin atau cofounder.",
        ],
        [f"demote", "Menurunkan admin sebagai member."],
        [
            f"mute <reply/username/userid>",
            "Membisukan member dari Grup.",
        ],
        [
            f"unmute <reply/username/userid>",
            "Membuka mute member dari Grup.",
        ],
        [
            f"pin <reply>",
            "Untuk menyematkan pesan dalam grup.",
        ],
        [
            f"unpin <reply>",
            "Untuk melepaskan pin pesan dalam grup.",
        ],
        [
            f"setgpic <reply ke foto>",
            "Untuk mengubah foto profil grup",
        ],
    ],
)

add_command_help(
    "afk",
    [
        [
            "afk <alasan>",
            "Memberi tahu orang yang menandai atau membalas salah satu pesan atau dm anda kalau anda sedang afk",
        ],
    ],
)
add_command_help(
    "animation",
    [
        ["fuck", "Untuk menampilkan animasi jari tengah."],
        ["dino", "Untuk menampilkan animasi dikejar dino."],
        ["santet", "Untuk menampilkan animasi menyantet onlen."],
        ["gabut", "Untuk menampilkan animasi gabut."],
        ["sayang", "Untuk menampilkan animasi sayang."],
        ["hack", "Untuk menampilkan animasi ngehek palsu."],
        ["bomb", "Untuk menampilkan animasi Bomb."],
        ["brain", "Untuk menampilkan animasi  Brain 🧠."],
        ["kontol", "Untuk menampilkan art kontol."],
        ["penis", "Untuk menampilkan art penis dengan emoji."],
        ["tembak", "Untuk menampilkan art nembak."],
        ["bundir", "Untuk menampilkan art bundir."],
        ["helikopter", "Untuk menampilkan art helikopter."],
        ["y", "Untuk menampilkan art y sj."],
        ["awk", "Untuk menampilkan art awkowkowk."],
        ["nah", "Untuk menampilkan art love."],
        ["ajg", "Untuk menampilkan art anjing."],
        ["babi", "Untuk menampilkan art babi."],
        ["hug", "To get A Hug Gifs anime."],
        ["hmm", "Get Random Hmmm."],
        ["wink", "To Get A Winking Gifs."],
        ["love", "To Propose Someone."],
        ["loveyou", "It Will Send Random Emojis."],
        [
            "pat",
            "To get a pat gifs",
        ],
        [
            "pikachu",
            "to get a Pikachu Gifs",
        ],
        [
            "kill",
            "To kill Someone randomly",
        ],
        [
            "wtf",
            "Wtf animation",
        ],
        [
            "ding",
            "Get Dong",
        ],
        [
            "ganstar",
            "Animation Gangster",
        ],
        [
            "charge",
            " Tesla animation charging",
        ],
    ],
)

add_command_help(
    "fundb",
    [
        [
            "asupan",
            "Asupan video TikTok",
        ],
        [f"ayang & {cmd}ayg", "Mencari Foto ayang kamu /nNote: Modul ini buat cwo yang jomblo."],
        [f"ppcp & {cmd}cpp", "Mencari Foto PP Couple Random."],
        [f"ppanime & {cmd}anim", "Mencari Foto PP Couple Anime."],
    ],
)

add_command_help(
    "broadcast",
    [
        [
            "gcast <text/reply>",
            "Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)",
        ],
        [
            "gucast <text/reply>",
            "Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)",
        ],
        [
            "blchat",
            "Untuk Mengecek informasi daftar blacklist gcast.",
        ],
        [
            "addblacklist",
            "Untuk Menambahkan grup tersebut ke blacklist gcast.",
        ],
        [
            "delblacklist",
            f"Untuk Menghapus grup tersebut dari blacklist gcast.\n\n  •  **Note : **Ketik perintah** `{cmd}addblacklist` **dan** `{cmd}delblacklist` **di grup yang kamu Blacklist.",
        ],
    ],
)
add_command_help(
    "carbon",
    [
        ["carbon <reply>", "Carbonisasi teks dengan pengaturan default."],
    ],
)
add_command_help(
    "create",
    [
        ["create ch", "Untuk membuat channel telegram dengan userbot"],
        ["create gc", "Untuk membuat group telegram dengan userbot"],
    ],
)
add_command_help(
    "fakeaction",
    [
        ["ftyp [detik]", "Menampilkan Pengetikan Palsu dalam obrolan."],
        ["fgame [detik]", "Menampilkan sedang bermain game Palsu dalam obrolan."],
        [
            "faud [detik]",
            "Menampilkan tindakan merekam suara palsu dalam obrolan.",
        ],
        [
            "fvid [detik]",
            "Menampilkan tindakan merekam video palsu dalam obrolan.",
        ],
        [
            "frou [detik]",
            "Menampilkan tindakan merekam video palsu dalam obrolan.",
        ],
        [
            "fpho [detik]",
            "Menampilkan tindakan mengirim foto palsu dalam obrolan.",
        ],
        [
            "fstick [detik]",
            "Menampilkan tindakan memilih Sticker palsu dalam obrolan.",
        ],
        [
            "fcon [detik]",
            "Menampilkan tindakan Share Contact palsu dalam obrolan.",
        ],
        [
            "floc [detik]",
            "Menampilkan tindakan Share Lokasi palsu dalam obrolan.",
        ],
        [
            "fdoc [detik]",
            "Menampilkan tindakan tengirim Document/File palsu dalam obrolan.",
        ],
        [
            "fscreen [jumlah]",
            "Menampilkan tindakan screenshot palsu. (Gunakan di Obrolan Pribadi)",
        ],
        ["fstop", "Memberhentikan tindakan palsu dalam obrolan."],
    ],
)
add_command_help(
    "globals",
    [
        [
            "gban <reply/username/userid>",
            "Melakukan Global Banned Ke Semua Grup Dimana anda Sebagai Admin.",
        ],
        ["ungban <reply/username/userid>", "Membatalkan Global Banned."],
        ["listgban", "Menampilkan List Global Banned."],
    ],
)
add_command_help(
    "google",
    [
        [
            "google",
            "Featch Details on Google.",
        ],
    ],
)
add_command_help(
    "heroku",
    [
        ["setvar", "Untuk mengatur variabel config userbot."],
        ["delvar", "Untuk menghapus variabel config userbot."],
        ["getvar", "Untuk melihat variabel config userbot."],
        [
            f"usage atau {cmd}dyno",
            "Untuk mengecheck kouta dyno heroku.",
        ],
        [
            "uasu",
            "Fake Usage Kouta Dyno Heroku jadi 1000jam Untuk menipu temanmu wkwk.",
        ],
    ],
)
add_command_help(
    "invite",
    [
        [
            "invitelink",
            "Untuk Mendapatkan Link invite ke grup Obrolan Anda. [Need Admin]",
        ],
        ["invite @username", "Untuk Mengundang Anggota ke grup Anda."],
        [
            "inviteall @usernamegc",
            "Untuk Mengundang Anggota dari obrolan grup lain ke obrolan grup Anda.",
        ],
    ],
)


add_command_help(
    "joinleave",
    [
        [
            "exit",
            "Keluar dari grup dengan menampilkan pesan has left this group, bye!!.",
        ],
        ["exitsgc", "Keluar dari semua grup telegram yang anda gabung."],
        ["exitsch", "Keluar dari semua channel telegram yang anda gabung."],
        ["join <UsernameGC>", "Untuk Bergabung dengan Obrolan Melalui username."],
        ["leave <UsernameGC>", "Untuk keluar dari grup Melalui username."],
    ],
)
add_command_help(
    "locks",
    [
        ["lock <all atau jenis lock>", "Mengunci izin di grup."],
        [
            "unlock <all atau jenis unlock>",
            "Membuka izin di grup\n\nSupported Locks / Unlocks:` `msg` | `media` | `stickers` | `polls` | `info`  | `invite` | `webprev` |`pin` | `all`.",
        ],
    ],
)
add_command_help(
    "log",
    [
        [
            "log",
            "Untuk mengaktifkan Log Chat dari obrolan/grup itu.",
        ],
        [
            "nolog",
            "Untuk menonaktifkan Log Chat dari obrolan/grup itu.",
        ],
        [
            "pmlog on/off",
            "Untuk mengaktifkan atau menonaktifkan log pesan pribadi yang akan di forward ke grup log.",
        ],
        [
            "gruplog on/off",
            "Untuk mengaktifkan atau menonaktifkan tag grup, yang akan masuk ke grup log.",
        ],
    ],
)
add_command_help(
    "memes",
    [
        ["trump", "make a Quote by Trump."],
        ["ctweet", "Twitte by Ur values."],
    ],
)
add_command_help(
    "mentiontag",
    [
        [
            "mention [text/reply ke chat]",
            "Untuk Mention semua member group",
        ],
        [
            "cancel",
            f"Untuk Membatalkan Perintah {cmd}tagall",
        ],
    ],
)



add_command_help(
    "tolink",
    [
        [
            "cp [link tautan]",
            "Untuk Mencuri link Channel, Yang tidak bisa di forward",
        ],
        [
            "tonime",
            f"reply Untuk Mengubah Foto Menjadi Anime, (mempunyai batas limit)",
        ],
    ],
)

add_command_help(
    "tolink",
    [
        [
            "jurus",
            f"reply foto Untuk Mengubah Foto Menjadi jelek.",
        ],
    ],
)

add_command_help(
    "misc",
    [
        ["limit", "Check Limit telegram from @SpamBot."],
        ["duck", "Untuk mendapatkan Link dari DuckDuckGo."],
        [
            "open",
            "Untuk melihat isi File menjadi text yang dikirim menjadi pesan telegram.",
        ],
    ],
)

add_command_help(
    "openai",
    [
        [f"ask [question]", "to ask questions using the API."],
    ],
)


add_command_help(
    "webshot",
    [
        [
            f"webshot <link> `atau` {cmd}ss <link>",
            "Untuk Mengscreenshot halaman web yang diberikan.",
        ],
    ],
)


add_command_help(
    "sosmed",
    [
        [
            f"ig <link> & {cmd}pint <link>",
            "Untuk Mendownload Media Dari Instagram & Pinteres",
        ],
        [    f"sosmed <link>",
            "Untuk Mendownload Media Dari Tiktok / facebook / twitter",
        ],
    ],
)
add_command_help(
    "speedtest",
    [
        ["dc", "Untuk melihat DC Telegram anda."],
        [
            f"speedtest `atau` {cmd}speed",
            "Untuk megetes Kecepatan Server anda.",
        ],
    ],
)


add_command_help(
    "ping",
    [
        ["ping or pink", "Untuk Menunjukkan Ping Bot Anda."],
    ],
)

add_command_help(
    "alip",
    [
        ["botme", "untuk menampilkan dekorasi gajelas😂."],
        ["setalivelogo", "Untuk Mengubah Text Alive."],
    ],
)
add_command_help(
    "pmpermit",
    [
        [
            f"ok atau {cmd}setuju",
            "Menerima pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm",
        ],
        [
            f"tolak atau {cmd}nopm",
            "Menolak pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm",
        ],
        [
            "pmlimit <angka>",
            "Untuk mengcustom pesan limit auto block pesan",
        ],
        [
            "setpmpermit <balas ke pesan>",
            "Untuk mengcustom pesan PMPERMIT untuk orang yang pesannya belum diterima.",
        ],
        [
            "getpmpermit",
            "Untuk melihat pesan PMPERMIT.",
        ],
        [
            "resetpmpermit",
            "Untuk Mereset Pesan PMPERMIT menjadi DEFAULT",
        ],
        [
            "pmpermit on/off",
            "Untuk mengaktifkan atau menonaktifkan PMPERMIT",
        ],
    ],
)
add_command_help(
    "profile",
    [
        ["block", "Untuk memblokir pengguna telegram"],
        ["unblock", "Untuk membuka pengguna yang anda blokir"],
        ["setname", "Untuk Mengganti Nama Telegram."],
        ["setbio", "Untuk Mengganti Bio Telegram."],
        [
            "setpfp",
            f"Balas Ke Gambar Ketik {cmd}setpfp Untuk Mengganti Foto Profil Telegram.",
        ],
        ["vpfp", "Untuk melihat foto profile pengguna saat ini."],
    ],
)
add_command_help(
    "purge",
    [
        ["del", "Menghapus pesan, balas ke pesan."],
        ["purge", "Menghapus pesan, balas ke pesan."],
        ["purgeme <angka>", "Menghapus jumlah pesan anda, yang mau anda hapus."],
    ],
)
add_command_help(
    "quotly",
    [
        [
            f"q atau {cmd}quotly",
            "Membuat pesan menjadi sticker dengan random background.",
        ],
        [
            f"q <warna> atau {cmd}quotly <warna>",
            "Membuat pesan menjadi sticker dengan custom warna background yang diberikan.",
        ],
    ],
)
add_command_help(
    "vctools",
    [
        ["startvc", "Untuk Memulai voice chat group."],
        ["stopvc", "Untuk Memberhentikan voice chat group."],
        [
            f"jvc atau {cmd}jvc <chatid/username gc>",
            "Untuk Bergabung ke voice chat group.",
        ],
        [
            f"lvc atau {cmd}lvc <chatid/username gc>",
            "Untuk Turun dari voice chat group.",
        ],
    ],
)
add_command_help(
    "song",
    [
        ["song", "Mendownload Musik dari Youtube."],
        ["deezer", "Mendownload musik dari deezer."],
    ],
)

add_command_help(
    "saavn",
    [
            ["saavn", "Download From Saavn"],
    ],
)
add_command_help(
    "video",
    [
        [
            "video",
            "Download Video from YouTube ",
        ]
    ],
)
add_command_help(
    "salam",
    [
        ["p", "Assalamualaikum."],
        ["pe", "Assalamualaikum Warahmatullahi Wabarakatuh."],
        ["l", "Wa'alaikumsalam."],
        ["ass", "Assalamualaikum Bahas arab."],
        ["oi", "Salam Kenal dan salam."],
        ["l", "Wa'alaikumsalam."],
        ["el", "Wa'alaikumsalam Warahmatullahi Wabarakatuh."],
    ],
)

add_command_help(
    "sfs",
    [
        ["sfs", "Subs for Subs Channel."],
        ["mutu", "Mutualan Ig cuyyyy,"],
    ],
)
add_command_help(
    "sangmata",
    [
        [
            f"sm <reply/userid/username>",
            "Untuk Mendapatkan Riwayat Nama Pengguna selama di telegram.",
        ],
    ],
)
add_command_help(
    "spam",
    [
        ["spam <jumlah spam> <text>", "Mengirim teks secara spam dalam obrolan!!"],
        [
            "delayspam <detik> <jumlah spam> <text>",
            "Mengirim teks spam dengan jangka delay yang ditentukan!",
        ],
        ["sspam <jumlah spam>", "Mengirim Spam Sticker, Wajib Reply Sticker!!!"],
    ],
)
add_command_help(
    "start",
    [
        ["alive", "Mencoba Apakah Bot dalam keadaan menyala atau mati."],
        ["repo", "Memunculkan Repo."],
        ["getstring", "Untuk Mengambil String."],
        ["id", "Balas Pesan Seseorang dan dapatkan Id nya."],
        [f"up `or` {cmd}uptime", "Check bot's current uptime."],
    ],
)
add_command_help(
    "stats",
    [
        ["stats", "Untuk Cek Status Akun Anda."],
    ],
)
add_command_help(
    "sticker",
    [
        [
            f"kang `atau` {cmd}tikel",
            f"Balas {cmd}kang Ke Sticker Atau Gambar Untuk Menambahkan Ke Sticker Pack.",
        ],
        [
            f"kang [emoji] `atau` {cmd}tikel [emoji]",
            f"Untuk Menambahkan dan costum emoji sticker Ke Sticker Pack Mu.\n\n`  •  **NOTE:** Untuk Membuat Sticker Pack baru Gunakan angka dibelakang {cmd}kang\n  •  **CONTOH:** {cmd}kang 2 untuk membuat dan menyimpan ke sticker pack ke 2`",
        ],
        [
            f"packinfo `atau` {cmd}stickerinfo",
            "Untuk Mendapatkan Informasi Sticker Pack.",
        ],
        ["get", "Balas ke sticker untuk mendapatkan foto sticker."],
        ["stickers <nama sticker>", "Untuk Mencari Sticker Pack."],
    ],
)


add_command_help(
    "memify",
    [
        [
            "mmf Teks Atas ; Teks Bawah",
            "Balas Ke Pesan Sticker atau Foto akan Di ubah menjadi sticker teks meme yang di tentukan.",
        ],
    ],
)


add_command_help(
    "tiny",
    [
        [
            "tiny <reply ke foto/sticker>",
            "Untuk Mengubah Sticker Menjadi Kecil.",
        ],
    ],
)
add_command_help(
    "system",
    [
        ["restart", "Untuk merestart userbot."],
        ["shutdown", "Untuk mematikan userbot."],
        ["logs", "Untuk melihat logs userbot."],
    ],
)
add_command_help(
    "telegraph",
    [
        ["tm", "Reply foto/video untuk menjadikan link telegraph."],
    ],
)
add_command_help(
    "toxic",
    [
        ["jamet", "Menghina Jamet telegram"],
        ["pp", "Menghina Jamet telegram yang ga pake foto profil."],
        ["dp", "Menghina Jamet muka hina!"],
        ["so", "Ngeledek orang sokab."],
        ["nb", "Ngeledek orang norak baru pake bot."],
        ["skb", "Ngeledek orang sokab versi 2."],
        ["met", "Ngeledek si jamet caper."],
        ["war", "Ngeledek orang so keras ngajak war."],
        ["wartai", "Ngeledek orang so ketrigger ngajak cod minta sharelok."],
        ["kismin", "Ngeledek orang kismin so jagoan di tele."],
        ["ded", "Nyuruh orang mati aja goblok wkwk."],
        ["sokab", "Ngeledek orang so kenal so dekat padahal kga kenal goblok."],
        ["gembel", "Ngeledek bapaknya si jamet."],
        ["cuih", "Ngeludahin keluarganya satu satu wkwk."],
        ["dih", "Ngeledek anak haram."],
        ["gcs", "Ngeledek gc sampah."],
    ],
)

add_command_help(
    "fglobal",
    [
        ["gbn", "Global Banned Secara fake."],
        ["gmt", "Global Mute secara fake."],
    ],
)
add_command_help(
    "translate",
    [
        [
            "tr <kode bahasa> <text/reply>",
            "Menerjemahkan teks ke bahasa yang disetel. (Default kode bahasa indonesia)",
        ],
    ],
)
add_command_help(
    "update",
    [
        ["apdet", "Untuk melihat list pembaruan terbaru dari RamPyro-Bot."],
        ["apdet dulu", "Untuk mengupdate userbot."],
    ],
)

add_command_help(
    "voice",
    [
        [f"voice atau {cmd}tts [text/reply]", "Ubah teks menjadi suara oleh google."],
        [
            f"{cmd}voicelang (lang_id) ",
            "Setel bahasa suara anda\n\nBeberapa Bahasa Suara yang Tersedia:"
            "\nID| Language  | ID| Language\n"
            "af: Afrikaans | ar: Arabic\n"
            "cs: Czech     | de: German\n"
            "el: Greek     | en: English\n"
            "es: Spanish   | fr: French\n"
            "hi: Hindi     | id: Indonesian\n"
            "is: Icelandic | it: Italian\n"
            "ja: Japanese  | jw: Javanese\n"
            "ko: Korean    | la: Latin\n"
            "my: Myanmar   | ne: Nepali\n"
            "nl: Dutch     | pt: Portuguese\n"
            "ru: Russian   | su: Sundanese\n"
            "sv: Swedish   | th: Thai\n"
            "tl: Filipino  | tr: Turkish\n"
            "vi: Vietname  |\n"
            "zh-cn: Chinese (Mandarin/China)\n"
            "zh-tw: Chinese (Mandarin/Taiwan)",
        ],
    ],
)
