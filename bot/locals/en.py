from bot.locals import Local

LOCAL = Local({
    'WRONG_ROOM' : 'I a\'m not suppose to be here.\nID : <code>{CHAT_ID}</code>',
    'WELCOME_MESSAGE' : "හායි 😍❤️\nමම <b>කූඩැල්ලා</b>!\nPowered by @Ravindu_Deshanz\nගෲපට එන්න අපේ 😌: <a href='t.me/Ravindu_mirror'>Mirror.Ravindu</a>",
    'PASS_REQUIRED' : '\n\n<code>/{cmd_pass} </code>කියලා ගහලා පාස්වඩ් එක ගහන්න බොටාට ඇක්සස් කරන්න 🥰.',
    'LEECH_LIST_MESSAGE_HEADER' : '<b>Leech Status</b>',
    'LEECH_LIST_FORMAT' : 'නම: <code>{name}</code>\nStatus: {status}\nID: <code>{gid}</code>\n\n',
    'ARIA2_CHECKING_LINK' : "පරීක්ෂා කරමින් 😍❤️...",
    'ARIA2_DOWNLOAD_STATUS' : "බාන ගමන් ඉන්නෙ උබට 🥰 : <code>{name}</code>\n{block} {percentage}\nSize : {total_size}\nDN : {download_speed} / UP : {upload_speed}\nSeeder : {seeder}\nETA : {eta}\nID : <code>{gid}</code>",
    'ARIA2_DOWNLOAD_SUCCESS' : 'බඩු බෑවා 😂❤️ : <code>{name}</code>',
    'ARIA2_DOWNLOAD_CANCELED' : 'ඩව්ලෝඩ් වෙන එක නතර කරා 🥺 : <code>{name}</code>',
    'ARIA2_DEAD_LINK' : 'Download auto canceled : <code>{name}</code>\nYour Torrent/Link is Dead.',
    'ARIA2_NO_URI' : 'Link is invalid.',
    'UPLOADING_FILE' : 'අප්ලෝඩ් කරමින් 😊 : <code>{name}</code>',
    'UPLOADING_PROGRESS' : 'අප්ලෝඩ් වෙනවෝ 🥰 : <code>{name}</code>\n{block} {percentage}%\nසයිස් එක ❤️ : {size}\nUP : {upload_speed}/s\nETA : {eta}',
    'UPLOAD_FAILED_FILE_MISSING' : 'Upload : Failed. file not found.\n<code>{name}</code>',
    'GENERATE_THUMBNAIL' : 'Thumbnail : Generating.\n<code>{name}</code>',
    'SPLIT_FILE' : 'ඔයාගේ ෆයිල් එක 2GB වලට වැඩි හින්දා ඒක කඩන්න වෙනවා කෑලි වලට 🥺💔 : <code>{name}</code>',
    'SPLIT_FAILED' : 'Split : Failed.\n<code>{name}</code>',
    'THUMBNAIL_NO_PHOTO' : 'Set <code>/{cmd_set_thumbnail}</code> as your photo caption.',
    'THUMBNAIL_DOWNLOADING' : 'ෆයිල් එකට අදාළ පසුබිම් ෆොටෝ එක බාන ගමන් 😍.',
    'THUMBNAIL_DOWNLOADED' : 'ෆයිල් එකට අදාළ පසුබිම් ෆොටෝ එක බෑවා 😊',
    'THUMBNAIL_APPLIED' : 'පසුබිම් පොටෝව දැම්මා ❤️',
    'THUMBNAIL_DELETING' : 'Deleting thumbnail.',
    'THUMBNAIL_RESET' : 'Thumbnail reset.',
    'UPLOAD_AS_DOC' : 'Upload as document set to {status}.',
    'UPLOAD_AS_ZIP' : 'Upload as zip file set to {status}.',
    'TRACKER_RESET' : 'Default torrent tracker reset.',
    'TRACKER_APPLIED' : 'Default torrent tracker applied.',
    'HELP_MESSAGE_HEADER' : '<b>Bot Command</b>',
    'NO_HELP_INFO' : 'no information',
    'COMMAND_START' : 'start bot',
    'COMMAND_PASSWORD' : 'enter password that required',
    'COMMAND_HELP' : 'this message',
    'COMMAND_LEECH' : 'leech link or magnet',
    'COMMAND_CANCEL_LEECH' : 'cancel leeching',
    'COMMAND_LEECH_LIST' : 'list on going leech',
    'COMMAND_SET_THUMBNAIL' : 'set custom video thumbail',
    'COMMAND_RESET_THUMBNAIL' : 'reset custom video thumbnail',
    'COMMAND_UPLOAD_AS_DOC' : 'toggle upload anything as document',
    'COMMAND_UPLOAD_AS_ZIP' : 'toggle upload anything as bundled zipfile',
    'COMMAND_SET_TRACKER' : 'set default tracker, sparated by newline',
    'BLOCK_EMPTY' : "▒",
    "BLOCK_FILLED" : "▉"
})
