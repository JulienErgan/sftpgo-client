from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
from ...models.transfer_quota_usage import TransferQuotaUsage
from ...models.user_transfer_quota_update_usage_mode import (
    UserTransferQuotaUpdateUsageMode,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    client: Client,
    json_body: TransferQuotaUsage,
    mode: Union[Unset, None, UserTransferQuotaUpdateUsageMode] = UNSET,
) -> Dict[str, Any]:
    url = "{}/quotas/users/{username}/transfer-usage".format(
        client.base_url, username=username
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_mode: Union[Unset, None, str] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value if mode else None

    params["mode"] = json_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ApiResponse]]:
    if response.status_code == 200:
        response_200 = ApiResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ApiResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Client,
    json_body: TransferQuotaUsage,
    mode: Union[Unset, None, UserTransferQuotaUpdateUsageMode] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Update transfer quota usage limits

     Sets the current used transfer quota limits for the given user

    Args:
        username (str):
        mode (Union[Unset, None, UserTransferQuotaUpdateUsageMode]): Update type:
                * `add` - add the specified quota limits to the current used ones
                * `reset` - reset the values to the specified ones. This is the default
             Example: reset.
        json_body (TransferQuotaUsage):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        json_body=json_body,
        mode=mode,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    username: str,
    *,
    client: Client,
    json_body: TransferQuotaUsage,
    mode: Union[Unset, None, UserTransferQuotaUpdateUsageMode] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Update transfer quota usage limits

     Sets the current used transfer quota limits for the given user

    Args:
        username (str):
        mode (Union[Unset, None, UserTransferQuotaUpdateUsageMode]): Update type:
                * `add` - add the specified quota limits to the current used ones
                * `reset` - reset the values to the specified ones. This is the default
             Example: reset.
        json_body (TransferQuotaUsage):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return sync_detailed(
        username=username,
        client=client,
        json_body=json_body,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Client,
    json_body: TransferQuotaUsage,
    mode: Union[Unset, None, UserTransferQuotaUpdateUsageMode] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Update transfer quota usage limits

     Sets the current used transfer quota limits for the given user

    Args:
        username (str):
        mode (Union[Unset, None, UserTransferQuotaUpdateUsageMode]): Update type:
                * `add` - add the specified quota limits to the current used ones
                * `reset` - reset the values to the specified ones. This is the default
             Example: reset.
        json_body (TransferQuotaUsage):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        json_body=json_body,
        mode=mode,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    username: str,
    *,
    client: Client,
    json_body: TransferQuotaUsage,
    mode: Union[Unset, None, UserTransferQuotaUpdateUsageMode] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Update transfer quota usage limits

     Sets the current used transfer quota limits for the given user

    Args:
        username (str):
        mode (Union[Unset, None, UserTransferQuotaUpdateUsageMode]): Update type:
                * `add` - add the specified quota limits to the current used ones
                * `reset` - reset the values to the specified ones. This is the default
             Example: reset.
        json_body (TransferQuotaUsage):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            json_body=json_body,
            mode=mode,
        )
    ).parsed
