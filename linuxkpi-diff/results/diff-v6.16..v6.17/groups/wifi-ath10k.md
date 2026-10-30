# Interfaces used by wifi/ath10k: v6.16 → v6.17

## Symbol-level summary

| | count |
|---|---|
| interfaces used in v6.16 | 232 |
| interfaces used in v6.17 | 232 |
| likely renames | 1 |
| newly used (excluding renames) | 1 |
| no longer used (excluding renames) | 1 |
| export kind/owner/namespace changed | 0 |
| used in both, own declaration changed | 0 |
| changed types reachable from used interfaces | 63 |

## Likely renames

Dropped and newly used symbols with identical signatures (types and parameter names) and similar names.

| v6.16 | v6.17 | signature | used by |
|---|---|---|---|
| `alloc_workqueue` | `alloc_workqueue_noprof` | `struct workqueue_struct*(const char* fmt, unsigned int flags, int max_active, ?)` | amdgpu,drm_display_helper,i915,radeon,gpu-sched,ttm,xe,ath10k_core,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_core,rtw89_core |

## Newly used in v6.17

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `crc32_le` | func | vmlinux | plain | lib/crc/crc32-main.c | ath10k_core,iwlmld,iwlmvm |

## No longer used in v6.17

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `crc32_le_arch` | func | vmlinux | plain | arch/x86/lib/crc32.c | ath10k_core,iwlmld,iwlmvm |

## Interfaces whose own declaration changed

Return/parameter types, variable types, or interfaces that lost their debug info. `[C]` changed, `[D]` deleted.

None.

## Changed types

Each changed type reachable from an interface this group uses, with the number of those interfaces it reaches, fewest first: low counts are targeted changes, high counts are churn reached through hub types (reachability is transitive through pointers, so e.g. `struct device` or `struct module` pull in hundreds).

| type | declared at | change | used interfaces reached |
|---|---|---|---|
| `struct nvmem_device` | internals.h:10:1 | type size changed from 7744 to 7808 (in bits); there are data member changes | 2 |
| `struct nvmem_layout` | nvmem-provider.h:154:1 | type size changed from 5888 to 5952 (in bits); there are data member changes | 2 |
| `struct thermal_cooling_device` | thermal.h:123:1 | type size changed from 6784 to 6848 (in bits); there are data member changes | 2 |
| `enum skb_drop_reason` | dropreason-core.h:131:1 | 6 enumerator insertions; 77 enumerator changes | 3 |
| `struct pci_bus` | pci.h:652:1 | type size changed from 8192 to 8256 (in bits); there are data member changes | 15 |
| `struct pci_dev` | pci.h:332:1 | type size changed from 16704 to 16768 (in bits); 1 data member insertion; there are data member changes | 15 |
| `struct pci_sriov` | pci.h:467:1 | 1 data member insertion; there are data member changes | 15 |
| `struct ieee80211_bss_conf` | mac80211.h:762:1 | 1 data member insertion | 24 |
| `struct ieee80211_link_sta` | mac80211.h:2440:1 | type size changed from 1984 to 2112 (in bits); 1 data member insertion; there are data member changes | 24 |
| `struct ieee80211_sta` | mac80211.h:2516:1 | type size changed from 4480 to 4608 (in bits); there are data member changes | 24 |
| `struct ieee80211_vif` | mac80211.h:2034:1 | there are data member changes | 24 |
| `struct sched_dl_entity` | sched.h:635:1 | type size changed from 1984 to 1920 (in bits); 1 data member deletion; there are data member changes | 35 |
| `struct wiphy` | cfg80211.h:5703:1 | type size changed from 10496 to 10752 (in bits); 1 data member insertion; there are data member changes | 35 |
| `enum phy_interface_t` | phy.h:110:1 | 4 enumerator insertions; 1 enumerator change | 77 |
| `struct acpi_device` | acpi_bus.h:471:1 | type size changed from 11136 to 11200 (in bits); there are data member changes | 77 |
| `struct blk_integrity` | blkdev.h:116:1 | type size changed from 48 to 56 (in bits); 1 data member insertion | 77 |
| `struct bpf_xdp_link` | dev.c:9881:1 | type size changed from 704 to 768 (in bits); there are data member changes | 77 |
| `struct device_link` | device.h:707:1 | type size changed from 6592 to 6656 (in bits); there are data member changes | 77 |
| `struct devlink_port` | devlink.h:123:1 | there are data member changes | 77 |
| `struct devlink_rate` | devlink.h:102:1 | type size changed from 704 to 960 (in bits); 1 data member insertion | 77 |
| `struct fs_struct` | fs_struct.h:9:1 | 1 data member deletion; there are data member changes | 77 |
| `struct io_ring_ctx` | io_uring_types.h:237:1 | type size changed from 12288 to 11776 (in bits); 2 data member deletions; there are data member changes | 77 |
| `struct iommu_ops` | iommu.h:621:1 | 1 data member deletion; 1 data member insertion; there are data member changes | 77 |
| `struct mdio_device` | mdio.h:28:1 | type size changed from 6592 to 6656 (in bits); there are data member changes | 77 |
| `struct mii_bus` | phy.h:334:1 | type size changed from 20928 to 18944 (in bits); 1 data member deletion; there are data member changes | 77 |
| `struct mount` | mount.h:50:1 | type size changed from 2944 to 2816 (in bits); 1 data member deletion; 2 data member insertions; there are data member changes | 77 |
| `struct mountpoint` | mount.h:43:1 | type size changed from 320 to 256 (in bits); 1 data member deletion | 77 |
| `struct msi_domain_info` | msi.h:499:1 | type size changed from 640 to 704 (in bits); 1 data member insertion; there are data member changes | 77 |
| `struct per_cpu_nodestat` | mmzone.h:758:1 | type size changed from 392 to 384 (in bits); there are data member changes | 77 |
| `struct pglist_data` | mmzone.h:1356:1 | there are data member changes | 77 |
| `struct phy_device` | phy.h:606:1 | 1 data member deletion; 1 data member insertion; there are data member changes | 77 |
| `struct queue_limits` | blkdev.h:368:1 | type size changed from 1472 to 1536 (in bits); 3 data member insertions; there are data member changes | 77 |
| `struct request_queue` | blkdev.h:465:1 | type size changed from 7744 to 7808 (in bits); there are data member changes | 77 |
| `struct rq` | sched.h:1099:1 | type size changed from 26624 to 26112 (in bits); there are data member changes | 77 |
| `struct sched_entity` | sched.h:568:1 | type size hasn't changed | 77 |
| `struct task_group` | sched.h:431:1 | 1 data member insertion | 77 |
| `struct wq_device` | workqueue.c:7047:1 | type size changed from 5824 to 5888 (in bits); there are data member changes | 77 |
| `struct address_space_operations` | fs.h:438:1 | there are data member changes | 112 |
| `struct block_device` | blk_types.h:41:1 | type size changed from 7424 to 7488 (in bits); there are data member changes | 112 |
| `struct bpf_link` | bpf.h:1694:1 | type size changed from 576 to 640 (in bits); 2 data member insertions; there are data member changes | 112 |
| `struct bpf_map` | bpf.h:263:1 | 2 data member insertions; there are data member changes | 112 |
| `struct bpf_offloaded_map` | bpf.h:601:1 | there are data member changes | 112 |
| `struct bpf_prog_aux` | bpf.h:1541:1 | type size changed from 9280 to 10304 (in bits); 1 data member insertion | 112 |
| `struct cgroup_subsys` | cgroup-defs.h:735:1 | there are data member changes | 112 |
| `struct css_rstat_cpu` | cgroup-defs.h:373:1 | type size changed from 128 to 256 (in bits); 2 data member insertions | 112 |
| `struct ethtool_ops` | ethtool.h:1083:1 | type size changed from 5056 to 5184 (in bits); 2 data member insertions; there are data member changes | 112 |
| `struct ethtool_rmon_stats` | ethtool.h:559:1 | type size changed from 1600 to 1728 (in bits); there are data member changes | 112 |
| `struct file_ra_state` | fs.h:1052:1 | 1 data member insertion; there are data member changes | 112 |
| `struct inet6_dev` | if_inet6.h:167:1 | there are data member changes | 112 |
| `struct inode_operations` | fs.h:2221:1 | there are data member changes | 112 |
| `struct linux_mib` | snmp.h:104:1 | type size changed from 8640 to 8704 (in bits); there are data member changes | 112 |
| `struct mm_struct` | mm_types.h:933:1 | type size changed from 10240 to 11264 (in bits); there are data member changes | 112 |
| `struct napi_config` | netdevice.h:367:1 | 1 data member insertion; there are data member changes | 112 |
| `struct neigh_table` | neighbour.h:202:1 | type size changed from 4800 to 5056 (in bits); 1 data member insertion; there are data member changes | 112 |
| `struct net_device` | netdevice.h:2084:1 | 1 data member insertion; there are data member changes | 112 |
| `struct pid` | pid.h:55:1 | type size changed from 1088 to 1152 (in bits); 2 data member deletions; there are data member changes | 112 |
| `struct pneigh_entry` | neighbour.h:178:1 | type size changed from 256 to 384 (in bits); 2 data member insertions; there are data member changes | 112 |
| `struct request_sock_ops` | request_sock.h:28:1 | type size changed from 512 to 448 (in bits); 1 data member deletion; there are data member changes | 112 |
| `struct sock` | sock.h:351:1 | type size changed from 6080 to 6144 (in bits); 1 data member insertion; there are data member changes | 112 |
| `struct super_block` | fs.h:1325:1 | 1 data member insertion; there are data member changes | 112 |
| `struct super_operations` | fs.h:2338:1 | type size changed from 1664 to 1728 (in bits); 1 data member insertion; there are data member changes | 112 |
| `struct task_struct` | sched.h:812:1 | type size changed from 24576 to 25088 (in bits); 1 data member insertion; there are data member changes | 112 |
| `struct writeback_control` | writeback.h:43:1 | type size changed from 2624 to 2496 (in bits); 3 data member deletions; there are data member changes | 112 |

### Details

<details><summary><code>struct nvmem_device</code> (internals.h:10:1)</summary>

```
  type size changed from 7744 to 7808 (in bits)
  there are data member changes:
    type 'struct device' of 'nvmem_device::dev' changed, as reported earlier
    'list_head node' offset changed from 5824 to 5888 (in bits) (by +64 bits)
    'int stride' offset changed from 5952 to 6016 (in bits) (by +64 bits)
    'int word_size' offset changed from 5984 to 6048 (in bits) (by +64 bits)
    'int id' offset changed from 6016 to 6080 (in bits) (by +64 bits)
    'kref refcnt' offset changed from 6048 to 6112 (in bits) (by +64 bits)
    'size_t size' offset changed from 6080 to 6144 (in bits) (by +64 bits)
    'bool read_only' offset changed from 6144 to 6208 (in bits) (by +64 bits)
    'bool root_only' offset changed from 6152 to 6216 (in bits) (by +64 bits)
    'int flags' offset changed from 6176 to 6240 (in bits) (by +64 bits)
    'nvmem_type type' offset changed from 6208 to 6272 (in bits) (by +64 bits)
    'bin_attribute eeprom' offset changed from 6272 to 6336 (in bits) (by +64 bits)
    'device* base_dev' offset changed from 6976 to 7040 (in bits) (by +64 bits)
    'list_head cells' offset changed from 7040 to 7104 (in bits) (by +64 bits)
    'void (nvmem_device*, nvmem_cell_info*)* fixup_dt_cell_info' offset changed from 7168 to 7232 (in bits) (by +64 bits)
    'const nvmem_keepout* keepout' offset changed from 7232 to 7296 (in bits) (by +64 bits)
    'unsigned int nkeepout' offset changed from 7296 to 7360 (in bits) (by +64 bits)
    'nvmem_reg_read_t reg_read' offset changed from 7360 to 7424 (in bits) (by +64 bits)
    'nvmem_reg_write_t reg_write' offset changed from 7424 to 7488 (in bits) (by +64 bits)
    'gpio_desc* wp_gpio' offset changed from 7488 to 7552 (in bits) (by +64 bits)
    'nvmem_layout* layout' offset changed from 7552 to 7616 (in bits) (by +64 bits)
    'void* priv' offset changed from 7616 to 7680 (in bits) (by +64 bits)
    'bool sysfs_cells_populated' offset changed from 7680 to 7744 (in bits) (by +64 bits)
```

Reaches: `function nvmem_cell* devm_nvmem_cell_get(device*, const char*)`, `function void* nvmem_cell_read(nvmem_cell*, size_t*)`

</details>

<details><summary><code>struct nvmem_layout</code> (nvmem-provider.h:154:1)</summary>

```
  type size changed from 5888 to 5952 (in bits)
  there are data member changes:
    type 'struct device' of 'nvmem_layout::dev' changed, as reported earlier
    'nvmem_device* nvmem' offset changed from 5760 to 5824 (in bits) (by +64 bits)
    'int (nvmem_layout*)* add_cells' offset changed from 5824 to 5888 (in bits) (by +64 bits)
```

Reaches: `function nvmem_cell* devm_nvmem_cell_get(device*, const char*)`, `function void* nvmem_cell_read(nvmem_cell*, size_t*)`

</details>

<details><summary><code>struct thermal_cooling_device</code> (thermal.h:123:1)</summary>

```
  type size changed from 6784 to 6848 (in bits)
  there are data member changes:
    type 'struct device' of 'thermal_cooling_device::device' changed, as reported earlier
    'device_node* np' offset changed from 5952 to 6016 (in bits) (by +64 bits)
    'void* devdata' offset changed from 6016 to 6080 (in bits) (by +64 bits)
    'void* stats' offset changed from 6080 to 6144 (in bits) (by +64 bits)
    'const thermal_cooling_device_ops* ops' offset changed from 6144 to 6208 (in bits) (by +64 bits)
    'bool updated' offset changed from 6208 to 6272 (in bits) (by +64 bits)
    'mutex lock' offset changed from 6272 to 6336 (in bits) (by +64 bits)
    'list_head thermal_instances' offset changed from 6528 to 6592 (in bits) (by +64 bits)
    'list_head node' offset changed from 6656 to 6720 (in bits) (by +64 bits)
```

Reaches: `function thermal_cooling_device* thermal_cooling_device_register(const char*, void*, const thermal_cooling_device_ops*)`, `function void thermal_cooling_device_unregister(thermal_cooling_device*)`

</details>

<details><summary><code>enum skb_drop_reason</code> (dropreason-core.h:131:1)</summary>

```
  type size hasn't changed
  6 enumerator insertions:
    'skb_drop_reason::SKB_DROP_REASON_TCP_INVALID_END_SEQUENCE' value '43'
    'skb_drop_reason::SKB_DROP_REASON_CAN_RX_INVALID_FRAME' value '120'
    'skb_drop_reason::SKB_DROP_REASON_CANFD_RX_INVALID_FRAME' value '121'
    'skb_drop_reason::SKB_DROP_REASON_CANXL_RX_INVALID_FRAME' value '122'
    'skb_drop_reason::SKB_DROP_REASON_PFMEMALLOC' value '123'
    'skb_drop_reason::SKB_DROP_REASON_DUALPI2_STEP_DROP' value '124'
  77 enumerator changes:
    'skb_drop_reason::SKB_DROP_REASON_TCP_INVALID_ACK_SEQUENCE' from value '43' to '44' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_RESET' from value '44' to '45' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_INVALID_SYN' from value '45' to '46' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_CLOSE' from value '46' to '47' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_FASTOPEN' from value '47' to '48' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_OLD_ACK' from value '48' to '49' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_TOO_OLD_ACK' from value '49' to '50' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_ACK_UNSENT_DATA' from value '50' to '51' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE' from value '51' to '52' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_OFO_DROP' from value '52' to '53' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_IP_OUTNOROUTES' from value '53' to '54' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_BPF_CGROUP_EGRESS' from value '54' to '55' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_IPV6DISABLED' from value '55' to '56' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_NEIGH_CREATEFAIL' from value '56' to '57' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_NEIGH_FAILED' from value '57' to '58' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_NEIGH_QUEUEFULL' from value '58' to '59' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_NEIGH_DEAD' from value '59' to '60' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_NEIGH_HH_FILLFAIL' from value '60' to '61' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TC_EGRESS' from value '61' to '62' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_SECURITY_HOOK' from value '62' to '63' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_QDISC_DROP' from value '63' to '64' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_QDISC_OVERLIMIT' from value '64' to '65' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_QDISC_CONGESTED' from value '65' to '66' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_CAKE_FLOOD' from value '66' to '67' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_FQ_BAND_LIMIT' from value '67' to '68' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_FQ_HORIZON_LIMIT' from value '68' to '69' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_FQ_FLOW_LIMIT' from value '69' to '70' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_CPU_BACKLOG' from value '70' to '71' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_XDP' from value '71' to '72' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_TC_INGRESS' from value '72' to '73' at dropreason-core.h:137:1
    'skb_drop_reason::SKB_DROP_REASON_UNHANDLED_PROTO' from value '73' to '74' at dropreason-core.h:137:1
  ...
```

Reaches: `function void dev_kfree_skb_any_reason(sk_buff*, skb_drop_reason)`, `function void sk_skb_reason_drop(sock*, sk_buff*, skb_drop_reason)`, `function void skb_queue_purge_reason(sk_buff_head*, skb_drop_reason)`

</details>

<details><summary><code>struct pci_bus</code> (pci.h:652:1)</summary>

```
  type size changed from 8192 to 8256 (in bits)
  there are data member changes:
    type 'struct device' of 'pci_bus::dev' changed, as reported earlier
    'bin_attribute* legacy_io' offset changed from 8000 to 8064 (in bits) (by +64 bits)
    'bin_attribute* legacy_mem' offset changed from 8064 to 8128 (in bits) (by +64 bits)
    'unsigned int is_added' offset changed from 8128 to 8192 (in bits) (by +64 bits)
    'unsigned int unsafe_warn' offset changed from 8129 to 8193 (in bits) (by +64 bits)
    'unsigned int flit_mode' offset changed from 8130 to 8194 (in bits) (by +64 bits)
```

Reaches: `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void pci_disable_device(pci_dev*)`, `function void pci_disable_msi(pci_dev*)`, `function int pci_enable_device(pci_dev*)`, `function int pci_enable_msi(pci_dev*)`, `function void* pci_iomap(pci_dev*, int, unsigned long int)`, `function void pci_iounmap(pci_dev*, void*)`, `function int pci_read_config_dword(const pci_dev*, int, u32*)`, `function void pci_release_region(pci_dev*, int)`, `function int pci_request_region(pci_dev*, int, const char*)`, `function void pci_set_master(pci_dev*)`, `function void pci_unregister_driver(pci_driver*)`, `function int pci_write_config_dword(const pci_dev*, int, u32)`, `function int pcie_capability_clear_and_set_word_locked(pci_dev*, int, u16, u16)`, `function int pcie_capability_read_word(pci_dev*, int, u16*)`

</details>

<details><summary><code>struct pci_dev</code> (pci.h:332:1)</summary>

```
  type size changed from 16704 to 16768 (in bits)
  1 data member insertion:
    'unsigned int is_pciehp', at offset 13594 (in bits) at pci.h:459:1
  there are data member changes:
    type 'struct device' of 'pci_dev::dev' changed, as reported earlier
    'int cfg_size' offset changed from 7296 to 7360 (in bits) (by +64 bits)
    'unsigned int irq' offset changed from 7328 to 7392 (in bits) (by +64 bits)
    'resource resource[11]' offset changed from 7360 to 7424 (in bits) (by +64 bits)
    'resource driver_exclusive_resource' offset changed from 12992 to 13056 (in bits) (by +64 bits)
    'unsigned int transparent' offset changed from 13504 to 13568 (in bits) (by +64 bits)
    'unsigned int io_window' offset changed from 13505 to 13569 (in bits) (by +64 bits)
    'unsigned int pref_window' offset changed from 13506 to 13570 (in bits) (by +64 bits)
    'unsigned int pref_64_window' offset changed from 13507 to 13571 (in bits) (by +64 bits)
    'unsigned int multifunction' offset changed from 13508 to 13572 (in bits) (by +64 bits)
    'unsigned int is_busmaster' offset changed from 13509 to 13573 (in bits) (by +64 bits)
    'unsigned int no_msi' offset changed from 13510 to 13574 (in bits) (by +64 bits)
    'unsigned int no_64bit_msi' offset changed from 13511 to 13575 (in bits) (by +64 bits)
    'unsigned int block_cfg_access' offset changed from 13512 to 13576 (in bits) (by +64 bits)
    'unsigned int broken_parity_status' offset changed from 13513 to 13577 (in bits) (by +64 bits)
    'unsigned int irq_reroute_variant' offset changed from 13514 to 13578 (in bits) (by +64 bits)
    'unsigned int msi_enabled' offset changed from 13516 to 13580 (in bits) (by +64 bits)
    'unsigned int msix_enabled' offset changed from 13517 to 13581 (in bits) (by +64 bits)
    'unsigned int ari_enabled' offset changed from 13518 to 13582 (in bits) (by +64 bits)
    'unsigned int ats_enabled' offset changed from 13519 to 13583 (in bits) (by +64 bits)
    'unsigned int pasid_enabled' offset changed from 13520 to 13584 (in bits) (by +64 bits)
    'unsigned int pri_enabled' offset changed from 13521 to 13585 (in bits) (by +64 bits)
    'unsigned int tph_enabled' offset changed from 13522 to 13586 (in bits) (by +64 bits)
    'unsigned int is_managed' offset changed from 13523 to 13587 (in bits) (by +64 bits)
    'unsigned int is_msi_managed' offset changed from 13524 to 13588 (in bits) (by +64 bits)
    'unsigned int needs_freset' offset changed from 13525 to 13589 (in bits) (by +64 bits)
    'unsigned int state_saved' offset changed from 13526 to 13590 (in bits) (by +64 bits)
    'unsigned int is_physfn' offset changed from 13527 to 13591 (in bits) (by +64 bits)
    'unsigned int is_virtfn' offset changed from 13528 to 13592 (in bits) (by +64 bits)
    'unsigned int is_hotplug_bridge' offset changed from 13529 to 13593 (in bits) (by +64 bits)
    'unsigned int shpc_managed' offset changed from 13530 to 13595 (in bits) (by +65 bits)
    'unsigned int is_thunderbolt' offset changed from 13531 to 13596 (in bits) (by +65 bits)
    'unsigned int untrusted' offset changed from 13532 to 13597 (in bits) (by +65 bits)
    'unsigned int external_facing' offset changed from 13533 to 13598 (in bits) (by +65 bits)
    'unsigned int broken_intx_masking' offset changed from 13534 to 13599 (in bits) (by +65 bits)
    'unsigned int io_window_1k' offset changed from 13535 to 13600 (in bits) (by +65 bits)
  ...
```

Reaches: `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void pci_disable_device(pci_dev*)`, `function void pci_disable_msi(pci_dev*)`, `function int pci_enable_device(pci_dev*)`, `function int pci_enable_msi(pci_dev*)`, `function void* pci_iomap(pci_dev*, int, unsigned long int)`, `function void pci_iounmap(pci_dev*, void*)`, `function int pci_read_config_dword(const pci_dev*, int, u32*)`, `function void pci_release_region(pci_dev*, int)`, `function int pci_request_region(pci_dev*, int, const char*)`, `function void pci_set_master(pci_dev*)`, `function void pci_unregister_driver(pci_driver*)`, `function int pci_write_config_dword(const pci_dev*, int, u32)`, `function int pcie_capability_clear_and_set_word_locked(pci_dev*, int, u16, u16)`, `function int pcie_capability_read_word(pci_dev*, int, u16*)`

</details>

<details><summary><code>struct pci_sriov</code> (pci.h:467:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u16 vf_rebar_cap', at offset 960 (in bits) at pci.h:492:1
  there are data member changes:
    'bool drivers_autoprobe' offset changed from 960 to 976 (in bits) (by +16 bits)
```

Reaches: `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void pci_disable_device(pci_dev*)`, `function void pci_disable_msi(pci_dev*)`, `function int pci_enable_device(pci_dev*)`, `function int pci_enable_msi(pci_dev*)`, `function void* pci_iomap(pci_dev*, int, unsigned long int)`, `function void pci_iounmap(pci_dev*, void*)`, `function int pci_read_config_dword(const pci_dev*, int, u32*)`, `function void pci_release_region(pci_dev*, int)`, `function int pci_request_region(pci_dev*, int, const char*)`, `function void pci_set_master(pci_dev*)`, `function void pci_unregister_driver(pci_driver*)`, `function int pci_write_config_dword(const pci_dev*, int, u32)`, `function int pcie_capability_clear_and_set_word_locked(pci_dev*, int, u16, u16)`, `function int pcie_capability_read_word(pci_dev*, int, u16*)`

</details>

<details><summary><code>struct ieee80211_bss_conf</code> (mac80211.h:762:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u8 s1g_long_beacon_period', at offset 7072 (in bits) at mac80211.h:863:1
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta(ieee80211_vif*, const u8*)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_hw_restart_disconnect(ieee80211_vif*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_manage_rx_ba_offl(ieee80211_vif*, const u8*, unsigned int)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)` … (+9 more)

</details>

<details><summary><code>struct ieee80211_link_sta</code> (mac80211.h:2440:1)</summary>

```
  type size changed from 1984 to 2112 (in bits)
  1 data member insertion:
    'ieee80211_sta_s1g_cap s1g_cap', at offset 1552 (in bits) at mac80211.h:2458:1
  there are data member changes:
    'ieee80211_sta_aggregates agg' offset changed from 1552 to 1680 (in bits) (by +128 bits)
    'u8 rx_nss' offset changed from 1840 to 1968 (in bits) (by +128 bits)
    'ieee80211_sta_rx_bandwidth bandwidth' offset changed from 1856 to 1984 (in bits) (by +128 bits)
    'ieee80211_sta_txpwr txpwr' offset changed from 1888 to 2016 (in bits) (by +128 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta(ieee80211_vif*, const u8*)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_hw_restart_disconnect(ieee80211_vif*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_manage_rx_ba_offl(ieee80211_vif*, const u8*, unsigned int)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)` … (+9 more)

</details>

<details><summary><code>struct ieee80211_sta</code> (mac80211.h:2516:1)</summary>

```
  type size changed from 4480 to 4608 (in bits)
  there are data member changes:
    type 'struct ieee80211_link_sta' of 'ieee80211_sta::deflink' changed, as reported earlier
    'ieee80211_link_sta* link[15]' offset changed from 3520 to 3648 (in bits) (by +128 bits)
    'u8 drv_priv[]' offset changed from 4480 to 4608 (in bits) (by +128 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta(ieee80211_vif*, const u8*)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_hw_restart_disconnect(ieee80211_vif*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_manage_rx_ba_offl(ieee80211_vif*, const u8*, unsigned int)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)` … (+9 more)

</details>

<details><summary><code>struct ieee80211_vif</code> (mac80211.h:2034:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct ieee80211_bss_conf' of 'ieee80211_vif::bss_conf' changed, as reported earlier
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta(ieee80211_vif*, const u8*)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_hw_restart_disconnect(ieee80211_vif*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_manage_rx_ba_offl(ieee80211_vif*, const u8*, unsigned int)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)` … (+9 more)

</details>

<details><summary><code>struct sched_dl_entity</code> (sched.h:635:1)</summary>

```
  type size changed from 1984 to 1920 (in bits)
  1 data member deletion:
    'dl_server_has_tasks_f server_has_tasks', at offset 1792 (in bits) at sched.h:730:1
  there are data member changes:
    type 'typedef dl_server_pick_f' of 'sched_dl_entity::server_pick_task' changed:
      underlying type 'task_struct* (sched_dl_entity*)*' changed:
    and offset changed from 1856 to 1792 (in bits) (by -64 bits)
    'sched_dl_entity* pi_se' offset changed from 1920 to 1856 (in bits) (by -64 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+20 more)

</details>

<details><summary><code>struct wiphy</code> (cfg80211.h:5703:1)</summary>

```
  type size changed from 10496 to 10752 (in bits)
  1 data member insertion:
    'wiphy_radio_cfg* radio_cfg', at offset 2944 (in bits) at cfg80211.h:5937:1
  there are data member changes:
    'const ieee80211_regdomain* regd' offset changed from 2944 to 3008 (in bits) (by +64 bits)
    type 'struct device' of 'wiphy::dev' changed, as reported earlier
    and offset changed from 3008 to 3072 (in bits) (by +64 bits)
    'bool registered' offset changed from 8768 to 8896 (in bits) (by +128 bits)
    'dentry* debugfsdir' offset changed from 8832 to 8960 (in bits) (by +128 bits)
    'const ieee80211_ht_cap* ht_capa_mod_mask' offset changed from 8896 to 9024 (in bits) (by +128 bits)
    'const ieee80211_vht_cap* vht_capa_mod_mask' offset changed from 8960 to 9088 (in bits) (by +128 bits)
    'list_head wdev_list' offset changed from 9024 to 9152 (in bits) (by +128 bits)
    type 'typedef possible_net_t' of 'wiphy::_net' changed:
      underlying type 'struct possible_net_t' at net_namespace.h:393:1 changed:
    and offset changed from 9152 to 9280 (in bits) (by +128 bits)
    'const wiphy_coalesce_support* coalesce' offset changed from 9216 to 9344 (in bits) (by +128 bits)
    'const wiphy_vendor_command* vendor_commands' offset changed from 9280 to 9408 (in bits) (by +128 bits)
    'const nl80211_vendor_cmd_info* vendor_events' offset changed from 9344 to 9472 (in bits) (by +128 bits)
    'int n_vendor_commands' offset changed from 9408 to 9536 (in bits) (by +128 bits)
    'int n_vendor_events' offset changed from 9440 to 9568 (in bits) (by +128 bits)
    'u16 max_ap_assoc_sta' offset changed from 9472 to 9600 (in bits) (by +128 bits)
    'u8 max_num_csa_counters' offset changed from 9488 to 9616 (in bits) (by +128 bits)
    'u32 bss_select_support' offset changed from 9504 to 9632 (in bits) (by +128 bits)
    'u8 nan_supported_bands' offset changed from 9536 to 9664 (in bits) (by +128 bits)
    'u32 txq_limit' offset changed from 9568 to 9696 (in bits) (by +128 bits)
    'u32 txq_memory_limit' offset changed from 9600 to 9728 (in bits) (by +128 bits)
    'u32 txq_quantum' offset changed from 9632 to 9760 (in bits) (by +128 bits)
    'unsigned long int tx_queue_len' offset changed from 9664 to 9792 (in bits) (by +128 bits)
    'u8 support_mbssid' offset changed from 9728 to 9856 (in bits) (by +128 bits)
    'u8 support_only_he_mbssid' offset changed from 9729 to 9857 (in bits) (by +128 bits)
    'const cfg80211_pmsr_capabilities* pmsr_capa' offset changed from 9792 to 9920 (in bits) (by +128 bits)
    'struct {u64 peer; u64 vif; u8 max_retry;} tid_config_support' offset changed from 9856 to 9984 (in bits) (by +128 bits)
    'u8 max_data_retry_count' offset changed from 10048 to 10176 (in bits) (by +128 bits)
    'const cfg80211_sar_capa* sar_capa' offset changed from 10112 to 10240 (in bits) (by +128 bits)
    'rfkill* rfkill' offset changed from 10176 to 10304 (in bits) (by +128 bits)
    'u8 mbssid_max_interfaces' offset changed from 10240 to 10368 (in bits) (by +128 bits)
    'u8 ema_max_profile_periodicity' offset changed from 10248 to 10376 (in bits) (by +128 bits)
    'u16 max_num_akm_suites' offset changed from 10256 to 10384 (in bits) (by +128 bits)
    'u16 hw_timestamp_max_peers' offset changed from 10272 to 10400 (in bits) (by +128 bits)
    'int n_radio' offset changed from 10304 to 10432 (in bits) (by +128 bits)
  ...
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+20 more)

</details>

<details><summary><code>enum phy_interface_t</code> (phy.h:110:1)</summary>

```
  type size hasn't changed
  4 enumerator insertions:
    'phy_interface_t::PHY_INTERFACE_MODE_50GBASER' value '34'
    'phy_interface_t::PHY_INTERFACE_MODE_LAUI' value '35'
    'phy_interface_t::PHY_INTERFACE_MODE_100GBASEP' value '36'
    'phy_interface_t::PHY_INTERFACE_MODE_MIILITE' value '37'
  1 enumerator change:
    'phy_interface_t::PHY_INTERFACE_MODE_MAX' from value '34' to '38' at phy.h:114:1
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct acpi_device</code> (acpi_bus.h:471:1)</summary>

```
  type size changed from 11136 to 11200 (in bits)
  there are data member changes:
    type 'struct device' of 'acpi_device::dev' changed:
      type size changed from 5760 to 5824 (in bits)
      there are data member changes:
        type 'struct dev_pm_info' of 'device::power' changed:
          type size changed from 2496 to 2560 (in bits)
          2 data member insertions:
            'bool strict_midlayer', at offset 583 (in bits) at pm.h:687:1
            'bool detach_power_off', at offset 2496 (in bits) at pm.h:725:1
        'dev_pm_domain* pm_domain' offset changed from 4224 to 4288 (in bits) (by +64 bits)
        'dev_msi_info msi' offset changed from 4288 to 4352 (in bits) (by +64 bits)
        'u64* dma_mask' offset changed from 4416 to 4480 (in bits) (by +64 bits)
        'u64 coherent_dma_mask' offset changed from 4480 to 4544 (in bits) (by +64 bits)
        'u64 bus_dma_limit' offset changed from 4544 to 4608 (in bits) (by +64 bits)
        'const bus_dma_region* dma_range_map' offset changed from 4608 to 4672 (in bits) (by +64 bits)
        'device_dma_parameters* dma_parms' offset changed from 4672 to 4736 (in bits) (by +64 bits)
        'list_head dma_pools' offset changed from 4736 to 4800 (in bits) (by +64 bits)
        'io_tlb_mem* dma_io_tlb_mem' offset changed from 4864 to 4928 (in bits) (by +64 bits)
        'dev_archdata archdata' offset changed from 4928 to 4992 (in bits) (by +64 bits)
        'device_node* of_node' offset changed from 4928 to 4992 (in bits) (by +64 bits)
        'fwnode_handle* fwnode' offset changed from 4992 to 5056 (in bits) (by +64 bits)
        'int numa_node' offset changed from 5056 to 5120 (in bits) (by +64 bits)
        'dev_t devt' offset changed from 5088 to 5152 (in bits) (by +64 bits)
        'u32 id' offset changed from 5120 to 5184 (in bits) (by +64 bits)
        'spinlock_t devres_lock' offset changed from 5152 to 5216 (in bits) (by +64 bits)
        'list_head devres_head' offset changed from 5184 to 5248 (in bits) (by +64 bits)
        'const class* class' offset changed from 5312 to 5376 (in bits) (by +64 bits)
        'const attribute_group** groups' offset changed from 5376 to 5440 (in bits) (by +64 bits)
        'void (device*)* release' offset changed from 5440 to 5504 (in bits) (by +64 bits)
        'iommu_group* iommu_group' offset changed from 5504 to 5568 (in bits) (by +64 bits)
        'dev_iommu* iommu' offset changed from 5568 to 5632 (in bits) (by +64 bits)
        'device_physical_location* physical_location' offset changed from 5632 to 5696 (in bits) (by +64 bits)
        'device_removable removable' offset changed from 5696 to 5760 (in bits) (by +64 bits)
        'bool offline_disabled' offset changed from 5728 to 5792 (in bits) (by +64 bits)
        'bool offline' offset changed from 5729 to 5793 (in bits) (by +64 bits)
        'bool of_node_reused' offset changed from 5730 to 5794 (in bits) (by +64 bits)
        'bool state_synced' offset changed from 5731 to 5795 (in bits) (by +64 bits)
        'bool can_match' offset changed from 5732 to 5796 (in bits) (by +64 bits)
        'bool dma_skip_sync' offset changed from 5733 to 5797 (in bits) (by +64 bits)
  ...
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct blk_integrity</code> (blkdev.h:116:1)</summary>

```
  type size changed from 48 to 56 (in bits)
  1 data member insertion:
    'unsigned char pi_tuple_size', at offset 48 (in bits) at blkdev.h:123:1
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct bpf_xdp_link</code> (dev.c:9881:1)</summary>

```
  type size changed from 704 to 768 (in bits)
  there are data member changes:
    type 'struct bpf_link' of 'bpf_xdp_link::link' changed, as reported earlier
    'net_device* dev' offset changed from 576 to 640 (in bits) (by +64 bits)
    'int flags' offset changed from 640 to 704 (in bits) (by +64 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct device_link</code> (device.h:707:1)</summary>

```
  type size changed from 6592 to 6656 (in bits)
  there are data member changes:
    type 'struct device' of 'device_link::link_dev' changed, as reported earlier
    'device_link_state status' offset changed from 6144 to 6208 (in bits) (by +64 bits)
    'u32 flags' offset changed from 6176 to 6240 (in bits) (by +64 bits)
    'refcount_t rpm_active' offset changed from 6208 to 6272 (in bits) (by +64 bits)
    'kref kref' offset changed from 6240 to 6304 (in bits) (by +64 bits)
    'work_struct rm_work' offset changed from 6272 to 6336 (in bits) (by +64 bits)
    'bool supplier_preactivated' offset changed from 6528 to 6592 (in bits) (by +64 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct devlink_port</code> (devlink.h:123:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct devlink_port_attrs' of 'devlink_port::attrs' changed:
      type size hasn't changed
      1 data member insertion:
        'u8 no_phys_port_name', at offset 2 (in bits) at devlink.h:94:1
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct devlink_rate</code> (devlink.h:102:1)</summary>

```
  type size changed from 704 to 960 (in bits)
  1 data member insertion:
    'u32 tc_bw[8]', at offset 704 (in bits) at devlink.h:126:1
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct fs_struct</code> (fs_struct.h:9:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'spinlock_t lock', at offset 32 (in bits) at fs_struct.h:11:1
  there are data member changes:
    type 'typedef seqcount_spinlock_t' of 'fs_struct::seq' changed:
      typedef name changed from seqcount_spinlock_t to seqlock_t at seqlock_types.h:91:1
      underlying type 'struct seqcount_spinlock' at seqlock_types.h:69:1 changed:
        type name changed from 'seqcount_spinlock' to 'seqlock_t'
        type size changed from 32 to 64 (in bits)
        1 data member insertion:
          'spinlock_t lock', at offset 32 (in bits) at seqlock_types.h:90:1
        there are data member changes:
          type 'typedef seqcount_t' of 'seqcount_spinlock::seqcount' changed:
            typedef name changed from seqcount_t to seqcount_spinlock_t at seqlock_types.h:69:1
            underlying type 'struct seqcount' at seqlock_types.h:33:1 changed:
              type name changed from 'seqcount' to 'seqcount_spinlock'
              type size hasn't changed
              there are data member changes:
                type 'unsigned int' of 'seqcount::sequence' changed:
                  entity changed from 'unsigned int' to 'typedef seqcount_t' at seqlock_types.h:38:1
                  type size hasn't changed
                and name of 'seqcount::sequence' changed to 'seqcount_spinlock::seqcount' at seqlock_types.h:69:1
          and name of 'seqcount_spinlock::seqcount' changed to 'seqlock_t::seqcount' at seqlock_types.h:89:1
    and offset changed from 64 to 32 (in bits) (by -32 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct io_ring_ctx</code> (io_uring_types.h:237:1)</summary>

```
  type size changed from 12288 to 11776 (in bits)
  2 data member deletions:
    'io_alloc_cache msg_cache', at offset 9344 (in bits) at io_uring_types.h:421:1
    'spinlock_t msg_lock', at offset 9536 (in bits) at io_uring_types.h:422:1
  there are data member changes:
    'list_head napi_list' offset changed from 9600 to 9344 (in bits) (by -256 bits)
    'spinlock_t napi_lock' offset changed from 9728 to 9472 (in bits) (by -256 bits)
    'ktime_t napi_busy_poll_dt' offset changed from 9792 to 9536 (in bits) (by -256 bits)
    'bool napi_prefer_busy_poll' offset changed from 9856 to 9600 (in bits) (by -256 bits)
    'u8 napi_track_mode' offset changed from 9864 to 9608 (in bits) (by -256 bits)
    'hlist_head napi_ht[16]' offset changed from 9920 to 9664 (in bits) (by -256 bits)
    'unsigned int evfd_last_cq_tail' offset changed from 10944 to 10688 (in bits) (by -256 bits)
    'unsigned int nr_req_allocated' offset changed from 10976 to 10720 (in bits) (by -256 bits)
    'mutex mmap_lock' offset changed from 11008 to 10752 (in bits) (by -256 bits)
    'io_mapped_region sq_region' offset changed from 11264 to 11008 (in bits) (by -256 bits)
    'io_mapped_region ring_region' offset changed from 11456 to 11200 (in bits) (by -256 bits)
    'io_mapped_region param_region' offset changed from 11648 to 11392 (in bits) (by -256 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct iommu_ops</code> (iommu.h:621:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'unsigned long int pgsize_bitmap', at offset 1152 (in bits) at iommu.h:662:1
  1 data member insertion:
    'int (iommufd_viommu*, iommu_domain*, const iommu_user_data*)* viommu_init', at offset 1088 (in bits) at iommu.h:702:1
  there are data member changes:
    type 'iommufd_viommu* (device*, iommu_domain*, iommufd_ctx*, unsigned int)*' of 'iommu_ops::viommu_alloc' changed:
      pointer type changed from: 'iommufd_viommu* (device*, iommu_domain*, iommufd_ctx*, unsigned int)*' to: 'typedef size_t (device*, enum iommu_viommu_type)*'
    and name of 'iommu_ops::viommu_alloc' changed to 'iommu_ops::get_viommu_size' at iommu.h:700:1
    type 'void* (device*, u32*, u32*)*' of 'iommu_ops::hw_info' changed:
      pointer type changed from: 'void* (device*, u32*, u32*)*' to: 'void* (device*, u32*, iommu_hw_info_type*)*'
    'const iommu_domain_ops* default_domain_ops' offset changed from 1088 to 1152 (in bits) (by +64 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct mdio_device</code> (mdio.h:28:1)</summary>

```
  type size changed from 6592 to 6656 (in bits)
  there are data member changes:
    type 'struct device' of 'mdio_device::dev' changed, as reported earlier
    'mii_bus* bus' offset changed from 5760 to 5824 (in bits) (by +64 bits)
    'char modalias[32]' offset changed from 5824 to 5888 (in bits) (by +64 bits)
    'int (device*, const device_driver*)* bus_match' offset changed from 6080 to 6144 (in bits) (by +64 bits)
    'void (mdio_device*)* device_free' offset changed from 6144 to 6208 (in bits) (by +64 bits)
    'void (mdio_device*)* device_remove' offset changed from 6208 to 6272 (in bits) (by +64 bits)
    'int addr' offset changed from 6272 to 6336 (in bits) (by +64 bits)
    'int flags' offset changed from 6304 to 6368 (in bits) (by +64 bits)
    'int reset_state' offset changed from 6336 to 6400 (in bits) (by +64 bits)
    'gpio_desc* reset_gpio' offset changed from 6400 to 6464 (in bits) (by +64 bits)
    'reset_control* reset_ctrl' offset changed from 6464 to 6528 (in bits) (by +64 bits)
    'unsigned int reset_assert_delay' offset changed from 6528 to 6592 (in bits) (by +64 bits)
    'unsigned int reset_deassert_delay' offset changed from 6560 to 6624 (in bits) (by +64 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct mii_bus</code> (phy.h:334:1)</summary>

```
  type size changed from 20928 to 18944 (in bits)
  1 data member deletion:
    'phy_package_shared* shared[32]', at offset 18880 (in bits) at phy.h:399:1
  there are data member changes:
    type 'struct device' of 'mii_bus::dev' changed, as reported earlier
    'mdio_device* mdio_map[32]' offset changed from 15360 to 15424 (in bits) (by +64 bits)
    'u32 phy_mask' offset changed from 17408 to 17472 (in bits) (by +64 bits)
    'u32 phy_ignore_ta_mask' offset changed from 17440 to 17504 (in bits) (by +64 bits)
    'int irq[32]' offset changed from 17472 to 17536 (in bits) (by +64 bits)
    'int reset_delay_us' offset changed from 18496 to 18560 (in bits) (by +64 bits)
    'int reset_post_delay_us' offset changed from 18528 to 18592 (in bits) (by +64 bits)
    'gpio_desc* reset_gpiod' offset changed from 18560 to 18624 (in bits) (by +64 bits)
    'mutex shared_lock' offset changed from 18624 to 18688 (in bits) (by +64 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct mount</code> (mount.h:50:1)</summary>

```
  type size changed from 2944 to 2816 (in bits)
  1 data member deletion:
    'list_head mnt_umounting', at offset 2176 (in bits) at mount.h:82:1
  2 data member insertions:
    'int mnt_t_flags', at offset 2432 (in bits) at mount.h:87:1
    'mount* overmount', at offset 2752 (in bits) at mount.h:94:1
  there are data member changes:
    type 'struct list_head' of 'mount::mnt_slave_list' changed:
      type name changed from 'list_head' to 'hlist_head'
      type size changed from 128 to 64 (in bits)
      1 data member deletion:
        'list_head* prev', at offset 64 (in bits) at types.h:200:1
      there are data member changes:
        type 'list_head*' of 'list_head::next' changed:
          pointer type changed from: 'list_head*' to: 'hlist_node*'
        and name of 'list_head::next' changed to 'hlist_head::first' at types.h:204:1
    type 'struct list_head' of 'mount::mnt_slave' changed:
      type name changed from 'list_head' to 'hlist_node'
      type size hasn't changed
      there are data member changes:
        type 'list_head*' of 'list_head::prev' changed:
          pointer type changed from: 'list_head*' to: 'hlist_node**'
        and name of 'list_head::prev' changed to 'hlist_node::pprev' at types.h:208:1
        type 'list_head*' of 'list_head::next' changed:
          pointer type changed from: 'list_head*' to: 'hlist_node*'
        and name of 'list_head::next' changed to 'hlist_node::next' at types.h:208:1
    and offset changed from 1728 to 1664 (in bits) (by -64 bits)
    'mount* mnt_master' offset changed from 1856 to 1792 (in bits) (by -64 bits)
    'mnt_namespace* mnt_ns' offset changed from 1920 to 1856 (in bits) (by -64 bits)
    'mountpoint* mnt_mp' offset changed from 1984 to 1920 (in bits) (by -64 bits)
    anonymous data member 'union {hlist_node mnt_mp_list; hlist_node mnt_umount;}' offset changed from 2048 to 1984 (in bits) (by -64 bits)
    'fsnotify_mark_connector* mnt_fsnotify_marks' offset changed from 2304 to 2112 (in bits) (by -192 bits)
    '__u32 mnt_fsnotify_mask' offset changed from 2368 to 2176 (in bits) (by -192 bits)
    'list_head to_notify' offset changed from 2432 to 2240 (in bits) (by -192 bits)
    'mnt_namespace* prev_ns' offset changed from 2560 to 2368 (in bits) (by -192 bits)
    'int mnt_id' offset changed from 2624 to 2464 (in bits) (by -160 bits)
    'u64 mnt_id_unique' offset changed from 2688 to 2496 (in bits) (by -192 bits)
    'int mnt_group_id' offset changed from 2752 to 2560 (in bits) (by -192 bits)
    'int mnt_expiry_mark' offset changed from 2784 to 2592 (in bits) (by -192 bits)
    'hlist_head mnt_pins' offset changed from 2816 to 2624 (in bits) (by -192 bits)
  ...
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct mountpoint</code> (mount.h:43:1)</summary>

```
  type size changed from 320 to 256 (in bits)
  1 data member deletion:
    'int m_count', at offset 256 (in bits) at mount.h:47:1
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct msi_domain_info</code> (msi.h:499:1)</summary>

```
  type size changed from 640 to 704 (in bits)
  1 data member insertion:
    'device* dev', at offset 192 (in bits) at msi.h:505:1
  there are data member changes:
    'irq_chip* chip' offset changed from 192 to 256 (in bits) (by +64 bits)
    'void* chip_data' offset changed from 256 to 320 (in bits) (by +64 bits)
    type 'typedef irq_flow_handler_t' of 'msi_domain_info::handler' changed:
      underlying type 'void (irq_desc*)*' changed:
    and offset changed from 320 to 384 (in bits) (by +64 bits)
    'void* handler_data' offset changed from 384 to 448 (in bits) (by +64 bits)
    'const char* handler_name' offset changed from 448 to 512 (in bits) (by +64 bits)
    'msi_alloc_info_t* alloc_data' offset changed from 512 to 576 (in bits) (by +64 bits)
    'void* data' offset changed from 576 to 640 (in bits) (by +64 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct per_cpu_nodestat</code> (mmzone.h:758:1)</summary>

```
  type size changed from 392 to 384 (in bits)
  there are data member changes:
    type 's8[48]' of 'per_cpu_nodestat::vm_node_stat_diff' changed:
      type name changed from 's8[48]' to 's8[47]'
      array type size changed from 384 to 376
      array type subrange 1 changed length from 48 to 47
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct pglist_data</code> (mmzone.h:1356:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'atomic_long_t[48]' of 'pglist_data::vm_stat' changed:
      type name changed from 'atomic_long_t[48]' to 'atomic_long_t[47]'
      array type size changed from 3072 to 3008
      array type subrange 1 changed length from 48 to 47
    'memory_tier* memtier' offset changed from 112192 to 112128 (in bits) (by -64 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct phy_device</code> (phy.h:606:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'phy_package_shared* shared', at offset 9664 (in bits) at phy.h:707:1
  1 data member insertion:
    'unsigned int is_genphy_driven', at offset 7949 (in bits) at phy.h:658:1
  there are data member changes:
    type 'struct mdio_device' of 'phy_device::mdio' changed, as reported earlier
    'const phy_driver* drv' offset changed from 6592 to 6656 (in bits) (by +64 bits)
    'device_link* devlink' offset changed from 6656 to 6720 (in bits) (by +64 bits)
    'u32 phyindex' offset changed from 6720 to 6784 (in bits) (by +64 bits)
    'u32 phy_id' offset changed from 6752 to 6816 (in bits) (by +64 bits)
    'phy_c45_device_ids c45_ids' offset changed from 6784 to 6848 (in bits) (by +64 bits)
    'unsigned int is_c45' offset changed from 7872 to 7936 (in bits) (by +64 bits)
    'unsigned int is_internal' offset changed from 7873 to 7937 (in bits) (by +64 bits)
    'unsigned int is_pseudo_fixed_link' offset changed from 7874 to 7938 (in bits) (by +64 bits)
    'unsigned int is_gigabit_capable' offset changed from 7875 to 7939 (in bits) (by +64 bits)
    'unsigned int has_fixups' offset changed from 7876 to 7940 (in bits) (by +64 bits)
    'unsigned int suspended' offset changed from 7877 to 7941 (in bits) (by +64 bits)
    'unsigned int suspended_by_mdio_bus' offset changed from 7878 to 7942 (in bits) (by +64 bits)
    'unsigned int sysfs_links' offset changed from 7879 to 7943 (in bits) (by +64 bits)
    'unsigned int loopback_enabled' offset changed from 7880 to 7944 (in bits) (by +64 bits)
    'unsigned int downshifted_rate' offset changed from 7881 to 7945 (in bits) (by +64 bits)
    'unsigned int is_on_sfp_module' offset changed from 7882 to 7946 (in bits) (by +64 bits)
    'unsigned int mac_managed_pm' offset changed from 7883 to 7947 (in bits) (by +64 bits)
    'unsigned int wol_enabled' offset changed from 7884 to 7948 (in bits) (by +64 bits)
    'unsigned int autoneg' offset changed from 7885 to 7950 (in bits) (by +65 bits)
    'unsigned int link' offset changed from 7886 to 7951 (in bits) (by +65 bits)
    'unsigned int autoneg_complete' offset changed from 7887 to 7952 (in bits) (by +65 bits)
    'unsigned int interrupts' offset changed from 7888 to 7953 (in bits) (by +65 bits)
    'unsigned int irq_suspended' offset changed from 7889 to 7954 (in bits) (by +65 bits)
    'unsigned int irq_rerun' offset changed from 7890 to 7955 (in bits) (by +65 bits)
    'unsigned int default_timestamp' offset changed from 7891 to 7956 (in bits) (by +65 bits)
    'int rate_matching' offset changed from 7904 to 7968 (in bits) (by +64 bits)
    'phy_state state' offset changed from 7936 to 8000 (in bits) (by +64 bits)
    'u32 dev_flags' offset changed from 7968 to 8032 (in bits) (by +64 bits)
    type 'typedef phy_interface_t' of 'phy_device::interface' changed:
      underlying type 'enum phy_interface_t' changed at phy.h:110:1, as reported earlier
    and offset changed from 8000 to 8064 (in bits) (by +64 bits)
    'unsigned long int possible_interfaces[1]' offset changed from 8064 to 8128 (in bits) (by +64 bits)
    'int speed' offset changed from 8128 to 8192 (in bits) (by +64 bits)
  ...
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct queue_limits</code> (blkdev.h:368:1)</summary>

```
  type size changed from 1472 to 1536 (in bits)
  3 data member insertions:
    'unsigned int max_wzeroes_unmap_sectors', at offset 736 (in bits) at blkdev.h:392:1
    'unsigned int max_hw_wzeroes_unmap_sectors', at offset 768 (in bits) at blkdev.h:393:1
    'unsigned int max_user_wzeroes_unmap_sectors', at offset 800 (in bits) at blkdev.h:394:1
  there are data member changes:
    'unsigned int max_hw_zone_append_sectors' offset changed from 736 to 832 (in bits) (by +96 bits)
    'unsigned int max_zone_append_sectors' offset changed from 768 to 864 (in bits) (by +96 bits)
    'unsigned int discard_granularity' offset changed from 800 to 896 (in bits) (by +96 bits)
    'unsigned int discard_alignment' offset changed from 832 to 928 (in bits) (by +96 bits)
    'unsigned int zone_write_granularity' offset changed from 864 to 960 (in bits) (by +96 bits)
    'unsigned int atomic_write_hw_max' offset changed from 896 to 992 (in bits) (by +96 bits)
    'unsigned int atomic_write_max_sectors' offset changed from 928 to 1024 (in bits) (by +96 bits)
    'unsigned int atomic_write_hw_boundary' offset changed from 960 to 1056 (in bits) (by +96 bits)
    'unsigned int atomic_write_boundary_sectors' offset changed from 992 to 1088 (in bits) (by +96 bits)
    'unsigned int atomic_write_hw_unit_min' offset changed from 1024 to 1120 (in bits) (by +96 bits)
    'unsigned int atomic_write_unit_min' offset changed from 1056 to 1152 (in bits) (by +96 bits)
    'unsigned int atomic_write_hw_unit_max' offset changed from 1088 to 1184 (in bits) (by +96 bits)
    'unsigned int atomic_write_unit_max' offset changed from 1120 to 1216 (in bits) (by +96 bits)
    'unsigned short int max_segments' offset changed from 1152 to 1248 (in bits) (by +96 bits)
    'unsigned short int max_integrity_segments' offset changed from 1168 to 1264 (in bits) (by +96 bits)
    'unsigned short int max_discard_segments' offset changed from 1184 to 1280 (in bits) (by +96 bits)
    'unsigned short int max_write_streams' offset changed from 1200 to 1296 (in bits) (by +96 bits)
    'unsigned int write_stream_granularity' offset changed from 1216 to 1312 (in bits) (by +96 bits)
    'unsigned int max_open_zones' offset changed from 1248 to 1344 (in bits) (by +96 bits)
    'unsigned int max_active_zones' offset changed from 1280 to 1376 (in bits) (by +96 bits)
    'unsigned int dma_alignment' offset changed from 1312 to 1408 (in bits) (by +96 bits)
    'unsigned int dma_pad_mask' offset changed from 1344 to 1440 (in bits) (by +96 bits)
    type 'struct blk_integrity' of 'queue_limits::integrity' changed, as reported earlier
    and offset changed from 1376 to 1472 (in bits) (by +96 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct request_queue</code> (blkdev.h:465:1)</summary>

```
  type size changed from 7744 to 7808 (in bits)
  there are data member changes:
    type 'struct queue_limits' of 'request_queue::limits' changed, as reported earlier
    'device* dev' offset changed from 2432 to 2496 (in bits) (by +64 bits)
    'rpm_status rpm_status' offset changed from 2496 to 2560 (in bits) (by +64 bits)
    'atomic_t pm_only' offset changed from 2528 to 2592 (in bits) (by +64 bits)
    'blk_queue_stats* stats' offset changed from 2560 to 2624 (in bits) (by +64 bits)
    'rq_qos* rq_qos' offset changed from 2624 to 2688 (in bits) (by +64 bits)
    'mutex rq_qos_mutex' offset changed from 2688 to 2752 (in bits) (by +64 bits)
    'int id' offset changed from 2944 to 3008 (in bits) (by +64 bits)
    'unsigned long int nr_requests' offset changed from 3008 to 3072 (in bits) (by +64 bits)
    'timer_list timeout' offset changed from 3072 to 3136 (in bits) (by +64 bits)
    'work_struct timeout_work' offset changed from 3392 to 3456 (in bits) (by +64 bits)
    'atomic_t nr_active_requests_shared_tags' offset changed from 3648 to 3712 (in bits) (by +64 bits)
    'blk_mq_tags* sched_shared_tags' offset changed from 3712 to 3776 (in bits) (by +64 bits)
    'list_head icq_list' offset changed from 3776 to 3840 (in bits) (by +64 bits)
    'unsigned long int blkcg_pols[1]' offset changed from 3904 to 3968 (in bits) (by +64 bits)
    'blkcg_gq* root_blkg' offset changed from 3968 to 4032 (in bits) (by +64 bits)
    'list_head blkg_list' offset changed from 4032 to 4096 (in bits) (by +64 bits)
    'mutex blkcg_mutex' offset changed from 4160 to 4224 (in bits) (by +64 bits)
    'int node' offset changed from 4416 to 4480 (in bits) (by +64 bits)
    'spinlock_t requeue_lock' offset changed from 4448 to 4512 (in bits) (by +64 bits)
    'list_head requeue_list' offset changed from 4480 to 4544 (in bits) (by +64 bits)
    'delayed_work requeue_work' offset changed from 4608 to 4672 (in bits) (by +64 bits)
    'blk_trace* blk_trace' offset changed from 5312 to 5376 (in bits) (by +64 bits)
    'blk_flush_queue* fq' offset changed from 5376 to 5440 (in bits) (by +64 bits)
    'list_head flush_list' offset changed from 5440 to 5504 (in bits) (by +64 bits)
    'mutex elevator_lock' offset changed from 5568 to 5632 (in bits) (by +64 bits)
    'mutex sysfs_lock' offset changed from 5824 to 5888 (in bits) (by +64 bits)
    'mutex limits_lock' offset changed from 6080 to 6144 (in bits) (by +64 bits)
    'list_head unused_hctx_list' offset changed from 6336 to 6400 (in bits) (by +64 bits)
    'spinlock_t unused_hctx_lock' offset changed from 6464 to 6528 (in bits) (by +64 bits)
    'int mq_freeze_depth' offset changed from 6496 to 6560 (in bits) (by +64 bits)
    'callback_head callback_head' offset changed from 6528 to 6592 (in bits) (by +64 bits)
    'wait_queue_head_t mq_freeze_wq' offset changed from 6656 to 6720 (in bits) (by +64 bits)
    'mutex mq_freeze_lock' offset changed from 6848 to 6912 (in bits) (by +64 bits)
    'blk_mq_tag_set* tag_set' offset changed from 7104 to 7168 (in bits) (by +64 bits)
    'list_head tag_set_list' offset changed from 7168 to 7232 (in bits) (by +64 bits)
    'dentry* debugfs_dir' offset changed from 7296 to 7360 (in bits) (by +64 bits)
    'dentry* sched_debugfs_dir' offset changed from 7360 to 7424 (in bits) (by +64 bits)
  ...
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct rq</code> (sched.h:1099:1)</summary>

```
  type size changed from 26624 to 26112 (in bits)
  there are data member changes:
    type 'struct sched_dl_entity' of 'rq::fair_server' changed:
      type size changed from 1984 to 1920 (in bits)
      1 data member deletion:
        'dl_server_has_tasks_f server_has_tasks', at offset 1792 (in bits) at sched.h:730:1
      there are data member changes:
        type 'typedef dl_server_pick_f' of 'sched_dl_entity::server_pick_task' changed:
          underlying type 'task_struct* (sched_dl_entity*)*' changed:
        and offset changed from 1856 to 1792 (in bits) (by -64 bits)
        'sched_dl_entity* pi_se' offset changed from 1920 to 1856 (in bits) (by -64 bits)
    'list_head leaf_cfs_rq_list' offset changed from 20288 to 20224 (in bits) (by -64 bits)
    'list_head* tmp_alone_branch' offset changed from 20416 to 20352 (in bits) (by -64 bits)
    'unsigned long int nr_uninterruptible' offset changed from 20480 to 20416 (in bits) (by -64 bits)
    anonymous data member 'union {task_struct* donor; task_struct* curr;}' offset changed from 20544 to 20480 (in bits) (by -64 bits)
    'sched_dl_entity* dl_server' offset changed from 20608 to 20544 (in bits) (by -64 bits)
    'task_struct* idle' offset changed from 20672 to 20608 (in bits) (by -64 bits)
    'task_struct* stop' offset changed from 20736 to 20672 (in bits) (by -64 bits)
    'unsigned long int next_balance' offset changed from 20800 to 20736 (in bits) (by -64 bits)
    'mm_struct* prev_mm' offset changed from 20864 to 20800 (in bits) (by -64 bits)
    'unsigned int clock_update_flags' offset changed from 20928 to 20864 (in bits) (by -64 bits)
    'u64 clock' offset changed from 20992 to 20928 (in bits) (by -64 bits)
    'u64 clock_task' offset changed from 21504 to 20992 (in bits) (by -512 bits)
    'u64 clock_pelt' offset changed from 21568 to 21056 (in bits) (by -512 bits)
    'unsigned long int lost_idle_time' offset changed from 21632 to 21120 (in bits) (by -512 bits)
    'u64 clock_pelt_idle' offset changed from 21696 to 21184 (in bits) (by -512 bits)
    'u64 clock_idle' offset changed from 21760 to 21248 (in bits) (by -512 bits)
    'atomic_t nr_iowait' offset changed from 21824 to 21312 (in bits) (by -512 bits)
    'u64 last_seen_need_resched_ns' offset changed from 21888 to 21376 (in bits) (by -512 bits)
    'int ticks_without_resched' offset changed from 21952 to 21440 (in bits) (by -512 bits)
    'int membarrier_state' offset changed from 21984 to 21472 (in bits) (by -512 bits)
    'root_domain* rd' offset changed from 22016 to 21504 (in bits) (by -512 bits)
    'sched_domain* sd' offset changed from 22080 to 21568 (in bits) (by -512 bits)
    'unsigned long int cpu_capacity' offset changed from 22144 to 21632 (in bits) (by -512 bits)
    'balance_callback* balance_callback' offset changed from 22208 to 21696 (in bits) (by -512 bits)
    'unsigned char nohz_idle_balance' offset changed from 22272 to 21760 (in bits) (by -512 bits)
    'unsigned char idle_balance' offset changed from 22280 to 21768 (in bits) (by -512 bits)
    'unsigned long int misfit_task_load' offset changed from 22336 to 21824 (in bits) (by -512 bits)
    'int active_balance' offset changed from 22400 to 21888 (in bits) (by -512 bits)
    'int push_cpu' offset changed from 22432 to 21920 (in bits) (by -512 bits)
  ...
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct sched_entity</code> (sched.h:568:1)</summary>

```
  type size hasn't changed
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct task_group</code> (sched.h:431:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'scx_task_group scx', at offset 2112 (in bits) at sched.h:500:1
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct wq_device</code> (workqueue.c:7047:1)</summary>

```
  type size changed from 5824 to 5888 (in bits)
  there are data member changes:
    type 'struct device' of 'wq_device::dev' changed, as reported earlier
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ulong`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function bool cancel_delayed_work(delayed_work*)` … (+62 more)

</details>

<details><summary><code>struct address_space_operations</code> (fs.h:438:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int (file*, address_space*, typedef loff_t, unsigned int, folio**, void**)*' of 'address_space_operations::write_begin' changed:
      pointer type changed from: 'int (file*, address_space*, typedef loff_t, unsigned int, folio**, void**)*' to: 'int (const kiocb*, address_space*, typedef loff_t, unsigned int, folio**, void**)*'
    type 'int (file*, address_space*, typedef loff_t, unsigned int, unsigned int, folio*, void*)*' of 'address_space_operations::write_end' changed:
      pointer type changed from: 'int (file*, address_space*, typedef loff_t, unsigned int, unsigned int, folio*, void*)*' to: 'int (const kiocb*, address_space*, typedef loff_t, unsigned int, unsigned int, folio*, void*)*'
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct block_device</code> (blk_types.h:41:1)</summary>

```
  type size changed from 7424 to 7488 (in bits)
  there are data member changes:
    type 'struct device' of 'block_device::bd_device' changed:
      type size changed from 5760 to 5824 (in bits)
      there are data member changes:
        type 'struct dev_pm_info' of 'device::power' changed:
          type size changed from 2496 to 2560 (in bits)
          2 data member insertions:
            'bool strict_midlayer', at offset 583 (in bits) at pm.h:687:1
            'bool detach_power_off', at offset 2496 (in bits) at pm.h:725:1
        'dev_pm_domain* pm_domain' offset changed from 4224 to 4288 (in bits) (by +64 bits)
        'dev_msi_info msi' offset changed from 4288 to 4352 (in bits) (by +64 bits)
        'u64* dma_mask' offset changed from 4416 to 4480 (in bits) (by +64 bits)
        'u64 coherent_dma_mask' offset changed from 4480 to 4544 (in bits) (by +64 bits)
        'u64 bus_dma_limit' offset changed from 4544 to 4608 (in bits) (by +64 bits)
        'const bus_dma_region* dma_range_map' offset changed from 4608 to 4672 (in bits) (by +64 bits)
        'device_dma_parameters* dma_parms' offset changed from 4672 to 4736 (in bits) (by +64 bits)
        'list_head dma_pools' offset changed from 4736 to 4800 (in bits) (by +64 bits)
        'io_tlb_mem* dma_io_tlb_mem' offset changed from 4864 to 4928 (in bits) (by +64 bits)
        'dev_archdata archdata' offset changed from 4928 to 4992 (in bits) (by +64 bits)
        'device_node* of_node' offset changed from 4928 to 4992 (in bits) (by +64 bits)
        'fwnode_handle* fwnode' offset changed from 4992 to 5056 (in bits) (by +64 bits)
        'int numa_node' offset changed from 5056 to 5120 (in bits) (by +64 bits)
        'dev_t devt' offset changed from 5088 to 5152 (in bits) (by +64 bits)
        'u32 id' offset changed from 5120 to 5184 (in bits) (by +64 bits)
        'spinlock_t devres_lock' offset changed from 5152 to 5216 (in bits) (by +64 bits)
        'list_head devres_head' offset changed from 5184 to 5248 (in bits) (by +64 bits)
        'const class* class' offset changed from 5312 to 5376 (in bits) (by +64 bits)
        'const attribute_group** groups' offset changed from 5376 to 5440 (in bits) (by +64 bits)
        'void (device*)* release' offset changed from 5440 to 5504 (in bits) (by +64 bits)
        'iommu_group* iommu_group' offset changed from 5504 to 5568 (in bits) (by +64 bits)
        'dev_iommu* iommu' offset changed from 5568 to 5632 (in bits) (by +64 bits)
        'device_physical_location* physical_location' offset changed from 5632 to 5696 (in bits) (by +64 bits)
        'device_removable removable' offset changed from 5696 to 5760 (in bits) (by +64 bits)
        'bool offline_disabled' offset changed from 5728 to 5792 (in bits) (by +64 bits)
        'bool offline' offset changed from 5729 to 5793 (in bits) (by +64 bits)
        'bool of_node_reused' offset changed from 5730 to 5794 (in bits) (by +64 bits)
        'bool state_synced' offset changed from 5731 to 5795 (in bits) (by +64 bits)
        'bool can_match' offset changed from 5732 to 5796 (in bits) (by +64 bits)
        'bool dma_skip_sync' offset changed from 5733 to 5797 (in bits) (by +64 bits)
  ...
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct bpf_link</code> (bpf.h:1694:1)</summary>

```
  type size changed from 576 to 640 (in bits)
  2 data member insertions:
    'u32 flags', at offset 256 (in bits) at bpf.h:1743:1
    'bpf_attach_type attach_type', at offset 288 (in bits) at bpf.h:1744:1
  there are data member changes:
    'bool sleepable' offset changed from 256 to 576 (in bits) (by +320 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct bpf_map</code> (bpf.h:263:1)</summary>

```
  type size hasn't changed
  2 data member insertions:
    'spinlock_t owner_lock', at offset 1536 (in bits) at bpf.h:322:1
    'u64 cookie', at offset 1856 (in bits) at bpf.h:330:1
  there are data member changes:
    type 'struct {const btf_type* attach_func_proto; spinlock_t lock; bpf_prog_type type; bool jited; bool xdp_has_frags;}' of 'bpf_map::owner' changed:
      entity changed from 'struct {const btf_type* attach_func_proto; spinlock_t lock; bpf_prog_type type; bool jited; bool xdp_has_frags;}' to 'bpf_map_owner*'
      type size changed from 192 to 64 (in bits)
    and offset changed from 1536 to 1600 (in bits) (by +64 bits)
    'bool bypass_spec_v1' offset changed from 1728 to 1664 (in bits) (by -64 bits)
    'bool frozen' offset changed from 1736 to 1672 (in bits) (by -64 bits)
    'bool free_after_mult_rcu_gp' offset changed from 1744 to 1680 (in bits) (by -64 bits)
    'bool free_after_rcu_gp' offset changed from 1752 to 1688 (in bits) (by -64 bits)
    'atomic64_t sleepable_refcnt' offset changed from 1792 to 1728 (in bits) (by -64 bits)
    's64* elem_count' offset changed from 1856 to 1792 (in bits) (by -64 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct bpf_offloaded_map</code> (bpf.h:601:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct bpf_map' of 'bpf_offloaded_map::map' changed, as reported earlier
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct bpf_prog_aux</code> (bpf.h:1541:1)</summary>

```
  type size changed from 9280 to 10304 (in bits)
  1 data member insertion:
    'bpf_stream stream[2]', at offset 9280 (in bits) at bpf.h:1690:1
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct cgroup_subsys</code> (cgroup-defs.h:735:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'raw_spinlock_t*' of 'cgroup_subsys::rstat_ss_cpu_lock' changed:
      pointer type changed from: 'raw_spinlock_t*' to: 'llist_head*'
    and name of 'cgroup_subsys::rstat_ss_cpu_lock' changed to 'cgroup_subsys::lhead' at cgroup-defs.h:821:1
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct css_rstat_cpu</code> (cgroup-defs.h:373:1)</summary>

```
  type size changed from 128 to 256 (in bits)
  2 data member insertions:
    'llist_node lnode', at offset 128 (in bits) at cgroup-defs.h:382:1
    'cgroup_subsys_state* owner', at offset 192 (in bits) at cgroup-defs.h:383:1
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct ethtool_ops</code> (ethtool.h:1083:1)</summary>

```
  type size changed from 5056 to 5184 (in bits)
  2 data member insertions:
    'int (net_device*, ethtool_rxfh_fields*)* get_rxfh_fields', at offset 2688 (in bits) at ethtool.h:1170:1
    'int (net_device*, const ethtool_rxfh_fields*, netlink_ext_ack*)* set_rxfh_fields', at offset 2752 (in bits) at ethtool.h:1172:1
  there are data member changes:
    'int (net_device*, ethtool_rxfh_context*, const ethtool_rxfh_param*, netlink_ext_ack*)* create_rxfh_context' offset changed from 2688 to 2816 (in bits) (by +128 bits)
    'int (net_device*, ethtool_rxfh_context*, const ethtool_rxfh_param*, netlink_ext_ack*)* modify_rxfh_context' offset changed from 2752 to 2880 (in bits) (by +128 bits)
    'int (net_device*, ethtool_rxfh_context*, typedef u32, netlink_ext_ack*)* remove_rxfh_context' offset changed from 2816 to 2944 (in bits) (by +128 bits)
    'void (net_device*, ethtool_channels*)* get_channels' offset changed from 2880 to 3008 (in bits) (by +128 bits)
    'int (net_device*, ethtool_channels*)* set_channels' offset changed from 2944 to 3072 (in bits) (by +128 bits)
    'int (net_device*, ethtool_dump*)* get_dump_flag' offset changed from 3008 to 3136 (in bits) (by +128 bits)
    'int (net_device*, ethtool_dump*, void*)* get_dump_data' offset changed from 3072 to 3200 (in bits) (by +128 bits)
    'int (net_device*, ethtool_dump*)* set_dump' offset changed from 3136 to 3264 (in bits) (by +128 bits)
    'int (net_device*, kernel_ethtool_ts_info*)* get_ts_info' offset changed from 3200 to 3328 (in bits) (by +128 bits)
    'void (net_device*, ethtool_ts_stats*)* get_ts_stats' offset changed from 3264 to 3392 (in bits) (by +128 bits)
    'int (net_device*, ethtool_modinfo*)* get_module_info' offset changed from 3328 to 3456 (in bits) (by +128 bits)
    'int (net_device*, ethtool_eeprom*, u8*)* get_module_eeprom' offset changed from 3392 to 3520 (in bits) (by +128 bits)
    'int (net_device*, ethtool_keee*)* get_eee' offset changed from 3456 to 3584 (in bits) (by +128 bits)
    'int (net_device*, ethtool_keee*)* set_eee' offset changed from 3520 to 3648 (in bits) (by +128 bits)
    'int (net_device*, const ethtool_tunable*, void*)* get_tunable' offset changed from 3584 to 3712 (in bits) (by +128 bits)
    'int (net_device*, const ethtool_tunable*, void*)* set_tunable' offset changed from 3648 to 3776 (in bits) (by +128 bits)
    'int (net_device*, typedef u32, ethtool_coalesce*)* get_per_queue_coalesce' offset changed from 3712 to 3840 (in bits) (by +128 bits)
    'int (net_device*, typedef u32, ethtool_coalesce*)* set_per_queue_coalesce' offset changed from 3776 to 3904 (in bits) (by +128 bits)
    'int (net_device*, ethtool_link_ksettings*)* get_link_ksettings' offset changed from 3840 to 3968 (in bits) (by +128 bits)
    'int (net_device*, const ethtool_link_ksettings*)* set_link_ksettings' offset changed from 3904 to 4032 (in bits) (by +128 bits)
    'void (net_device*, ethtool_fec_stats*)* get_fec_stats' offset changed from 3968 to 4096 (in bits) (by +128 bits)
    'int (net_device*, ethtool_fecparam*)* get_fecparam' offset changed from 4032 to 4160 (in bits) (by +128 bits)
    'int (net_device*, ethtool_fecparam*)* set_fecparam' offset changed from 4096 to 4224 (in bits) (by +128 bits)
    'void (net_device*, ethtool_stats*, u64*)* get_ethtool_phy_stats' offset changed from 4160 to 4288 (in bits) (by +128 bits)
    'int (net_device*, const ethtool_tunable*, void*)* get_phy_tunable' offset changed from 4224 to 4352 (in bits) (by +128 bits)
    'int (net_device*, const ethtool_tunable*, void*)* set_phy_tunable' offset changed from 4288 to 4416 (in bits) (by +128 bits)
    'int (net_device*, const ethtool_module_eeprom*, netlink_ext_ack*)* get_module_eeprom_by_page' offset changed from 4352 to 4480 (in bits) (by +128 bits)
    'int (net_device*, const ethtool_module_eeprom*, netlink_ext_ack*)* set_module_eeprom_by_page' offset changed from 4416 to 4544 (in bits) (by +128 bits)
    'void (net_device*, ethtool_eth_phy_stats*)* get_eth_phy_stats' offset changed from 4480 to 4608 (in bits) (by +128 bits)
    'void (net_device*, ethtool_eth_mac_stats*)* get_eth_mac_stats' offset changed from 4544 to 4672 (in bits) (by +128 bits)
    'void (net_device*, ethtool_eth_ctrl_stats*)* get_eth_ctrl_stats' offset changed from 4608 to 4736 (in bits) (by +128 bits)
    'void (net_device*, ethtool_rmon_stats*, const ethtool_rmon_hist_range**)* get_rmon_stats' offset changed from 4672 to 4800 (in bits) (by +128 bits)
    'int (net_device*, ethtool_module_power_mode_params*, netlink_ext_ack*)* get_module_power_mode' offset changed from 4736 to 4864 (in bits) (by +128 bits)
    'int (net_device*, const ethtool_module_power_mode_params*, netlink_ext_ack*)* set_module_power_mode' offset changed from 4800 to 4928 (in bits) (by +128 bits)
    'int (net_device*, ethtool_mm_state*)* get_mm' offset changed from 4864 to 4992 (in bits) (by +128 bits)
  ...
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct ethtool_rmon_stats</code> (ethtool.h:559:1)</summary>

```
  type size changed from 1600 to 1728 (in bits)
  there are data member changes:
    anonymous data member at offset 64 (in bits) changed from:
      union {struct {u64 undersize_pkts; u64 oversize_pkts; u64 fragments; u64 jabbers; u64 hist[10]; u64 hist_tx[10];}; struct {u64 undersize_pkts; u64 oversize_pkts; u64 fragments; u64 jabbers; u64 hist[10]; u64 hist_tx[10];} stats;}
    to:
      union {struct {u64 undersize_pkts; u64 oversize_pkts; u64 fragments; u64 jabbers; u64 hist[11]; u64 hist_tx[11];}; struct {u64 undersize_pkts; u64 oversize_pkts; u64 fragments; u64 jabbers; u64 hist[11]; u64 hist_tx[11];} stats;}
    and size changed from 1536 to 1664 (in bits) (by +128 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct file_ra_state</code> (fs.h:1052:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'unsigned short int order', at offset 160 (in bits) at fs.h:1059:1
  there are data member changes:
    type 'unsigned int' of 'file_ra_state::mmap_miss' changed:
      type name changed from 'unsigned int' to 'unsigned short int'
      type size changed from 32 to 16 (in bits)
    and offset changed from 160 to 176 (in bits) (by +16 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct inet6_dev</code> (if_inet6.h:167:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct ipv6_devconf' of 'inet6_dev::cnf' changed:
      type size hasn't changed
      1 data member insertion:
        '__s32 force_forwarding', at offset 128 (in bits) at ipv6.h:20:1
      there are data member changes:
        '__s32 disable_policy' offset changed from 128 to 160 (in bits) (by +32 bits)
        '__s32 proxy_ndp' offset changed from 160 to 192 (in bits) (by +32 bits)
        '__u8 __cacheline_group_end__ipv6_devconf_read_txrx[]' offset changed from 192 to 224 (in bits) (by +32 bits)
        '__s32 accept_ra' offset changed from 192 to 224 (in bits) (by +32 bits)
        '__s32 accept_redirects' offset changed from 224 to 256 (in bits) (by +32 bits)
        '__s32 autoconf' offset changed from 256 to 288 (in bits) (by +32 bits)
        '__s32 dad_transmits' offset changed from 288 to 320 (in bits) (by +32 bits)
        '__s32 rtr_solicits' offset changed from 320 to 352 (in bits) (by +32 bits)
        '__s32 rtr_solicit_interval' offset changed from 352 to 384 (in bits) (by +32 bits)
        '__s32 rtr_solicit_max_interval' offset changed from 384 to 416 (in bits) (by +32 bits)
        '__s32 rtr_solicit_delay' offset changed from 416 to 448 (in bits) (by +32 bits)
        '__s32 force_mld_version' offset changed from 448 to 480 (in bits) (by +32 bits)
        '__s32 mldv1_unsolicited_report_interval' offset changed from 480 to 512 (in bits) (by +32 bits)
        '__s32 mldv2_unsolicited_report_interval' offset changed from 512 to 544 (in bits) (by +32 bits)
        '__s32 use_tempaddr' offset changed from 544 to 576 (in bits) (by +32 bits)
        '__s32 temp_valid_lft' offset changed from 576 to 608 (in bits) (by +32 bits)
        '__s32 temp_prefered_lft' offset changed from 608 to 640 (in bits) (by +32 bits)
        '__s32 regen_min_advance' offset changed from 640 to 672 (in bits) (by +32 bits)
        '__s32 regen_max_retry' offset changed from 672 to 704 (in bits) (by +32 bits)
        '__s32 max_desync_factor' offset changed from 704 to 736 (in bits) (by +32 bits)
        '__s32 max_addresses' offset changed from 736 to 768 (in bits) (by +32 bits)
        '__s32 accept_ra_defrtr' offset changed from 768 to 800 (in bits) (by +32 bits)
        '__u32 ra_defrtr_metric' offset changed from 800 to 832 (in bits) (by +32 bits)
        '__s32 accept_ra_min_hop_limit' offset changed from 832 to 864 (in bits) (by +32 bits)
        '__s32 accept_ra_min_lft' offset changed from 864 to 896 (in bits) (by +32 bits)
        '__s32 accept_ra_pinfo' offset changed from 896 to 928 (in bits) (by +32 bits)
        '__s32 ignore_routes_with_linkdown' offset changed from 928 to 960 (in bits) (by +32 bits)
        '__s32 accept_source_route' offset changed from 960 to 992 (in bits) (by +32 bits)
        '__s32 accept_ra_from_local' offset changed from 992 to 1024 (in bits) (by +32 bits)
        '__s32 drop_unicast_in_l2_multicast' offset changed from 1024 to 1056 (in bits) (by +32 bits)
        '__s32 accept_dad' offset changed from 1056 to 1088 (in bits) (by +32 bits)
        '__s32 force_tllao' offset changed from 1088 to 1120 (in bits) (by +32 bits)
        '__s32 ndisc_notify' offset changed from 1120 to 1152 (in bits) (by +32 bits)
  ...
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct inode_operations</code> (fs.h:2221:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int (mnt_idmap*, dentry*, fileattr*)*' of 'inode_operations::fileattr_set' changed:
      pointer type changed from: 'int (mnt_idmap*, dentry*, fileattr*)*' to: 'int (mnt_idmap*, dentry*, file_kattr*)*'
    type 'int (dentry*, fileattr*)*' of 'inode_operations::fileattr_get' changed:
      pointer type changed from: 'int (dentry*, fileattr*)*' to: 'int (dentry*, file_kattr*)*'
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct linux_mib</code> (snmp.h:104:1)</summary>

```
  type size changed from 8640 to 8704 (in bits)
  there are data member changes:
    type 'unsigned long int[135]' of 'linux_mib::mibs' changed:
      type name changed from 'unsigned long int[135]' to 'unsigned long int[136]'
      array type size changed from 8640 to 8704
      array type subrange 1 changed length from 135 to 136
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct mm_struct</code> (mm_types.h:933:1)</summary>

```
  type size changed from 10240 to 11264 (in bits)
  there are data member changes:
    anonymous data member at offset 0 (in bits) changed from:
      struct {struct {atomic_t mm_count;}; maple_tree mm_mt; unsigned long int mmap_base; unsigned long int mmap_legacy_base; unsigned long int mmap_compat_base; unsigned long int mmap_compat_legacy_base; unsigned long int task_size; pgd_t* pgd; atomic_t membarrier_state; atomic_t mm_users; mm_cid* pcpu_cid; unsigned long int mm_cid_next_scan; unsigned int nr_cpus_allowed; atomic_t max_nr_cid; raw_spinlock_t cpus_allowed_lock; atomic_long_t pgtables_bytes; int map_count; spinlock_t page_table_lock; rw_semaphore mmap_lock; list_head mmlist; rcuwait vma_writer_wait; seqcount_t mm_lock_seq; unsigned long int hiwater_rss; unsigned long int hiwater_vm; unsigned long int total_vm; unsigned long int locked_vm; atomic64_t pinned_vm; unsigned long int data_vm; unsigned long int exec_vm; unsigned long int stack_vm; unsigned long int def_flags; seqcount_t write_protect_seq; spinlock_t arg_lock; unsigned long int start_code; unsigned long int end_code; unsigned long int start_data; unsigned long int end_data; unsigned long int start_brk; unsigned long int brk; unsigned long int start_stack; unsigned long int arg_start; unsigned long int arg_end; unsigned long int env_start; unsigned long int env_end; unsigned long int saved_auxv[52]; percpu_counter rss_stat[4]; linux_binfmt* binfmt; mm_context_t context; unsigned long int flags; spinlock_t ioctx_lock; kioctx_table* ioctx_table; user_namespace* user_ns; file* exe_file; mmu_notifier_subscriptions* notifier_subscriptions; atomic_t tlb_flush_pending; atomic_t tlb_flush_batched; uprobes_state uprobes_state; atomic_long_t hugetlb_usage; work_struct async_put_work; iommu_mm_data* iommu_mm;}
    to:
      struct {struct {atomic_t mm_count;}; maple_tree mm_mt; unsigned long int mmap_base; unsigned long int mmap_legacy_base; unsigned long int mmap_compat_base; unsigned long int mmap_compat_legacy_base; unsigned long int task_size; pgd_t* pgd; atomic_t membarrier_state; atomic_t mm_users; mm_cid* pcpu_cid; unsigned long int mm_cid_next_scan; unsigned int nr_cpus_allowed; atomic_t max_nr_cid; raw_spinlock_t cpus_allowed_lock; atomic_long_t pgtables_bytes; int map_count; spinlock_t page_table_lock; rw_semaphore mmap_lock; list_head mmlist; rcuwait vma_writer_wait; seqcount_t mm_lock_seq; mutex futex_hash_lock; futex_private_hash* futex_phash; futex_private_hash* futex_phash_new; unsigned long int futex_batches; callback_head futex_rcu; atomic_long_t futex_atomic; unsigned int* futex_ref; unsigned long int hiwater_rss; unsigned long int hiwater_vm; unsigned long int total_vm; unsigned long int locked_vm; atomic64_t pinned_vm; unsigned long int data_vm; unsigned long int exec_vm; unsigned long int stack_vm; vm_flags_t def_flags; seqcount_t write_protect_seq; spinlock_t arg_lock; unsigned long int start_code; unsigned long int end_code; unsigned long int start_data; unsigned long int end_data; unsigned long int start_brk; unsigned long int brk; unsigned long int start_stack; unsigned long int arg_start; unsigned long int arg_end; unsigned long int env_start; unsigned long int env_end; unsigned long int saved_auxv[52]; percpu_counter rss_stat[4]; linux_binfmt* binfmt; mm_context_t context; unsigned long int flags; spinlock_t ioctx_lock; kioctx_table* ioctx_table; user_namespace* user_ns; file* exe_file; mmu_notifier_subscriptions* notifier_subscriptions; atomic_t tlb_flush_pending; atomic_t tlb_flush_batched; uprobes_state uprobes_state; atomic_long_t hugetlb_usage; work_struct async_put_work; iommu_mm_data* iommu_mm;}
    and size changed from 10240 to 11264 (in bits) (by +1024 bits)
    'unsigned long int cpu_bitmap[]' offset changed from 10240 to 11264 (in bits) (by +1024 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct napi_config</code> (netdevice.h:367:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u8 threaded', at offset 256 (in bits) at netdevice.h:372:1
  there are data member changes:
    'unsigned int napi_id' offset changed from 256 to 288 (in bits) (by +32 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct neigh_table</code> (neighbour.h:202:1)</summary>

```
  type size changed from 4800 to 5056 (in bits)
  1 data member insertion:
    'mutex phash_lock', at offset 4736 (in bits) at neighbour.h:243:1
  there are data member changes:
    'pneigh_entry** phash_buckets' offset changed from 4736 to 4992 (in bits) (by +256 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct net_device</code> (netdevice.h:2084:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u32 num_napi_configs', at offset 19136 (in bits) at netdevice.h:2487:1
  there are data member changes:
    type 'struct device' of 'net_device::dev' changed, as reported earlier
    type 'const attribute_group*[4]' of 'net_device::sysfs_groups' changed:
      type name changed from 'const attribute_group*[4]' to 'const attribute_group*[5]'
      array type size changed from 256 to 320
      array type subrange 1 changed length from 4 to 5
    and offset changed from 16448 to 16512 (in bits) (by +64 bits)
    'const attribute_group* sysfs_rx_queue_group' offset changed from 16704 to 16832 (in bits) (by +128 bits)
    'const rtnl_link_ops* rtnl_link_ops' offset changed from 16768 to 16896 (in bits) (by +128 bits)
    'const netdev_stat_ops* stat_ops' offset changed from 16832 to 16960 (in bits) (by +128 bits)
    'const netdev_queue_mgmt_ops* queue_mgmt_ops' offset changed from 16896 to 17024 (in bits) (by +128 bits)
    'unsigned int tso_max_size' offset changed from 16960 to 17088 (in bits) (by +128 bits)
    'u16 tso_max_segs' offset changed from 16992 to 17120 (in bits) (by +128 bits)
    'u8 prio_tc_map[16]' offset changed from 17008 to 17136 (in bits) (by +128 bits)
    'netprio_map* priomap' offset changed from 17152 to 17280 (in bits) (by +128 bits)
    'phy_link_topology* link_topo' offset changed from 17216 to 17344 (in bits) (by +128 bits)
    'phy_device* phydev' offset changed from 17280 to 17408 (in bits) (by +128 bits)
    'sfp_bus* sfp_bus' offset changed from 17344 to 17472 (in bits) (by +128 bits)
    'lock_class_key* qdisc_tx_busylock' offset changed from 17408 to 17536 (in bits) (by +128 bits)
    'bool proto_down' offset changed from 17472 to 17600 (in bits) (by +128 bits)
    type 'typedef bool' of 'net_device::threaded' changed:
      typedef name changed from bool to u8 at int-ll64.h:17:1
      underlying type 'bool' changed:
        entity changed from 'bool' to compatible type 'typedef __u8' at int-ll64.h:21:1
        type size hasn't changed
    and offset changed from 17480 to 6424 (in bits) (by -11056 bits)
    'bool irq_affinity_auto' offset changed from 17488 to 17608 (in bits) (by +120 bits)
    'bool rx_cpu_rmap_auto' offset changed from 17496 to 17616 (in bits) (by +120 bits)
    'unsigned long int see_all_hwtstamp_requests' offset changed from 17504 to 17624 (in bits) (by +120 bits)
    'unsigned long int change_proto_down' offset changed from 17505 to 17625 (in bits) (by +120 bits)
    'unsigned long int netns_immutable' offset changed from 17506 to 17626 (in bits) (by +120 bits)
    'unsigned long int fcoe_mtu' offset changed from 17507 to 17627 (in bits) (by +120 bits)
    'list_head net_notifier_list' offset changed from 17536 to 17664 (in bits) (by +128 bits)
    'const udp_tunnel_nic_info* udp_tunnel_nic_info' offset changed from 17664 to 17792 (in bits) (by +128 bits)
    'udp_tunnel_nic* udp_tunnel_nic' offset changed from 17728 to 17856 (in bits) (by +128 bits)
    'netdev_config* cfg' offset changed from 17792 to 17920 (in bits) (by +128 bits)
    'netdev_config* cfg_pending' offset changed from 17856 to 17984 (in bits) (by +128 bits)
  ...
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct pid</code> (pid.h:55:1)</summary>

```
  type size changed from 1088 to 1152 (in bits)
  2 data member deletions:
    'u64 ino', at offset 192 (in bits) at pid.h:61:1
    'rb_node pidfs_node', at offset 256 (in bits) at pid.h:62:1
  there are data member changes:
    data member dentry* stashed at offset 128 (in bits) became anonymous data member 'struct {u64 ino; rb_node pidfs_node; dentry* stashed; pidfs_attr* attr;}'
    and size changed from 64 to 384 (in bits) (by +320 bits)
    'hlist_head tasks[4]' offset changed from 448 to 512 (in bits) (by +64 bits)
    'hlist_head inodes' offset changed from 704 to 768 (in bits) (by +64 bits)
    'wait_queue_head_t wait_pidfd' offset changed from 768 to 832 (in bits) (by +64 bits)
    'callback_head rcu' offset changed from 960 to 1024 (in bits) (by +64 bits)
    'upid numbers[]' offset changed from 1088 to 1152 (in bits) (by +64 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct pneigh_entry</code> (neighbour.h:178:1)</summary>

```
  type size changed from 256 to 384 (in bits)
  2 data member insertions:
    'union {list_head free_node; callback_head rcu;}', at offset 192 (in bits)
    'bool permanent', at offset 360 (in bits) at neighbour.h:189:1
  there are data member changes:
    'u32 flags' offset changed from 192 to 320 (in bits) (by +128 bits)
    'u8 protocol' offset changed from 224 to 352 (in bits) (by +128 bits)
    'u32 key[]' offset changed from 256 to 384 (in bits) (by +128 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct request_sock_ops</code> (request_sock.h:28:1)</summary>

```
  type size changed from 512 to 448 (in bits)
  1 data member deletion:
    'int (const sock*, request_sock*)* rtx_syn_ack', at offset 192 (in bits) at request_sock.h:33:1
  there are data member changes:
    'void (const sock*, sk_buff*, request_sock*)* send_ack' offset changed from 256 to 192 (in bits) (by -64 bits)
    'void (const sock*, sk_buff*, enum sk_rst_reason)* send_reset' offset changed from 320 to 256 (in bits) (by -64 bits)
    'void (request_sock*)* destructor' offset changed from 384 to 320 (in bits) (by -64 bits)
    'void (const request_sock*)* syn_ack_timeout' offset changed from 448 to 384 (in bits) (by -64 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct sock</code> (sock.h:351:1)</summary>

```
  type size changed from 6080 to 6144 (in bits)
  1 data member insertion:
    'unsigned long int sk_ino', at offset 4864 (in bits) at sock.h:522:1
  there are data member changes:
    'spinlock_t sk_peer_lock' offset changed from 4864 to 4928 (in bits) (by +64 bits)
    'int sk_bind_phc' offset changed from 4896 to 4960 (in bits) (by +64 bits)
    'pid* sk_peer_pid' offset changed from 4928 to 4992 (in bits) (by +64 bits)
    'const cred* sk_peer_cred' offset changed from 4992 to 5056 (in bits) (by +64 bits)
    'ktime_t sk_stamp' offset changed from 5056 to 5120 (in bits) (by +64 bits)
    'int sk_disconnects' offset changed from 5120 to 5184 (in bits) (by +64 bits)
    anonymous data member 'union {u8 sk_txrehash; u8 sk_scm_recv_flags; struct {u8 sk_scm_credentials; u8 sk_scm_security; u8 sk_scm_pidfd; u8 sk_scm_rights; u8 sk_scm_unused;};}' offset changed from 5152 to 5216 (in bits) (by +64 bits)
    'u8 sk_clockid' offset changed from 5160 to 5224 (in bits) (by +64 bits)
    'u8 sk_txtime_deadline_mode' offset changed from 5168 to 5232 (in bits) (by +64 bits)
    'u8 sk_txtime_report_errors' offset changed from 5169 to 5233 (in bits) (by +64 bits)
    'u8 sk_txtime_unused' offset changed from 5170 to 5234 (in bits) (by +64 bits)
    'u8 sk_bpf_cb_flags' offset changed from 5176 to 5240 (in bits) (by +64 bits)
    'void* sk_user_data' offset changed from 5184 to 5248 (in bits) (by +64 bits)
    'void* sk_security' offset changed from 5248 to 5312 (in bits) (by +64 bits)
    'sock_cgroup_data sk_cgrp_data' offset changed from 5312 to 5376 (in bits) (by +64 bits)
    'void (sock*)* sk_state_change' offset changed from 5440 to 5504 (in bits) (by +64 bits)
    'void (sock*)* sk_write_space' offset changed from 5504 to 5568 (in bits) (by +64 bits)
    'void (sock*)* sk_error_report' offset changed from 5568 to 5632 (in bits) (by +64 bits)
    'int (sock*, sk_buff*)* sk_backlog_rcv' offset changed from 5632 to 5696 (in bits) (by +64 bits)
    'void (sock*)* sk_destruct' offset changed from 5696 to 5760 (in bits) (by +64 bits)
    'sock_reuseport* sk_reuseport_cb' offset changed from 5760 to 5824 (in bits) (by +64 bits)
    'callback_head sk_rcu' offset changed from 5824 to 5888 (in bits) (by +64 bits)
    'netns_tracker ns_tracker' offset changed from 5952 to 6016 (in bits) (by +64 bits)
    'xarray sk_user_frags' offset changed from 5952 to 6016 (in bits) (by +64 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct super_block</code> (fs.h:1325:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'unsigned int s_d_flags', at offset 8160 (in bits) at fs.h:1408:1
  there are data member changes:
    name of 'super_block::s_d_op' changed to 'super_block::__s_d_op' at fs.h:1422:1
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct super_operations</code> (fs.h:2338:1)</summary>

```
  type size changed from 1664 to 1728 (in bits)
  1 data member insertion:
    'int (super_block*, block_device*)* remove_bdev', at offset 1600 (in bits) at fs.h:2381:1
  there are data member changes:
    'void (super_block*)* shutdown' offset changed from 1600 to 1664 (in bits) (by +64 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct task_struct</code> (sched.h:812:1)</summary>

```
  type size changed from 24576 to 25088 (in bits)
  1 data member insertion:
    'mutex* blocked_on', at offset 17728 (in bits) at sched.h:1235:1
  there are data member changes:
    type 'struct sched_entity' of 'task_struct::se' changed, as reported earlier
    type 'struct sched_dl_entity' of 'task_struct::dl' changed, as reported earlier
    'sched_dl_entity* dl_server' offset changed from 5440 to 5376 (in bits) (by -64 bits)
    'const sched_class* sched_class' offset changed from 5504 to 5440 (in bits) (by -64 bits)
    'task_group* sched_task_group' offset changed from 5568 to 5504 (in bits) (by -64 bits)
    'void* journal_info' offset changed from 17728 to 17792 (in bits) (by +64 bits)
    'bio_list* bio_list' offset changed from 17792 to 17856 (in bits) (by +64 bits)
    'blk_plug* plug' offset changed from 17856 to 17920 (in bits) (by +64 bits)
    'reclaim_state* reclaim_state' offset changed from 17920 to 17984 (in bits) (by +64 bits)
    'io_context* io_context' offset changed from 17984 to 18048 (in bits) (by +64 bits)
    'capture_control* capture_control' offset changed from 18048 to 18112 (in bits) (by +64 bits)
    'unsigned long int ptrace_message' offset changed from 18112 to 18176 (in bits) (by +64 bits)
    'kernel_siginfo_t* last_siginfo' offset changed from 18176 to 18240 (in bits) (by +64 bits)
    'task_io_accounting ioac' offset changed from 18240 to 18304 (in bits) (by +64 bits)
    'u64 acct_rss_mem1' offset changed from 18688 to 18752 (in bits) (by +64 bits)
    'u64 acct_vm_mem1' offset changed from 18752 to 18816 (in bits) (by +64 bits)
    'u64 acct_timexpd' offset changed from 18816 to 18880 (in bits) (by +64 bits)
    'nodemask_t mems_allowed' offset changed from 18880 to 18944 (in bits) (by +64 bits)
    'seqcount_spinlock_t mems_allowed_seq' offset changed from 18944 to 19008 (in bits) (by +64 bits)
    'int cpuset_mem_spread_rotor' offset changed from 18976 to 19040 (in bits) (by +64 bits)
    'css_set* cgroups' offset changed from 19008 to 19072 (in bits) (by +64 bits)
    'list_head cg_list' offset changed from 19072 to 19136 (in bits) (by +64 bits)
    'robust_list_head* robust_list' offset changed from 19200 to 19264 (in bits) (by +64 bits)
    'compat_robust_list_head* compat_robust_list' offset changed from 19264 to 19328 (in bits) (by +64 bits)
    'list_head pi_state_list' offset changed from 19328 to 19392 (in bits) (by +64 bits)
    'futex_pi_state* pi_state_cache' offset changed from 19456 to 19520 (in bits) (by +64 bits)
    'mutex futex_exit_mutex' offset changed from 19520 to 19584 (in bits) (by +64 bits)
    'unsigned int futex_state' offset changed from 19776 to 19840 (in bits) (by +64 bits)
    'u8 perf_recursion[4]' offset changed from 19808 to 19872 (in bits) (by +64 bits)
    'perf_event_context* perf_event_ctxp' offset changed from 19840 to 19904 (in bits) (by +64 bits)
    'mutex perf_event_mutex' offset changed from 19904 to 19968 (in bits) (by +64 bits)
    'list_head perf_event_list' offset changed from 20160 to 20224 (in bits) (by +64 bits)
    'perf_ctx_data* perf_ctx_data' offset changed from 20288 to 20352 (in bits) (by +64 bits)
    'mempolicy* mempolicy' offset changed from 20352 to 20416 (in bits) (by +64 bits)
    'short int il_prev' offset changed from 20416 to 20480 (in bits) (by +64 bits)
    'u8 il_weight' offset changed from 20432 to 20496 (in bits) (by +64 bits)
  ...
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

<details><summary><code>struct writeback_control</code> (writeback.h:43:1)</summary>

```
  type size changed from 2624 to 2496 (in bits)
  3 data member deletions:
    'unsigned int for_reclaim', at offset 291 (in bits) at writeback.h:62:1
    'swap_iocb** swap_plug', at offset 320 (in bits) at writeback.h:80:1
    'list_head* list', at offset 384 (in bits) at writeback.h:83:1
  there are data member changes:
    'unsigned int range_cyclic' offset changed from 292 to 291 (in bits) (by -1 bits)
    'unsigned int for_sync' offset changed from 293 to 292 (in bits) (by -1 bits)
    'unsigned int unpinned_netfs_wb' offset changed from 294 to 293 (in bits) (by -1 bits)
    'unsigned int no_cgroup_owner' offset changed from 295 to 294 (in bits) (by -1 bits)
    'folio_batch fbatch' offset changed from 448 to 320 (in bits) (by -128 bits)
    'unsigned long int index' offset changed from 2496 to 2368 (in bits) (by -128 bits)
    'int saved_err' offset changed from 2560 to 2432 (in bits) (by -128 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function ieee80211_txq* ieee80211_next_txq(ieee80211_hw*, u8)`, `function sk_buff* ieee80211_proberesp_get(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)`, `function void ieee80211_radar_detected(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_ready_on_channel(ieee80211_hw*)`, `function int ieee80211_register_hw(ieee80211_hw*)` … (+97 more)

</details>

## Header-level interfaces

Macros, static inline functions, struct/union/enum tags, typedefs and enumerators defined in provider headers (headers the consumer objects were compiled against that are not consumer code) and named in consumer code. They never appear as ELF symbols, but LinuxKPI has to provide them. Name-based, so an occasional false positive is possible (e.g. a local variable or member sharing a macro's name).

| | count |
|---|---|
| used in v6.16 | 852 |
| used in v6.17 | 850 |
| newly used | 0 |
| no longer used | 1 |
| likely renames | 0 |
| macro/inline signature changed | 1 |
| macro body changed | 3 |
| moved to another header | 0 |

### Likely renames (header)

None.

### Newly used (header)

None.

### No longer used (header)

| name | kind | header | signature | used by |
|---|---|---|---|---|
| `crc32_le` | inline | include/linux/crc32.h | `u32(u32 crc, const void *p, size_t len)` | ath10k_core,iwlmld,iwlmvm |

### Signature changed (header)

| name | kind | header | v6.16 | v6.17 |
|---|---|---|---|---|
| `crc32` | inline | include/linux/crc32.h | `(seed,data,length)` | `u32(u32 crc, const void *p, size_t len)` |

<details><summary>Macro body changed (3)</summary>

| macro | header | v6.16 | v6.17 |
|---|---|---|---|
| `GENMASK` | include/linux/bits.h | `(GENMASK_INPUT_CHECK(h, l) + __GENMASK(h, l))` | `GENMASK_TYPE(unsigned long, h, l)` |
| `GENMASK_ULL` | include/linux/bits.h | `(GENMASK_INPUT_CHECK(h, l) + __GENMASK_ULL(h, l))` | `GENMASK_TYPE(unsigned long long, h, l)` |
| `MODULE_PARM_DESC` | include/linux/moduleparam.h | `__MODULE_INFO(parm, _parm, #_parm "" desc)` | `MODULE_INFO(parm, #_parm "" desc)` |

</details>

## Same interface, different set of users

| symbol | v6.16 | v6.17 |
|---|---|---|
| `__x86_indirect_thunk_rcx` | amdgpu,drm_kms_helper,i915,radeon,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt7615-common,mt7915e,mt7925-common,mt7925e,mt7996e,rtw88_8723d,rtw88_8814a,rtw88_8821c,rtw88_8822b,rtw88_8822c,rtw88_core,rtw88_pci,rtw89_8922a,rtw89_core,rtw89_pci | amdgpu,drm,drm_kms_helper,i915,radeon,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt7615-common,mt7915e,mt7925-common,mt7925e,mt7996e,rtw88_8723d,rtw88_8814a,rtw88_8821c,rtw88_8822b,rtw88_8822c,rtw88_core,rtw88_pci,rtw89_8922a,rtw89_core,rtw89_pci |
| `devm_kmalloc` | drm_display_helper,drm_kms_helper,xe,ath10k_core,brcmfmac,iwlwifi,mt76,mt76-connac-lib,mt7615-common,mt7915e,mt7925-common,mt792x-lib,mt7996e,rtw89_core | drm_display_helper,xe,ath10k_core,brcmfmac,iwlwifi,mt76,mt76-connac-lib,mt7615-common,mt7915e,mt7925-common,mt792x-lib,mt7996e,rtw89_core |
| `ieee80211_beacon_cntdwn_is_complete` | ath10k_core,ath11k,iwlmvm,mt76 | ath10k_core,ath11k,iwlmvm,mt76,rtw89_core |
| `ieee80211_csa_finish` | ath10k_core,ath11k,ath12k,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt7996e | ath10k_core,ath11k,ath12k,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt7996e,rtw89_core |
| `ieee80211_iterate_stations_atomic` | ath10k_core,ath11k,iwlmld,iwlmvm,mt7915e,mt792x-lib,mt7996e,rtw88_core,rtw89_core | ath10k_core,ath11k,ath12k,iwlmld,iwlmvm,mt7915e,mt792x-lib,mt7996e,rtw88_core,rtw89_core |
| `ieee80211_tx_status_ext` | ath10k_core,ath11k,iwlmld,iwlmvm,mt76,mt7615-common | ath10k_core,ath11k,ath12k,iwlmld,iwlmvm,mt76,mt7615-common |
| `ktime_get_with_offset` | amdgpu,i915,xe,ath10k_core,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt792x-lib,mt7996e | amdgpu,i915,xe,ath10k_core,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt792x-lib,mt7996e,rtw89_core |

