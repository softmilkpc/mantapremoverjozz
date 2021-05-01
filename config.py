# ForwardTagRemoverBot - A Telegram Bot To Hide Forward Source
#Copyright (C) 2020 by Rasak <https://github.com/Artis7eeR>
#ForwardTagRemoverBot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#ForwardTagRemoverBot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os

class Config:
	
 TOKEN=os.environ.get("BOT_TOKEN",None)
 SOURCE="https://t.me/mantapvids"
 START_TEXT="Henlow [{}](tg://user?id={})\nGw botnya @mantapvids Channel Berguna untuk Menghapus caption caption gaje yang dipasang sama uploader termasuk gw sendiri eh jingan juga ya.\n ketik /help biar lu tau kegunaan gw apa !\n jgn lupa join ©mantapvids @groupgratis"
 HELP_TEXT="Forward ke gw File,Video,Audio,Photo atau apapun sesuka kepala jidad kalian \n dan gw bakal ngirimin file tersebut kembali tanpa caption gaje!!\n\n`Gmn cara set caption su?`\nReply Caption ke File,Photo,Audio,Media"
	
