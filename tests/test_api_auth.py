import pytest
from fastapi import HTTPException
from d4k_ms_service.api_auth import get_api_key
from d4k_ms_base import ServiceEnvironment
from unittest.mock import patch

@pytest.mark.asyncio
async def test_get_api_key_valid():
    # Mock the ServiceEnvironment to return a known API key
    with patch.object(ServiceEnvironment, 'get', return_value='test_api_key'):
        # Test with valid API key
        result = await get_api_key('test_api_key')
        assert result == 'test_api_key'

@pytest.mark.asyncio
async def test_get_api_key_invalid():
    # Mock the ServiceEnvironment to return a known API key
    with patch.object(ServiceEnvironment, 'get', return_value='correct_api_key'):
        # Test with invalid API key
        with pytest.raises(HTTPException) as exc_info:
            await get_api_key('wrong_api_key')
        
        assert exc_info.value.status_code == 403
        assert exc_info.value.detail == "Could not validate API KEY" 