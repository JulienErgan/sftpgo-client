from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.recovery_code import RecoveryCode
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/admin/2fa/recoverycodes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, List[RecoveryCode]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RecoveryCode.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, List[RecoveryCode]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, List[RecoveryCode]]]:
    """Get recovery codes

     Returns the recovery codes for the logged in admin. Recovery codes can be used if the admin loses
    access to their second factor auth device. Recovery codes are returned unencrypted

    Returns:
        Response[Union[Any, List[RecoveryCode]]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, List[RecoveryCode]]]:
    """Get recovery codes

     Returns the recovery codes for the logged in admin. Recovery codes can be used if the admin loses
    access to their second factor auth device. Recovery codes are returned unencrypted

    Returns:
        Response[Union[Any, List[RecoveryCode]]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, List[RecoveryCode]]]:
    """Get recovery codes

     Returns the recovery codes for the logged in admin. Recovery codes can be used if the admin loses
    access to their second factor auth device. Recovery codes are returned unencrypted

    Returns:
        Response[Union[Any, List[RecoveryCode]]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, List[RecoveryCode]]]:
    """Get recovery codes

     Returns the recovery codes for the logged in admin. Recovery codes can be used if the admin loses
    access to their second factor auth device. Recovery codes are returned unencrypted

    Returns:
        Response[Union[Any, List[RecoveryCode]]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
