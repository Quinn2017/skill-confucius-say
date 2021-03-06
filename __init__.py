# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util import wait_while_speaking

from mycroft.util.log import getLogger
LOGGER = getLogger(__name__)

__author__ = 'aussieW'

class ConfuciusSkill(MycroftSkill):
    def __init__(self):
        super(ConfuciusSkill, self).__init__(name="ConfuciusSkill")

    @intent_handler(IntentBuilder('handle_saying').require('confucius').require('say'))
    def handle_saying(self, message):
        LOGGER.info('ConfuciusSkill: Quoting Confucius')
        self.speak('Confucius say')
        wait_while_speaking()
        self.speak_dialog('sayings')

    @intent_handler(IntentBuilder('handle_funny_saying').require('funny').require('confucius').require('say'))
    def handle_funny_saying(self, message):
        LOGGER.info('ConfuciusSkill: Funny Confucius saying')
        self.speak('Confucius say')
        wait_while_speaking()
        self.speak_dialog('funny_sayings')

    def stop(self):
        pass

def create_skill():
    return ConfuciusSkill()
