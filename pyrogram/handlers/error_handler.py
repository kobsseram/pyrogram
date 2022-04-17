#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from .handler import Handler
from typing import Callable

import pyrogram
from pyrogram.types import Update


class ErrorHandler(Handler):
    """The Exception handler class. Used to handle error in handlers.
    It is intended to be used with :meth:`~pyrogram.Client.add_handler`
    Parameters:
        callback (``callable``):
            Pass a function that will be called when a new Exception arrives. It takes *(client, error)*
            as positional arguments (look at the section below for a detailed description).
        errors (``Exception``, "Tuple[``Exception``]"):
            Pass a error class(es) which the handler will react to. Dont use if global.
    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself, useful when you want to call other API methods inside the message handler.
        error (:obj:`Exception`):
            The received error.
    """

    # TODO ⬇️
    """For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_error` decorator."""

    def __init__(self, callback: Callable, errors=None):
        self.callback = callback
        self.errors = tuple(errors) if isinstance(errors, list) else errors
    
    async def check(self, client: "pyrogram.Client", update: Update):
        return True
