# Kernel interfaces used by LinuxKPI consumers, v6.15 … v6.18

Provider symbols imported, per consumer group (parents include their children).

| group | v6.15 | v6.16 | v6.17 | v6.18 |
|---|---|---|---|---|
| **all** | 1441 | 1448 | 1469 | 1485 |
| drm | 1017 | 1022 | 1043 | 1056 |
| &nbsp;&nbsp;drm/core | 360 | 358 | 365 | 368 |
| &nbsp;&nbsp;drm/ttm | 127 | 127 | 127 | 127 |
| &nbsp;&nbsp;drm/sched | 90 | 90 | 90 | 92 |
| &nbsp;&nbsp;drm/amdgpu | 524 | 531 | 534 | 539 |
| &nbsp;&nbsp;drm/radeon | 274 | 272 | 272 | 273 |
| &nbsp;&nbsp;drm/i915 | 678 | 678 | 684 | 686 |
| &nbsp;&nbsp;drm/xe | 510 | 517 | 541 | 540 |
| wifi | 728 | 731 | 731 | 736 |
| &nbsp;&nbsp;wifi/iwlwifi | 380 | 379 | 375 | 376 |
| &nbsp;&nbsp;wifi/mt76 | 337 | 337 | 337 | 340 |
| &nbsp;&nbsp;wifi/rtw88 | 186 | 186 | 189 | 189 |
| &nbsp;&nbsp;wifi/rtw89 | 210 | 213 | 221 | 224 |
| &nbsp;&nbsp;wifi/ath | 16 | 16 | 16 | 16 |
| &nbsp;&nbsp;wifi/ath10k | 232 | 232 | 232 | 232 |
| &nbsp;&nbsp;wifi/ath11k | 265 | 269 | 270 | 270 |
| &nbsp;&nbsp;wifi/ath12k | 247 | 252 | 254 | 255 |
| &nbsp;&nbsp;wifi/brcm80211 | 216 | 217 | 217 | 217 |

## v6.15 → v6.16

[full report](diff-v6.15..v6.16/report.md)

| group | used | newly used | no longer used | renames | declaration changed | changed types | hdr: newly used | hdr: no longer used | hdr: renames | hdr: signature changed |
|---|---|---|---|---|---|---|---|---|---|---|
| **all** | 1448 | 15 | 8 | 1 | 6 | 73 | 53 | 10 | 1 | 2 |
| [drm](diff-v6.15..v6.16/groups/drm.md) | 1022 | 11 | 6 | 1 | 6 | 60 | 29 | 4 | 1 | 2 |
| &nbsp;&nbsp;[drm/core](diff-v6.15..v6.16/groups/drm-core.md) | 358 | 0 | 2 | 1 | 2 | 56 | 1 | 0 | 1 | 0 |
| &nbsp;&nbsp;[drm/ttm](diff-v6.15..v6.16/groups/drm-ttm.md) | 127 | 1 | 1 | 0 | 2 | 53 | 1 | 0 | 0 | 0 |
| &nbsp;&nbsp;[drm/sched](diff-v6.15..v6.16/groups/drm-sched.md) | 90 | 0 | 0 | 1 | 0 | 52 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[drm/amdgpu](diff-v6.15..v6.16/groups/drm-amdgpu.md) | 531 | 5 | 1 | 1 | 4 | 60 | 11 | 1 | 1 | 0 |
| &nbsp;&nbsp;[drm/radeon](diff-v6.15..v6.16/groups/drm-radeon.md) | 272 | 0 | 2 | 1 | 1 | 56 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[drm/i915](diff-v6.15..v6.16/groups/drm-i915.md) | 678 | 6 | 4 | 1 | 6 | 59 | 13 | 2 | 1 | 1 |
| &nbsp;&nbsp;[drm/xe](diff-v6.15..v6.16/groups/drm-xe.md) | 517 | 0 | 2 | 1 | 4 | 58 | 15 | 1 | 0 | 2 |
| [wifi](diff-v6.15..v6.16/groups/wifi.md) | 731 | 4 | 3 | 1 | 2 | 68 | 25 | 6 | 1 | 1 |
| &nbsp;&nbsp;[wifi/iwlwifi](diff-v6.15..v6.16/groups/wifi-iwlwifi.md) | 379 | 0 | 1 | 1 | 1 | 60 | 4 | 5 | 1 | 1 |
| &nbsp;&nbsp;[wifi/mt76](diff-v6.15..v6.16/groups/wifi-mt76.md) | 337 | 0 | 0 | 1 | 2 | 58 | 0 | 0 | 1 | 0 |
| &nbsp;&nbsp;[wifi/rtw88](diff-v6.15..v6.16/groups/wifi-rtw88.md) | 186 | 0 | 0 | 1 | 1 | 58 | 1 | 0 | 1 | 0 |
| &nbsp;&nbsp;[wifi/rtw89](diff-v6.15..v6.16/groups/wifi-rtw89.md) | 213 | 0 | 0 | 1 | 1 | 58 | 4 | 0 | 0 | 1 |
| &nbsp;&nbsp;[wifi/ath](diff-v6.15..v6.16/groups/wifi-ath.md) | 16 | 0 | 0 | 0 | 0 | 53 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/ath10k](diff-v6.15..v6.16/groups/wifi-ath10k.md) | 232 | 0 | 0 | 1 | 1 | 58 | 0 | 0 | 1 | 0 |
| &nbsp;&nbsp;[wifi/ath11k](diff-v6.15..v6.16/groups/wifi-ath11k.md) | 269 | 2 | 2 | 1 | 1 | 63 | 4 | 1 | 1 | 0 |
| &nbsp;&nbsp;[wifi/ath12k](diff-v6.15..v6.16/groups/wifi-ath12k.md) | 252 | 3 | 2 | 1 | 1 | 63 | 11 | 1 | 1 | 0 |
| &nbsp;&nbsp;[wifi/brcm80211](diff-v6.15..v6.16/groups/wifi-brcm80211.md) | 217 | 1 | 0 | 1 | 1 | 58 | 4 | 0 | 1 | 0 |

## v6.16 → v6.17

[full report](diff-v6.16..v6.17/report.md)

| group | used | newly used | no longer used | renames | declaration changed | changed types | hdr: newly used | hdr: no longer used | hdr: renames | hdr: signature changed |
|---|---|---|---|---|---|---|---|---|---|---|
| **all** | 1469 | 27 | 6 | 1 | 7 | 93 | 52 | 16 | 1 | 4 |
| [drm](diff-v6.16..v6.17/groups/drm.md) | 1043 | 23 | 1 | 1 | 5 | 70 | 38 | 5 | 1 | 4 |
| &nbsp;&nbsp;[drm/core](diff-v6.16..v6.17/groups/drm-core.md) | 365 | 3 | 0 | 1 | 2 | 60 | 1 | 0 | 0 | 1 |
| &nbsp;&nbsp;[drm/ttm](diff-v6.16..v6.17/groups/drm-ttm.md) | 127 | 0 | 0 | 1 | 1 | 53 | 2 | 0 | 0 | 0 |
| &nbsp;&nbsp;[drm/sched](diff-v6.16..v6.17/groups/drm-sched.md) | 90 | 0 | 0 | 1 | 0 | 50 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[drm/amdgpu](diff-v6.16..v6.17/groups/drm-amdgpu.md) | 534 | 3 | 1 | 1 | 1 | 65 | 2 | 1 | 0 | 1 |
| &nbsp;&nbsp;[drm/radeon](diff-v6.16..v6.17/groups/drm-radeon.md) | 272 | 0 | 0 | 1 | 1 | 57 | 1 | 0 | 0 | 1 |
| &nbsp;&nbsp;[drm/i915](diff-v6.16..v6.17/groups/drm-i915.md) | 684 | 5 | 0 | 1 | 4 | 68 | 14 | 4 | 1 | 3 |
| &nbsp;&nbsp;[drm/xe](diff-v6.16..v6.17/groups/drm-xe.md) | 541 | 15 | 1 | 1 | 1 | 66 | 22 | 0 | 0 | 3 |
| [wifi](diff-v6.16..v6.17/groups/wifi.md) | 731 | 4 | 5 | 1 | 3 | 82 | 15 | 11 | 0 | 1 |
| &nbsp;&nbsp;[wifi/iwlwifi](diff-v6.16..v6.17/groups/wifi-iwlwifi.md) | 375 | 1 | 5 | 1 | 2 | 65 | 2 | 11 | 0 | 1 |
| &nbsp;&nbsp;[wifi/mt76](diff-v6.16..v6.17/groups/wifi-mt76.md) | 337 | 0 | 0 | 1 | 1 | 65 | 1 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/rtw88](diff-v6.16..v6.17/groups/wifi-rtw88.md) | 189 | 2 | 0 | 1 | 0 | 60 | 1 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/rtw89](diff-v6.16..v6.17/groups/wifi-rtw89.md) | 221 | 3 | 0 | 1 | 1 | 61 | 2 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/ath](diff-v6.16..v6.17/groups/wifi-ath.md) | 16 | 0 | 0 | 0 | 0 | 52 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/ath10k](diff-v6.16..v6.17/groups/wifi-ath10k.md) | 232 | 1 | 1 | 1 | 0 | 63 | 0 | 1 | 0 | 1 |
| &nbsp;&nbsp;[wifi/ath11k](diff-v6.16..v6.17/groups/wifi-ath11k.md) | 270 | 0 | 0 | 1 | 0 | 62 | 2 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/ath12k](diff-v6.16..v6.17/groups/wifi-ath12k.md) | 254 | 0 | 0 | 1 | 0 | 61 | 10 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/brcm80211](diff-v6.16..v6.17/groups/wifi-brcm80211.md) | 217 | 0 | 0 | 1 | 1 | 67 | 1 | 0 | 0 | 0 |

## v6.17 → v6.18

[full report](diff-v6.17..v6.18/report.md)

| group | used | newly used | no longer used | renames | declaration changed | changed types | hdr: newly used | hdr: no longer used | hdr: renames | hdr: signature changed |
|---|---|---|---|---|---|---|---|---|---|---|
| **all** | 1485 | 18 | 2 | 0 | 7 | 89 | 41 | 18 | 0 | 15 |
| [drm](diff-v6.17..v6.18/groups/drm.md) | 1056 | 15 | 2 | 0 | 7 | 64 | 35 | 7 | 0 | 14 |
| &nbsp;&nbsp;[drm/core](diff-v6.17..v6.18/groups/drm-core.md) | 368 | 5 | 2 | 0 | 1 | 60 | 3 | 0 | 0 | 6 |
| &nbsp;&nbsp;[drm/ttm](diff-v6.17..v6.18/groups/drm-ttm.md) | 127 | 0 | 0 | 0 | 1 | 59 | 0 | 0 | 0 | 5 |
| &nbsp;&nbsp;[drm/sched](diff-v6.17..v6.18/groups/drm-sched.md) | 92 | 1 | 0 | 0 | 0 | 59 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[drm/amdgpu](diff-v6.17..v6.18/groups/drm-amdgpu.md) | 539 | 7 | 1 | 0 | 2 | 62 | 17 | 0 | 0 | 3 |
| &nbsp;&nbsp;[drm/radeon](diff-v6.17..v6.18/groups/drm-radeon.md) | 273 | 4 | 0 | 0 | 1 | 60 | 2 | 0 | 0 | 1 |
| &nbsp;&nbsp;[drm/i915](diff-v6.17..v6.18/groups/drm-i915.md) | 686 | 4 | 1 | 0 | 3 | 64 | 7 | 2 | 0 | 11 |
| &nbsp;&nbsp;[drm/xe](diff-v6.17..v6.18/groups/drm-xe.md) | 540 | 6 | 1 | 0 | 6 | 63 | 9 | 5 | 0 | 3 |
| [wifi](diff-v6.17..v6.18/groups/wifi.md) | 736 | 5 | 1 | 0 | 1 | 85 | 6 | 11 | 0 | 2 |
| &nbsp;&nbsp;[wifi/iwlwifi](diff-v6.17..v6.18/groups/wifi-iwlwifi.md) | 376 | 2 | 1 | 0 | 0 | 78 | 1 | 11 | 0 | 1 |
| &nbsp;&nbsp;[wifi/mt76](diff-v6.17..v6.18/groups/wifi-mt76.md) | 340 | 2 | 0 | 0 | 1 | 74 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/rtw88](diff-v6.17..v6.18/groups/wifi-rtw88.md) | 189 | 0 | 0 | 0 | 0 | 74 | 0 | 0 | 0 | 2 |
| &nbsp;&nbsp;[wifi/rtw89](diff-v6.17..v6.18/groups/wifi-rtw89.md) | 224 | 1 | 0 | 0 | 0 | 74 | 0 | 0 | 0 | 2 |
| &nbsp;&nbsp;[wifi/ath](diff-v6.17..v6.18/groups/wifi-ath.md) | 16 | 0 | 0 | 0 | 0 | 61 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/ath10k](diff-v6.17..v6.18/groups/wifi-ath10k.md) | 232 | 0 | 0 | 0 | 1 | 75 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/ath11k](diff-v6.17..v6.18/groups/wifi-ath11k.md) | 270 | 1 | 0 | 0 | 0 | 74 | 1 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/ath12k](diff-v6.17..v6.18/groups/wifi-ath12k.md) | 255 | 1 | 0 | 0 | 0 | 74 | 2 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/brcm80211](diff-v6.17..v6.18/groups/wifi-brcm80211.md) | 217 | 1 | 0 | 0 | 0 | 72 | 2 | 0 | 0 | 0 |
