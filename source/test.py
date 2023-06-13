import pytest

from unittest.mock import AsyncMock

from telegram_bot import (
    handle_start,
    handle_lang,
    handle_help,
    handle_stop,
    handle_make,
    handle_reset,
    supported_conversion_formats
)

from localization import (
    supported_languages
)


@pytest.mark.asyncio
async def test_handle_start():
    user = AsyncMock(first_name = 'TestUser',id = '12345678')
    message = AsyncMock(from_user = user)
    await handle_start(message)
    message.answer.assert_called_with("Hi, dear TestUser, my name is Converty and I am file converter bot 😎\n"
                                        "Use /help command to find out what I can do\n")


@pytest.mark.asyncio
async def test_handle_stop():
    user = AsyncMock(first_name = 'TestUser')
    message = AsyncMock(from_user = user)
    await handle_stop(message)
    message.answer.assert_called_once_with("Goodbye, dear TestUser")


@pytest.mark.asyncio
async def test_handle_make_one_param():
    message=AsyncMock(text = '/make')
    await handle_make(message)
    message.answer.assert_called_with("Please specify one convertation format")


@pytest.mark.asyncio
async def test_handle_make_unsupported_format():
    message=AsyncMock(text = '/make unsupported_format')
    await handle_make(message)
    message.answer.assert_called_with(('Oops, this format is not supported yet 😔️️️\n'
                                      'Choose supported one from: {formats}').format(formats=', '.join(map(str, supported_conversion_formats))))


@pytest.mark.asyncio
async def test_handle_make_supported_format():
    message=AsyncMock(text = '/make pdf')
    await handle_make(message)
    message.answer.assert_called_with('Something went wrong, please try again later')


@pytest.mark.asyncio
async def test_handle_help():
    user = AsyncMock(first_name = 'TestUser')
    message = AsyncMock(from_user = user, text = "/help")
    await handle_help(message)
    message.answer.assert_called_with(f"Use commands:\n"
                         "/start to launch the bot\n"
                         "/stop to stop the bot\n"
                         "/make <format> to convert files into format\n"
                         "/reset to forget all uploaded files\n"
                         "/lang to change language\n"
                         "/help to see this message or\n"
                         "/help <command> to see additional information about chosen command\n")


@pytest.mark.asyncio
async def test_handle_lang_one_param():
    message = AsyncMock(text = "/lang")
    await handle_lang(message)
    message.answer.assert_called_with("Please specify one language")


@pytest.mark.asyncio
async def test_handle_lang_two_params():
    message = AsyncMock(text = "/lang ja")
    await handle_lang(message)
    message.answer.assert_called_with(("Unfortunately, this language is not supported yet 😔️️️\n"
                                      "Choose supported one from: {langs}").format(langs=', '.join(map(str, supported_languages))))


@pytest.mark.asyncio
async def test_handle_reset():
    user = AsyncMock(first_name = 'TestUser',id = '12345678')
    message = AsyncMock(from_user = user)
    await handle_reset(message)
    message.answer.assert_called_with("All uploaded files deleted")
