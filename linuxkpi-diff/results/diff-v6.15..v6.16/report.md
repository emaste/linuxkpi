# Kernel interfaces used by LinuxKPI consumers: v6.15 → v6.16

## Overview by group

Interface counts per consumer group (parents include their children). Per-group reports are in `groups/`.

| group | used | newly used | no longer used | renames | declaration changed | changed types | hdr: newly used | hdr: no longer used | hdr: renames | hdr: signature changed |
|---|---|---|---|---|---|---|---|---|---|---|
| [drm](groups/drm.md) | 1022 | 11 | 6 | 1 | 6 | 60 | 29 | 4 | 1 | 2 |
| &nbsp;&nbsp;[drm/core](groups/drm-core.md) | 358 | 0 | 2 | 1 | 2 | 56 | 1 | 0 | 1 | 0 |
| &nbsp;&nbsp;[drm/ttm](groups/drm-ttm.md) | 127 | 1 | 1 | 0 | 2 | 53 | 1 | 0 | 0 | 0 |
| &nbsp;&nbsp;[drm/sched](groups/drm-sched.md) | 90 | 0 | 0 | 1 | 0 | 52 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[drm/amdgpu](groups/drm-amdgpu.md) | 531 | 5 | 1 | 1 | 4 | 60 | 11 | 1 | 1 | 0 |
| &nbsp;&nbsp;[drm/radeon](groups/drm-radeon.md) | 272 | 0 | 2 | 1 | 1 | 56 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[drm/i915](groups/drm-i915.md) | 678 | 6 | 4 | 1 | 6 | 59 | 13 | 2 | 1 | 1 |
| &nbsp;&nbsp;[drm/xe](groups/drm-xe.md) | 517 | 0 | 2 | 1 | 4 | 58 | 15 | 1 | 0 | 2 |
| [wifi](groups/wifi.md) | 731 | 4 | 3 | 1 | 2 | 68 | 25 | 6 | 1 | 1 |
| &nbsp;&nbsp;[wifi/iwlwifi](groups/wifi-iwlwifi.md) | 379 | 0 | 1 | 1 | 1 | 60 | 4 | 5 | 1 | 1 |
| &nbsp;&nbsp;[wifi/mt76](groups/wifi-mt76.md) | 337 | 0 | 0 | 1 | 2 | 58 | 0 | 0 | 1 | 0 |
| &nbsp;&nbsp;[wifi/rtw88](groups/wifi-rtw88.md) | 186 | 0 | 0 | 1 | 1 | 58 | 1 | 0 | 1 | 0 |
| &nbsp;&nbsp;[wifi/rtw89](groups/wifi-rtw89.md) | 213 | 0 | 0 | 1 | 1 | 58 | 4 | 0 | 0 | 1 |
| &nbsp;&nbsp;[wifi/ath](groups/wifi-ath.md) | 16 | 0 | 0 | 0 | 0 | 53 | 0 | 0 | 0 | 0 |
| &nbsp;&nbsp;[wifi/ath10k](groups/wifi-ath10k.md) | 232 | 0 | 0 | 1 | 1 | 58 | 0 | 0 | 1 | 0 |
| &nbsp;&nbsp;[wifi/ath11k](groups/wifi-ath11k.md) | 269 | 2 | 2 | 1 | 1 | 63 | 4 | 1 | 1 | 0 |
| &nbsp;&nbsp;[wifi/ath12k](groups/wifi-ath12k.md) | 252 | 3 | 2 | 1 | 1 | 63 | 11 | 1 | 1 | 0 |
| &nbsp;&nbsp;[wifi/brcm80211](groups/wifi-brcm80211.md) | 217 | 1 | 0 | 1 | 1 | 58 | 4 | 0 | 1 | 0 |

## Symbol-level summary

| | count |
|---|---|
| interfaces used in v6.15 | 1441 |
| interfaces used in v6.16 | 1448 |
| likely renames | 1 |
| newly used (excluding renames) | 15 |
| no longer used (excluding renames) | 8 |
| export kind/owner/namespace changed | 0 |
| used in both, own declaration changed | 6 |
| changed types reachable from used interfaces | 73 |

## Likely renames

Dropped and newly used symbols with identical signatures (types and parameter names) and similar names.

| v6.15 | v6.16 | signature | used by |
|---|---|---|---|
| `init_timer_key` | `timer_init_key` | `void(struct timer_list* timer, fn(struct timer_list*)->void* func, unsigned int flags, const char* name, struct lock_class_key* key)` | amdgpu,drm,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw88_core,rtw89_core |

## Newly used in v6.16

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `cfg80211_external_auth_request` | func | net/wireless/cfg80211 | plain | net/wireless/nl80211.c | brcmfmac-cyw |
| `compat_vma_mmap_prepare` | func | vmlinux | plain | mm/util.c | i915 |
| `crypto_shash_finup` | func | vmlinux | GPL | crypto/shash.c | ath11k,ath12k |
| `crypto_shash_init` | func | vmlinux | GPL | crypto/shash.c | ath11k,ath12k |
| `dma_fence_dedup_array` | func | vmlinux | GPL | drivers/dma-buf/dma-fence-unwrap.c | amdgpu |
| `dma_fence_unwrap_first` | func | vmlinux | GPL | drivers/dma-buf/dma-fence-unwrap.c | amdgpu |
| `dma_fence_unwrap_next` | func | vmlinux | GPL | drivers/dma-buf/dma-fence-unwrap.c | amdgpu |
| `dma_resv_describe` | func | vmlinux | GPL | drivers/dma-buf/dma-resv.c | amdgpu |
| `folio_redirty_for_writepage` | func | vmlinux | plain | mm/page-writeback.c | i915 |
| `generic_handle_irq_safe` | func | vmlinux | GPL | kernel/irq/irqdesc.c | i915 |
| `ieee80211_queue_stopped` | func | net/mac80211/mac80211 | plain | net/mac80211/util.c | ath12k |
| `intel_gmch_gtt_read_entry` | func | vmlinux | plain | drivers/char/agp/intel-gtt.c | i915 |
| `shmem_writeout` | func | vmlinux | GPL | mm/shmem.c | i915,ttm |
| `sysfs_update_group` | func | vmlinux | GPL | fs/sysfs/group.c | amdgpu |
| `writeback_iter` | func | vmlinux | GPL | mm/page-writeback.c | i915 |

## No longer used in v6.16

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `clear_page_dirty_for_io` | func | vmlinux | plain | mm/folio-compat.c | i915 |
| `console_lock` | func | vmlinux | plain | kernel/printk/printk.c | radeon |
| `console_unlock` | func | vmlinux | plain | kernel/printk/printk.c | radeon |
| `crypto_shash_final` | func | vmlinux | GPL | crypto/shash.c | ath11k,ath12k |
| `crypto_shash_update` | func | vmlinux | GPL | crypto/shash.c | ath11k,ath12k |
| `llist_add_batch` | func | vmlinux | GPL | lib/llist.c | drm,i915,xe |
| `pagecache_get_page` | func | vmlinux | plain | mm/folio-compat.c | i915 |
| `sg_next` | func | vmlinux | plain | lib/scatterlist.c | amdgpu,drm,i915,ttm,xe,iwlwifi |

## Interfaces whose own declaration changed

Return/parameter types, variable types, or interfaces that lost their debug info. `[C]` changed, `[D]` deleted.

**[C] 'function void perf_pmu_unregister(pmu*)' at core.c:12480:1 has some sub-type changes:** (vmlinux)

```
    return type changed:
      type name changed from 'void' to 'int'
      type size changed from 0 to 32 (in bits)
```

**[D] 'cpuinfo_x86 boot_cpu_data'    {boot_cpu_data}** (vmlinux)

**[C] 'const dma_fence_ops dma_fence_array_ops' was changed at dma-fence.h:632:1:** (vmlinux)

```
    size of symbol changed from 80 to 64
    type of variable changed:
      in unqualified underlying type 'struct dma_fence_ops' at dma-fence.h:126:1:
        type size changed from 640 to 512 (in bits)
        2 data member deletions:
          'void (dma_fence*, char*, int)* fence_value_str', at offset 448 (in bits) at dma-fence.h:249:1
          'void (dma_fence*, char*, int)* timeline_value_str', at offset 512 (in bits) at dma-fence.h:259:1
        there are data member changes:
          'void (dma_fence*, typedef ktime_t)* set_deadline' offset changed from 576 to 448 (in bits) (by -128 bits)
```

**[C] 'const dma_fence_ops dma_fence_chain_ops' was changed at dma-fence.h:633:1:** (vmlinux)

```
    size of symbol changed from 80 to 64
    type of variable changed:
      unqualified underlying type 'struct dma_fence_ops' changed at dma-fence.h:126:1, as reported earlier
```

**[C] 'const file_operations relay_file_operations' was changed at relay.h:275:1:** (vmlinux)

```
    size of symbol changed from 264 to 272
    type of variable changed:
      in unqualified underlying type 'struct file_operations' at fs.h:2151:1:
        type size changed from 2112 to 2176 (in bits)
        1 data member insertion:
          'int (vm_area_desc*)* mmap_prepare', at offset 2112 (in bits) at fs.h:2194:1
```

**[D] phys_base** (vmlinux)

## Changed types

Each changed type reachable from an interface this group uses, with the number of those interfaces it reaches, fewest first: low counts are targeted changes, high counts are churn reached through hub types (reachability is transitive through pointers, so e.g. `struct device` or `struct module` pull in hundreds).

| type | declared at | change | used interfaces reached |
|---|---|---|---|
| `struct cfg80211_ap_settings` | cfg80211.h:1502:1 | there are data member changes | 1 |
| `struct drm_device` | drm_device.h:57:1 | type size changed from 12480 to 12608 (in bits); 1 data member insertion; there are data member changes | 1 |
| `struct i2c_board_info` | i2c.h:426:1 | type size changed from 640 to 576 (in bits); 1 data member deletion; there are data member changes | 1 |
| `struct station_parameters` | cfg80211.h:1775:1 | 2 data member insertions | 1 |
| `struct crypto_alg` | crypto.h:328:1 | type size changed from 3072 to 3136 (in bits); 1 data member insertion; there are data member changes | 3 |
| `struct crypto_instance` | algapi.h:59:1 | type size changed from 3520 to 3328 (in bits); 1 data member deletion; there are data member changes | 3 |
| `struct crypto_shash` | hash.h:240:1 | 1 data member deletion; there are data member changes | 3 |
| `struct crypto_template` | algapi.h:76:1 | type size changed from 1344 to 1664 (in bits); 2 data member insertions; there are data member changes | 3 |
| `struct crypto_type` | internal.h:36:1 | type size changed from 576 to 640 (in bits); 1 data member insertion | 3 |
| `struct dma_pool` | dmapool.c:48:1 | 1 data member insertion; there are data member changes | 3 |
| `struct ptp_clock_info` | ptp_clock_kernel.h:168:1 | type size changed from 1472 to 1536 (in bits); 2 data member insertions; there are data member changes | 3 |
| `enum skb_drop_reason` | dropreason-core.h:129:1 | 2 enumerator insertions; 80 enumerator changes | 4 |
| `struct platform_device_id` | mod_devicetable.h:607:1 | there are data member changes | 4 |
| `struct backlight_device` | backlight.h:247:1 | type size changed from 7168 to 6720 (in bits); 2 data member deletions; there are data member changes | 7 |
| `struct dma_buf_attachment` | dma-buf.h:513:1 | type size changed from 576 to 512 (in bits); 2 data member deletions; there are data member changes | 15 |
| `struct dma_buf_ops` | dma-buf.h:36:1 | type size changed from 832 to 768 (in bits); 1 data member deletion; there are data member changes | 15 |
| `struct ieee80211_bss_conf` | mac80211.h:758:1 | type size changed from 6976 to 7104 (in bits); 2 data member insertions; there are data member changes | 77 |
| `struct ieee80211_sta` | mac80211.h:2511:1 | 1 data member insertion | 77 |
| `struct ieee80211_vif` | mac80211.h:2028:1 | type size changed from 9408 to 9472 (in bits); 1 data member deletion; there are data member changes | 77 |
| `struct pci_dev` | pci.h:332:1 | type size changed from 16768 to 16704 (in bits); 1 data member deletion; there are data member changes | 99 |
| `struct file_operations` | fs.h:2129:1 | type size changed from 2112 to 2176 (in bits); 1 data member insertion | 147 |
| `struct bio` | blk_types.h:214:1 | 1 data member insertion; there are data member changes | 587 |
| `struct fib6_info` | ip6_fib.h:158:1 | type size changed from 1472 to 1600 (in bits); 1 data member insertion; there are data member changes | 587 |
| `struct folio_queue` | folio_queue.h:30:1 | type size changed from 2688 to 2624 (in bits); 1 data member deletion; there are data member changes | 587 |
| `struct gendisk` | blkdev.h:142:1 | type size changed from 4544 to 4736 (in bits); 1 data member deletion; 1 data member insertion; there are data member changes | 587 |
| `struct io_ring_ctx` | io_uring_types.h:239:1 | 1 data member deletion; 2 data member insertions; there are data member changes | 587 |
| `struct iommu_device` | iommu.h:754:1 | 1 data member insertion | 587 |
| `struct iommu_iotlb_gather` | iommu.h:362:1 | there are data member changes | 587 |
| `struct iommu_ops` | iommu.h:627:1 | type size changed from 1728 to 1600 (in bits); 2 data member deletions; there are data member changes | 587 |
| `struct linux_binfmt` | binfmts.h:89:1 | type size changed from 448 to 384 (in bits); 1 data member deletion; there are data member changes | 587 |
| `struct mnt_namespace` | mount.h:14:1 | 1 data member deletion | 587 |
| `struct msi_domain_info` | msi.h:491:1 | type size changed from 576 to 640 (in bits); 1 data member insertion; there are data member changes | 587 |
| `struct msi_domain_ops` | msi.h:448:1 | type size changed from 640 to 704 (in bits); 1 data member insertion; there are data member changes | 587 |
| `struct nexthop` | nexthop.h:142:1 | 2 data member insertions; there are data member changes | 587 |
| `struct page_pool` | types.h:162:1 | 1 data member insertion; there are data member changes | 587 |
| `struct per_cpu_zonestat` | mmzone.h:728:1 | there are data member changes | 587 |
| `struct pglist_data` | mmzone.h:1341:1 | type size changed from 114688 to 112640 (in bits); there are data member changes | 587 |
| `struct phy_driver` | phy.h:898:1 | there are data member changes | 587 |
| `struct queue_limits` | blkdev.h:365:1 | type size changed from 1408 to 1472 (in bits); 2 data member insertions; there are data member changes | 587 |
| `struct request_queue` | blkdev.h:459:1 | type size changed from 7680 to 7744 (in bits); there are data member changes | 587 |
| `struct rq` | sched.h:1097:1 | type size changed from 26112 to 26624 (in bits); there are data member changes | 587 |
| `struct task_group` | sched.h:431:1 | there are data member changes | 587 |
| `struct trace_array` | trace.h:326:1 | type size changed from 3328 to 3456 (in bits); 1 data member insertion; there are data member changes | 587 |
| `struct trace_array_cpu` | trace.h:185:1 | type size changed from 1024 to 960 (in bits); 1 data member deletion; there are data member changes | 587 |
| `struct zone` | mmzone.h:845:1 | type size changed from 10240 to 9728 (in bits); there are data member changes | 587 |
| `enum perf_event_state` | perf_event.h:624:1 | 1 enumerator insertion; 1 enumerator change | 602 |
| `struct hw_perf_event` | perf_event.h:155:1 | type size changed from 1536 to 1664 (in bits); there are data member changes | 602 |
| `struct perf_cgroup` | perf_event.h:1123:1 | there are data member changes | 602 |
| `struct perf_event` | perf_event.h:708:1 | type size changed from 8768 to 9024 (in bits); 1 data member insertion; there are data member changes | 602 |
| `struct pmu` | perf_event.h:325:1 | type size changed from 2368 to 2560 (in bits); 2 data member insertions; there are data member changes | 602 |
| `struct kernel_ethtool_ts_info` | ethtool.h:763:1 | type size changed from 192 to 256 (in bits); 2 data member insertions; there are data member changes | 706 |
| `enum hwtstamp_source` | net_tstamp.h:16:1 | 1 enumerator deletion | 713 |
| `struct linux_mib` | snmp.h:104:1 | type size changed from 8576 to 8640 (in bits); there are data member changes | 713 |
| `struct net` | net_namespace.h:61:1 | there are data member changes | 713 |
| `struct net_device` | netdevice.h:2080:1 | 1 data member insertion; there are data member changes | 713 |
| `struct netlink_ext_ack` | netlink.h:82:1 | type size changed from 1088 to 1024 (in bits); there are data member changes | 713 |
| `struct sock` | sock.h:345:1 | type size hasn't changed | 713 |
| `struct address_space_operations` | fs.h:435:1 | type size changed from 1280 to 1216 (in bits); 1 data member deletion; there are data member changes | 734 |
| `struct cgroup` | cgroup-defs.h:412:1 | type size changed from 9216 to 8704 (in bits); 2 data member deletions; there are data member changes | 734 |
| `struct cgroup_root` | cgroup-defs.h:577:1 | type size changed from 43520 to 43008 (in bits); there are data member changes | 734 |
| `struct cgroup_subsys` | cgroup-defs.h:706:1 | type size changed from 2048 to 2112 (in bits); 2 data member insertions | 734 |
| `struct dir_context` | fs.h:2071:1 | type size changed from 128 to 192 (in bits); 1 data member insertion | 734 |
| `struct kiocb` | fs.h:404:1 | 1 data member insertion | 734 |
| `struct kstat` | stat.h:22:1 | type size changed from 1472 to 1536 (in bits); 1 data member insertion; there are data member changes | 734 |
| `struct mod_arch_specific` | module.h:8:1 | type size changed from 192 to 320 (in bits); 1 data member insertion | 734 |
| `struct module` | module.h:414:1 | 2 data member deletions; there are data member changes | 734 |
| `struct sb_writers` | fs.h:1306:1 | type size changed from 2432 to 2496 (in bits); 1 data member insertion; there are data member changes | 734 |
| `struct super_block` | fs.h:1313:1 | type size changed from 10240 to 10752 (in bits); there are data member changes | 734 |
| `struct super_operations` | fs.h:2287:1 | there are data member changes | 734 |
| `struct task_struct` | sched.h:813:1 | type size changed from 58880 to 24576 (in bits); 1 data member insertion; there are data member changes | 734 |
| `struct user_struct` | user.h:14:1 | there are data member changes | 734 |
| `struct vm_area_struct` | mm_types.h:779:1 | 1 data member insertion | 734 |
| `struct ratelimit_state` | ratelimit_types.h:15:1 | there are data member changes | 735 |

### Details

<details><summary><code>struct cfg80211_ap_settings</code> (cfg80211.h:1502:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cfg80211_mbssid_config' of 'cfg80211_ap_settings::mbssid_config' changed:
      type size hasn't changed
      1 data member insertion:
        'u8 tx_link_id', at offset 64 (in bits) at cfg80211.h:1272:1
      there are data member changes:
        'u8 index' offset changed from 64 to 72 (in bits) (by +8 bits)
        'bool ema' offset changed from 72 to 80 (in bits) (by +8 bits)
```

Reaches: `function wiphy* wiphy_new_nm(const cfg80211_ops*, int, const char*)`

</details>

<details><summary><code>struct drm_device</code> (drm_device.h:57:1)</summary>

```
  type size changed from 12480 to 12608 (in bits)
  1 data member insertion:
    'device* dma_dev', at offset 128 (in bits) at drm_device.h:87:1
  there are data member changes:
    'struct {list_head resources; void* final_kfree; spinlock_t lock;} managed' offset changed from 128 to 192 (in bits) (by +64 bits)
    'const drm_driver* driver' offset changed from 384 to 448 (in bits) (by +64 bits)
    'void* dev_private' offset changed from 448 to 512 (in bits) (by +64 bits)
    'drm_minor* primary' offset changed from 512 to 576 (in bits) (by +64 bits)
    'drm_minor* render' offset changed from 576 to 640 (in bits) (by +64 bits)
    'drm_minor* accel' offset changed from 640 to 704 (in bits) (by +64 bits)
    'bool registered' offset changed from 704 to 768 (in bits) (by +64 bits)
    'drm_master* master' offset changed from 768 to 832 (in bits) (by +64 bits)
    'u32 driver_features' offset changed from 832 to 896 (in bits) (by +64 bits)
    'bool unplugged' offset changed from 864 to 928 (in bits) (by +64 bits)
    'inode* anon_inode' offset changed from 896 to 960 (in bits) (by +64 bits)
    'char* unique' offset changed from 960 to 1024 (in bits) (by +64 bits)
    'mutex struct_mutex' offset changed from 1024 to 1088 (in bits) (by +64 bits)
    'mutex master_mutex' offset changed from 1280 to 1344 (in bits) (by +64 bits)
    'atomic_t open_count' offset changed from 1536 to 1600 (in bits) (by +64 bits)
    'mutex filelist_mutex' offset changed from 1600 to 1664 (in bits) (by +64 bits)
    'list_head filelist' offset changed from 1856 to 1920 (in bits) (by +64 bits)
    'list_head filelist_internal' offset changed from 1984 to 2048 (in bits) (by +64 bits)
    'mutex clientlist_mutex' offset changed from 2112 to 2176 (in bits) (by +64 bits)
    'list_head clientlist' offset changed from 2368 to 2432 (in bits) (by +64 bits)
    'bool vblank_disable_immediate' offset changed from 2496 to 2560 (in bits) (by +64 bits)
    'drm_vblank_crtc* vblank' offset changed from 2560 to 2624 (in bits) (by +64 bits)
    'spinlock_t vblank_time_lock' offset changed from 2624 to 2688 (in bits) (by +64 bits)
    'spinlock_t vbl_lock' offset changed from 2656 to 2720 (in bits) (by +64 bits)
    'u32 max_vblank_count' offset changed from 2688 to 2752 (in bits) (by +64 bits)
    'list_head vblank_event_list' offset changed from 2752 to 2816 (in bits) (by +64 bits)
    'spinlock_t event_lock' offset changed from 2880 to 2944 (in bits) (by +64 bits)
    'unsigned int num_crtcs' offset changed from 2912 to 2976 (in bits) (by +64 bits)
    type 'struct drm_mode_config' of 'drm_device::mode_config' changed:
      type size changed from 8768 to 8832 (in bits)
      1 data member insertion:
        'drm_property* async_modifiers_property', at offset 8512 (in bits) at drm_mode_config.h:943:1
      there are data member changes:
        type 'int' of 'drm_mode_config::min_width' changed:
          type name changed from 'int' to 'unsigned int'
          type size hasn't changed
  ...
```

Reaches: `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`

</details>

<details><summary><code>struct i2c_board_info</code> (i2c.h:426:1)</summary>

```
  type size changed from 640 to 576 (in bits)
  1 data member deletion:
    'device_node* of_node', at offset 320 (in bits) at i2c.h:432:1
  there are data member changes:
    'fwnode_handle* fwnode' offset changed from 384 to 320 (in bits) (by -64 bits)
    'const software_node* swnode' offset changed from 448 to 384 (in bits) (by -64 bits)
    'const resource* resources' offset changed from 512 to 448 (in bits) (by -64 bits)
    'unsigned int num_resources' offset changed from 576 to 512 (in bits) (by -64 bits)
    'int irq' offset changed from 608 to 544 (in bits) (by -64 bits)
```

Reaches: `function i2c_client* i2c_new_client_device(i2c_adapter*, const i2c_board_info*)`

</details>

<details><summary><code>struct station_parameters</code> (cfg80211.h:1775:1)</summary>

```
  type size hasn't changed
  2 data member insertions:
    'bool eml_cap_present', at offset 784 (in bits) at cfg80211.h:1765:1
    'u16 eml_cap', at offset 800 (in bits) at cfg80211.h:1766:1
```

Reaches: `function wiphy* wiphy_new_nm(const cfg80211_ops*, int, const char*)`

</details>

<details><summary><code>struct crypto_alg</code> (crypto.h:328:1)</summary>

```
  type size changed from 3072 to 3136 (in bits)
  1 data member insertion:
    'unsigned int cra_reqsize', at offset 384 (in bits) at crypto.h:337:1
  there are data member changes:
    'int cra_priority' offset changed from 384 to 416 (in bits) (by +32 bits)
    'refcount_t cra_refcnt' offset changed from 416 to 448 (in bits) (by +32 bits)
    'char cra_name[128]' offset changed from 448 to 480 (in bits) (by +32 bits)
    'char cra_driver_name[128]' offset changed from 1472 to 1504 (in bits) (by +32 bits)
    'const crypto_type* cra_type' offset changed from 2496 to 2560 (in bits) (by +64 bits)
    'union {cipher_alg cipher;} cra_u' offset changed from 2560 to 2624 (in bits) (by +64 bits)
    'int (crypto_tfm*)* cra_init' offset changed from 2816 to 2880 (in bits) (by +64 bits)
    'void (crypto_tfm*)* cra_exit' offset changed from 2880 to 2944 (in bits) (by +64 bits)
    'void (crypto_alg*)* cra_destroy' offset changed from 2944 to 3008 (in bits) (by +64 bits)
    'module* cra_module' offset changed from 3008 to 3072 (in bits) (by +64 bits)
```

Reaches: `function crypto_shash* crypto_alloc_shash(const char*, u32, u32)`, `function void crypto_destroy_tfm(void*, crypto_tfm*)`, `function int crypto_shash_setkey(crypto_shash*, const u8*, unsigned int)`

</details>

<details><summary><code>struct crypto_instance</code> (algapi.h:59:1)</summary>

```
  type size changed from 3520 to 3328 (in bits)
  1 data member deletion:
    'work_struct free_work', at offset 3264 (in bits) at algapi.h:71:1
  there are data member changes:
    type 'struct crypto_alg' of 'crypto_instance::alg' changed, as reported earlier
    'crypto_template* tmpl' offset changed from 3072 to 3136 (in bits) (by +64 bits)
    anonymous data member 'union {hlist_node list; crypto_spawn* spawns;}' offset changed from 3136 to 3200 (in bits) (by +64 bits)
    'void* __ctx[]' offset changed from 3520 to 3328 (in bits) (by -192 bits)
```

Reaches: `function crypto_shash* crypto_alloc_shash(const char*, u32, u32)`, `function void crypto_destroy_tfm(void*, crypto_tfm*)`, `function int crypto_shash_setkey(crypto_shash*, const u8*, unsigned int)`

</details>

<details><summary><code>struct crypto_shash</code> (hash.h:240:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'unsigned int descsize', at offset 0 (in bits) at hash.h:241:1
  there are data member changes:
    type 'struct crypto_tfm' of 'crypto_shash::base' changed:
      type size changed from 256 to 320 (in bits)
      1 data member insertion:
        'crypto_tfm* fb', at offset 128 (in bits) at crypto.h:415:1
      there are data member changes:
        'void (crypto_tfm*)* exit' offset changed from 128 to 192 (in bits) (by +64 bits)
        'crypto_alg* __crt_alg' offset changed from 192 to 256 (in bits) (by +64 bits)
        'void* __crt_ctx[]' offset changed from 256 to 320 (in bits) (by +64 bits)
    and offset changed from 64 to 0 (in bits) (by -64 bits)
```

Reaches: `function crypto_shash* crypto_alloc_shash(const char*, u32, u32)`, `function void crypto_destroy_tfm(void*, crypto_tfm*)`, `function int crypto_shash_setkey(crypto_shash*, const u8*, unsigned int)`

</details>

<details><summary><code>struct crypto_template</code> (algapi.h:76:1)</summary>

```
  type size changed from 1344 to 1664 (in bits)
  2 data member insertions:
    'hlist_head dead', at offset 192 (in bits) at algapi.h:77:1
    'work_struct free_work', at offset 320 (in bits) at algapi.h:80:1
  there are data member changes:
    'module* module' offset changed from 192 to 256 (in bits) (by +64 bits)
    'int (crypto_template*, rtattr**)* create' offset changed from 256 to 576 (in bits) (by +320 bits)
    'char name[128]' offset changed from 320 to 640 (in bits) (by +320 bits)
```

Reaches: `function crypto_shash* crypto_alloc_shash(const char*, u32, u32)`, `function void crypto_destroy_tfm(void*, crypto_tfm*)`, `function int crypto_shash_setkey(crypto_shash*, const u8*, unsigned int)`

</details>

<details><summary><code>struct crypto_type</code> (internal.h:36:1)</summary>

```
  type size changed from 576 to 640 (in bits)
  1 data member insertion:
    'unsigned int algsize', at offset 576 (in bits) at internal.h:49:1
```

Reaches: `function crypto_shash* crypto_alloc_shash(const char*, u32, u32)`, `function void crypto_destroy_tfm(void*, crypto_tfm*)`, `function int crypto_shash_setkey(crypto_shash*, const u8*, unsigned int)`

</details>

<details><summary><code>struct dma_pool</code> (dmapool.c:48:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'int node', at offset 608 (in bits) at dmapool.c:59:1
  there are data member changes:
    'char name[32]' offset changed from 608 to 640 (in bits) (by +32 bits)
```

Reaches: `function void* dma_pool_alloc(dma_pool*, gfp_t, dma_addr_t*)`, `function void dma_pool_free(dma_pool*, void*, dma_addr_t)`, `function dma_pool* dmam_pool_create(const char*, device*, size_t, size_t, size_t)`

</details>

<details><summary><code>struct ptp_clock_info</code> (ptp_clock_kernel.h:168:1)</summary>

```
  type size changed from 1472 to 1536 (in bits)
  2 data member insertions:
    'unsigned int supported_perout_flags', at offset 512 (in bits) at ptp_clock_kernel.h:193:1
    'unsigned int supported_extts_flags', at offset 544 (in bits) at ptp_clock_kernel.h:194:1
  there are data member changes:
    'ptp_pin_desc* pin_config' offset changed from 512 to 576 (in bits) (by +64 bits)
    'int (ptp_clock_info*, long int)* adjfine' offset changed from 576 to 640 (in bits) (by +64 bits)
    'int (ptp_clock_info*, typedef s32)* adjphase' offset changed from 640 to 704 (in bits) (by +64 bits)
    'typedef s32 (ptp_clock_info*)* getmaxphase' offset changed from 704 to 768 (in bits) (by +64 bits)
    'int (ptp_clock_info*, typedef s64)* adjtime' offset changed from 768 to 832 (in bits) (by +64 bits)
    'int (ptp_clock_info*, timespec64*)* gettime64' offset changed from 832 to 896 (in bits) (by +64 bits)
    'int (ptp_clock_info*, timespec64*, ptp_system_timestamp*)* gettimex64' offset changed from 896 to 960 (in bits) (by +64 bits)
    'int (ptp_clock_info*, system_device_crosststamp*)* getcrosststamp' offset changed from 960 to 1024 (in bits) (by +64 bits)
    'int (ptp_clock_info*, const timespec64*)* settime64' offset changed from 1024 to 1088 (in bits) (by +64 bits)
    'int (ptp_clock_info*, timespec64*)* getcycles64' offset changed from 1088 to 1152 (in bits) (by +64 bits)
    'int (ptp_clock_info*, timespec64*, ptp_system_timestamp*)* getcyclesx64' offset changed from 1152 to 1216 (in bits) (by +64 bits)
    'int (ptp_clock_info*, system_device_crosststamp*)* getcrosscycles' offset changed from 1216 to 1280 (in bits) (by +64 bits)
    'int (ptp_clock_info*, ptp_clock_request*, int)* enable' offset changed from 1280 to 1344 (in bits) (by +64 bits)
    'int (ptp_clock_info*, unsigned int, enum ptp_pin_function, unsigned int)* verify' offset changed from 1344 to 1408 (in bits) (by +64 bits)
    'long int (ptp_clock_info*)* do_aux_work' offset changed from 1408 to 1472 (in bits) (by +64 bits)
```

Reaches: `function int ptp_clock_index(ptp_clock*)`, `function ptp_clock* ptp_clock_register(ptp_clock_info*, device*)`, `function int ptp_clock_unregister(ptp_clock*)`

</details>

<details><summary><code>enum skb_drop_reason</code> (dropreason-core.h:129:1)</summary>

```
  type size hasn't changed
  2 enumerator insertions:
    'skb_drop_reason::SKB_DROP_REASON_TCP_RFC7323_TW_PAWS' value '38'
    'skb_drop_reason::SKB_DROP_REASON_NEIGH_HH_FILLFAIL' value '60'
  80 enumerator changes:
    'skb_drop_reason::SKB_DROP_REASON_TCP_RFC7323_TSECR' from value '38' to '39' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_LISTEN_OVERFLOW' from value '39' to '40' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_OLD_SEQUENCE' from value '40' to '41' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_INVALID_SEQUENCE' from value '41' to '42' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_INVALID_ACK_SEQUENCE' from value '42' to '43' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_RESET' from value '43' to '44' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_INVALID_SYN' from value '44' to '45' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_CLOSE' from value '45' to '46' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_FASTOPEN' from value '46' to '47' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_OLD_ACK' from value '47' to '48' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_TOO_OLD_ACK' from value '48' to '49' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_ACK_UNSENT_DATA' from value '49' to '50' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE' from value '50' to '51' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TCP_OFO_DROP' from value '51' to '52' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_IP_OUTNOROUTES' from value '52' to '53' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_BPF_CGROUP_EGRESS' from value '53' to '54' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_IPV6DISABLED' from value '54' to '55' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_NEIGH_CREATEFAIL' from value '55' to '56' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_NEIGH_FAILED' from value '56' to '57' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_NEIGH_QUEUEFULL' from value '57' to '58' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_NEIGH_DEAD' from value '58' to '59' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TC_EGRESS' from value '59' to '61' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_SECURITY_HOOK' from value '60' to '62' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_QDISC_DROP' from value '61' to '63' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_QDISC_OVERLIMIT' from value '62' to '64' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_QDISC_CONGESTED' from value '63' to '65' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_CAKE_FLOOD' from value '64' to '66' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_FQ_BAND_LIMIT' from value '65' to '67' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_FQ_HORIZON_LIMIT' from value '66' to '68' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_FQ_FLOW_LIMIT' from value '67' to '69' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_CPU_BACKLOG' from value '68' to '70' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_XDP' from value '69' to '71' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_TC_INGRESS' from value '70' to '72' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_UNHANDLED_PROTO' from value '71' to '73' at dropreason-core.h:131:1
    'skb_drop_reason::SKB_DROP_REASON_SKB_CSUM' from value '72' to '74' at dropreason-core.h:131:1
  ...
```

Reaches: `function void dev_kfree_skb_any_reason(sk_buff*, skb_drop_reason)`, `function void dev_kfree_skb_irq_reason(sk_buff*, skb_drop_reason)`, `function void sk_skb_reason_drop(sock*, sk_buff*, skb_drop_reason)`, `function void skb_queue_purge_reason(sk_buff_head*, skb_drop_reason)`

</details>

<details><summary><code>struct platform_device_id</code> (mod_devicetable.h:607:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'char[20]' of 'platform_device_id::name' changed:
      type name changed from 'char[20]' to 'char[24]'
      array type size changed from 160 to 192
      array type subrange 1 changed length from 20 to 24
```

Reaches: `function int __platform_driver_probe(platform_driver*, int (platform_device*)*, module*)`, `function platform_device* platform_device_register_full(const platform_device_info*)`, `function void platform_device_unregister(platform_device*)`, `function void platform_driver_unregister(platform_driver*)`

</details>

<details><summary><code>struct backlight_device</code> (backlight.h:247:1)</summary>

```
  type size changed from 7168 to 6720 (in bits)
  2 data member deletions:
    'notifier_block fb_notif', at offset 768 (in bits) at backlight.h:284:1
    'bool fb_bl_on[32]', at offset 6848 (in bits) at backlight.h:302:1
  there are data member changes:
    'list_head entry' offset changed from 960 to 768 (in bits) (by -192 bits)
    'device dev' offset changed from 1088 to 896 (in bits) (by -192 bits)
    'int use_count' offset changed from 7104 to 6656 (in bits) (by -448 bits)
```

Reaches: `function backlight_device* backlight_device_get_by_name(const char*)`, `function backlight_device* backlight_device_register(const char*, device*, void*, const backlight_ops*, const backlight_properties*)`, `function int backlight_device_set_brightness(backlight_device*, unsigned long int)`, `function void backlight_device_unregister(backlight_device*)`, `function void backlight_force_update(backlight_device*, backlight_update_reason)`, `function backlight_device* devm_backlight_device_register(device*, const char*, device*, void*, const backlight_ops*, const backlight_properties*)`, `function backlight_device* devm_of_find_backlight(device*)`

</details>

<details><summary><code>struct dma_buf_attachment</code> (dma-buf.h:513:1)</summary>

```
  type size changed from 576 to 512 (in bits)
  2 data member deletions:
    'sg_table* sgt', at offset 256 (in bits) at dma-buf.h:517:1
    'dma_data_direction dir', at offset 320 (in bits) at dma-buf.h:518:1
  there are data member changes:
    'bool peer2peer' offset changed from 352 to 256 (in bits) (by -96 bits)
    'const dma_buf_attach_ops* importer_ops' offset changed from 384 to 320 (in bits) (by -64 bits)
    'void* importer_priv' offset changed from 448 to 384 (in bits) (by -64 bits)
    'void* priv' offset changed from 512 to 448 (in bits) (by -64 bits)
```

Reaches: `function dma_buf_attachment* dma_buf_attach(dma_buf*, device*)`, `function int dma_buf_begin_cpu_access(dma_buf*, dma_data_direction)`, `function void dma_buf_detach(dma_buf*, dma_buf_attachment*)`, `function dma_buf_attachment* dma_buf_dynamic_attach(dma_buf*, device*, const dma_buf_attach_ops*, void*)`, `function int dma_buf_end_cpu_access(dma_buf*, dma_data_direction)`, `function dma_buf* dma_buf_export(const dma_buf_export_info*)`, `function dma_buf* dma_buf_get(int)`, `function sg_table* dma_buf_map_attachment(dma_buf_attachment*, dma_data_direction)`, `function sg_table* dma_buf_map_attachment_unlocked(dma_buf_attachment*, dma_data_direction)`, `function void dma_buf_move_notify(dma_buf*)`, `function int dma_buf_pin(dma_buf_attachment*)`, `function void dma_buf_put(dma_buf*)`, `function void dma_buf_unmap_attachment(dma_buf_attachment*, sg_table*, dma_data_direction)`, `function void dma_buf_unmap_attachment_unlocked(dma_buf_attachment*, sg_table*, dma_data_direction)`, `function void dma_buf_unpin(dma_buf_attachment*)`

</details>

<details><summary><code>struct dma_buf_ops</code> (dma-buf.h:36:1)</summary>

```
  type size changed from 832 to 768 (in bits)
  1 data member deletion:
    'bool cache_sgt_mapping', at offset 0 (in bits) at dma-buf.h:44:1
  there are data member changes:
    'int (dma_buf*, dma_buf_attachment*)* attach' offset changed from 64 to 0 (in bits) (by -64 bits)
    'void (dma_buf*, dma_buf_attachment*)* detach' offset changed from 128 to 64 (in bits) (by -64 bits)
    'int (dma_buf_attachment*)* pin' offset changed from 192 to 128 (in bits) (by -64 bits)
    'void (dma_buf_attachment*)* unpin' offset changed from 256 to 192 (in bits) (by -64 bits)
    'sg_table* (dma_buf_attachment*, enum dma_data_direction)* map_dma_buf' offset changed from 320 to 256 (in bits) (by -64 bits)
    'void (dma_buf_attachment*, sg_table*, enum dma_data_direction)* unmap_dma_buf' offset changed from 384 to 320 (in bits) (by -64 bits)
    'void (dma_buf*)* release' offset changed from 448 to 384 (in bits) (by -64 bits)
    'int (dma_buf*, enum dma_data_direction)* begin_cpu_access' offset changed from 512 to 448 (in bits) (by -64 bits)
    'int (dma_buf*, enum dma_data_direction)* end_cpu_access' offset changed from 576 to 512 (in bits) (by -64 bits)
    'int (dma_buf*, vm_area_struct*)* mmap' offset changed from 640 to 576 (in bits) (by -64 bits)
    'int (dma_buf*, iosys_map*)* vmap' offset changed from 704 to 640 (in bits) (by -64 bits)
    'void (dma_buf*, iosys_map*)* vunmap' offset changed from 768 to 704 (in bits) (by -64 bits)
```

Reaches: `function dma_buf_attachment* dma_buf_attach(dma_buf*, device*)`, `function int dma_buf_begin_cpu_access(dma_buf*, dma_data_direction)`, `function void dma_buf_detach(dma_buf*, dma_buf_attachment*)`, `function dma_buf_attachment* dma_buf_dynamic_attach(dma_buf*, device*, const dma_buf_attach_ops*, void*)`, `function int dma_buf_end_cpu_access(dma_buf*, dma_data_direction)`, `function dma_buf* dma_buf_export(const dma_buf_export_info*)`, `function dma_buf* dma_buf_get(int)`, `function sg_table* dma_buf_map_attachment(dma_buf_attachment*, dma_data_direction)`, `function sg_table* dma_buf_map_attachment_unlocked(dma_buf_attachment*, dma_data_direction)`, `function void dma_buf_move_notify(dma_buf*)`, `function int dma_buf_pin(dma_buf_attachment*)`, `function void dma_buf_put(dma_buf*)`, `function void dma_buf_unmap_attachment(dma_buf_attachment*, sg_table*, dma_data_direction)`, `function void dma_buf_unmap_attachment_unlocked(dma_buf_attachment*, sg_table*, dma_data_direction)`, `function void dma_buf_unpin(dma_buf_attachment*)`

</details>

<details><summary><code>struct ieee80211_bss_conf</code> (mac80211.h:758:1)</summary>

```
  type size changed from 6976 to 7104 (in bits)
  2 data member insertions:
    'ieee80211_bss_conf* tx_bss_conf', at offset 2496 (in bits) at mac80211.h:811:1
    'bool eht_disable_mcs15', at offset 7048 (in bits) at mac80211.h:856:1
  there are data member changes:
    'u8 transmitter_bssid[6]' offset changed from 2440 to 2560 (in bits) (by +120 bits)
    'u8 bssid_index' offset changed from 2488 to 2608 (in bits) (by +120 bits)
    'u8 bssid_indicator' offset changed from 2496 to 2616 (in bits) (by +120 bits)
    'bool ema_ap' offset changed from 2504 to 2624 (in bits) (by +120 bits)
    'u8 profile_periodicity' offset changed from 2512 to 2632 (in bits) (by +120 bits)
    'struct {u32 params; u16 nss_set;} he_oper' offset changed from 2528 to 2656 (in bits) (by +128 bits)
    'ieee80211_he_obss_pd he_obss_pd' offset changed from 2592 to 2720 (in bits) (by +128 bits)
    'cfg80211_he_bss_color he_bss_color' offset changed from 2760 to 2888 (in bits) (by +128 bits)
    'ieee80211_fils_discovery fils_discovery' offset changed from 2784 to 2912 (in bits) (by +128 bits)
    'u32 unsol_bcast_probe_resp_interval' offset changed from 2848 to 2976 (in bits) (by +128 bits)
    'cfg80211_bitrate_mask beacon_tx_rate' offset changed from 2880 to 3008 (in bits) (by +128 bits)
    'ieee80211_ap_reg_power power_type' offset changed from 5760 to 5888 (in bits) (by +128 bits)
    'ieee80211_parsed_tpe tpe' offset changed from 5792 to 5920 (in bits) (by +128 bits)
    'u8 pwr_reduction' offset changed from 6624 to 6752 (in bits) (by +128 bits)
    'bool eht_support' offset changed from 6632 to 6760 (in bits) (by +128 bits)
    'bool epcs_support' offset changed from 6640 to 6768 (in bits) (by +128 bits)
    'bool csa_active' offset changed from 6648 to 6776 (in bits) (by +128 bits)
    'bool mu_mimo_owner' offset changed from 6656 to 6784 (in bits) (by +128 bits)
    'ieee80211_chanctx_conf* chanctx_conf' offset changed from 6720 to 6848 (in bits) (by +128 bits)
    'bool color_change_active' offset changed from 6784 to 6912 (in bits) (by +128 bits)
    'u8 color_change_color' offset changed from 6792 to 6920 (in bits) (by +128 bits)
    'bool ht_ldpc' offset changed from 6800 to 6928 (in bits) (by +128 bits)
    'bool vht_ldpc' offset changed from 6808 to 6936 (in bits) (by +128 bits)
    'bool he_ldpc' offset changed from 6816 to 6944 (in bits) (by +128 bits)
    'bool vht_su_beamformer' offset changed from 6824 to 6952 (in bits) (by +128 bits)
    'bool vht_su_beamformee' offset changed from 6832 to 6960 (in bits) (by +128 bits)
    'bool vht_mu_beamformer' offset changed from 6840 to 6968 (in bits) (by +128 bits)
    'bool vht_mu_beamformee' offset changed from 6848 to 6976 (in bits) (by +128 bits)
    'bool he_su_beamformer' offset changed from 6856 to 6984 (in bits) (by +128 bits)
    'bool he_su_beamformee' offset changed from 6864 to 6992 (in bits) (by +128 bits)
    'bool he_mu_beamformer' offset changed from 6872 to 7000 (in bits) (by +128 bits)
    'bool he_full_ul_mumimo' offset changed from 6880 to 7008 (in bits) (by +128 bits)
    'bool eht_su_beamformer' offset changed from 6888 to 7016 (in bits) (by +128 bits)
    'bool eht_su_beamformee' offset changed from 6896 to 7024 (in bits) (by +128 bits)
    'bool eht_mu_beamformer' offset changed from 6904 to 7032 (in bits) (by +128 bits)
  ...
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function void ieee80211_beacon_set_cntdwn(ieee80211_vif*, u8)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_channel_switch_disconnect(ieee80211_vif*)`, `function void ieee80211_chswitch_done(ieee80211_vif*, bool, unsigned int)`, `function void ieee80211_color_change_finish(ieee80211_vif*, u8)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_cqm_beacon_loss_notify(ieee80211_vif*, gfp_t)`, `function void ieee80211_cqm_rssi_notify(ieee80211_vif*, nl80211_cqm_rssi_threshold_event, s32, gfp_t)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)` … (+62 more)

</details>

<details><summary><code>struct ieee80211_sta</code> (mac80211.h:2511:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u16 eml_cap', at offset 240 (in bits) at mac80211.h:2530:1
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function void ieee80211_beacon_set_cntdwn(ieee80211_vif*, u8)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_channel_switch_disconnect(ieee80211_vif*)`, `function void ieee80211_chswitch_done(ieee80211_vif*, bool, unsigned int)`, `function void ieee80211_color_change_finish(ieee80211_vif*, u8)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_cqm_beacon_loss_notify(ieee80211_vif*, gfp_t)`, `function void ieee80211_cqm_rssi_notify(ieee80211_vif*, nl80211_cqm_rssi_threshold_event, s32, gfp_t)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)` … (+62 more)

</details>

<details><summary><code>struct ieee80211_vif</code> (mac80211.h:2028:1)</summary>

```
  type size changed from 9408 to 9472 (in bits)
  1 data member deletion:
    'ieee80211_vif* mbssid_tx_vif', at offset 9344 (in bits) at mac80211.h:2055:1
  there are data member changes:
    type 'struct ieee80211_bss_conf' of 'ieee80211_vif::bss_conf' changed, as reported earlier
    'ieee80211_bss_conf* link_conf[15]' offset changed from 7680 to 7808 (in bits) (by +128 bits)
    'u16 valid_links' offset changed from 8640 to 8768 (in bits) (by +128 bits)
    'u16 active_links' offset changed from 8656 to 8784 (in bits) (by +128 bits)
    'u16 dormant_links' offset changed from 8672 to 8800 (in bits) (by +128 bits)
    'u16 suspended_links' offset changed from 8688 to 8816 (in bits) (by +128 bits)
    'ieee80211_neg_ttlm neg_ttlm' offset changed from 8704 to 8832 (in bits) (by +128 bits)
    'u8 addr[6]' offset changed from 8976 to 9104 (in bits) (by +128 bits)
    'bool addr_valid' offset changed from 9024 to 9152 (in bits) (by +128 bits)
    'bool p2p' offset changed from 9032 to 9160 (in bits) (by +128 bits)
    'u8 cab_queue' offset changed from 9040 to 9168 (in bits) (by +128 bits)
    'u8 hw_queue[4]' offset changed from 9048 to 9176 (in bits) (by +128 bits)
    'ieee80211_txq* txq' offset changed from 9088 to 9216 (in bits) (by +128 bits)
    'netdev_features_t netdev_features' offset changed from 9152 to 9280 (in bits) (by +128 bits)
    'u32 driver_flags' offset changed from 9216 to 9344 (in bits) (by +128 bits)
    'u32 offload_flags' offset changed from 9248 to 9376 (in bits) (by +128 bits)
    'bool probe_req_reg' offset changed from 9280 to 9408 (in bits) (by +128 bits)
    'bool rx_mcast_action_reg' offset changed from 9288 to 9416 (in bits) (by +128 bits)
    'u8 drv_priv[]' offset changed from 9408 to 9472 (in bits) (by +64 bits)
```

Reaches: `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function void ieee80211_beacon_set_cntdwn(ieee80211_vif*, u8)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_channel_switch_disconnect(ieee80211_vif*)`, `function void ieee80211_chswitch_done(ieee80211_vif*, bool, unsigned int)`, `function void ieee80211_color_change_finish(ieee80211_vif*, u8)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_cqm_beacon_loss_notify(ieee80211_vif*, gfp_t)`, `function void ieee80211_cqm_rssi_notify(ieee80211_vif*, nl80211_cqm_rssi_threshold_event, s32, gfp_t)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)` … (+62 more)

</details>

<details><summary><code>struct pci_dev</code> (pci.h:332:1)</summary>

```
  type size changed from 16768 to 16704 (in bits)
  1 data member deletion:
    'bool match_driver', at offset 13504 (in bits) at pci.h:428:1
  there are data member changes:
    'unsigned int transparent' offset changed from 13512 to 13504 (in bits) (by -8 bits)
    'unsigned int io_window' offset changed from 13513 to 13505 (in bits) (by -8 bits)
    'unsigned int pref_window' offset changed from 13514 to 13506 (in bits) (by -8 bits)
    'unsigned int pref_64_window' offset changed from 13515 to 13507 (in bits) (by -8 bits)
    'unsigned int multifunction' offset changed from 13516 to 13508 (in bits) (by -8 bits)
    'unsigned int is_busmaster' offset changed from 13517 to 13509 (in bits) (by -8 bits)
    'unsigned int no_msi' offset changed from 13518 to 13510 (in bits) (by -8 bits)
    'unsigned int no_64bit_msi' offset changed from 13519 to 13511 (in bits) (by -8 bits)
    'unsigned int block_cfg_access' offset changed from 13520 to 13512 (in bits) (by -8 bits)
    'unsigned int broken_parity_status' offset changed from 13521 to 13513 (in bits) (by -8 bits)
    'unsigned int irq_reroute_variant' offset changed from 13522 to 13514 (in bits) (by -8 bits)
    'unsigned int msi_enabled' offset changed from 13524 to 13516 (in bits) (by -8 bits)
    'unsigned int msix_enabled' offset changed from 13525 to 13517 (in bits) (by -8 bits)
    'unsigned int ari_enabled' offset changed from 13526 to 13518 (in bits) (by -8 bits)
    'unsigned int ats_enabled' offset changed from 13527 to 13519 (in bits) (by -8 bits)
    'unsigned int pasid_enabled' offset changed from 13528 to 13520 (in bits) (by -8 bits)
    'unsigned int pri_enabled' offset changed from 13529 to 13521 (in bits) (by -8 bits)
    'unsigned int tph_enabled' offset changed from 13530 to 13522 (in bits) (by -8 bits)
    'unsigned int is_managed' offset changed from 13531 to 13523 (in bits) (by -8 bits)
    'unsigned int is_msi_managed' offset changed from 13532 to 13524 (in bits) (by -8 bits)
    'unsigned int needs_freset' offset changed from 13533 to 13525 (in bits) (by -8 bits)
    'unsigned int state_saved' offset changed from 13534 to 13526 (in bits) (by -8 bits)
    'unsigned int is_physfn' offset changed from 13535 to 13527 (in bits) (by -8 bits)
    'unsigned int is_virtfn' offset changed from 13536 to 13528 (in bits) (by -8 bits)
    'unsigned int is_hotplug_bridge' offset changed from 13537 to 13529 (in bits) (by -8 bits)
    'unsigned int shpc_managed' offset changed from 13538 to 13530 (in bits) (by -8 bits)
    'unsigned int is_thunderbolt' offset changed from 13539 to 13531 (in bits) (by -8 bits)
    'unsigned int untrusted' offset changed from 13540 to 13532 (in bits) (by -8 bits)
    'unsigned int external_facing' offset changed from 13541 to 13533 (in bits) (by -8 bits)
    'unsigned int broken_intx_masking' offset changed from 13542 to 13534 (in bits) (by -8 bits)
    'unsigned int io_window_1k' offset changed from 13543 to 13535 (in bits) (by -8 bits)
    'unsigned int irq_managed' offset changed from 13544 to 13536 (in bits) (by -8 bits)
    'unsigned int non_compliant_bars' offset changed from 13545 to 13537 (in bits) (by -8 bits)
    'unsigned int is_probed' offset changed from 13546 to 13538 (in bits) (by -8 bits)
    'unsigned int link_active_reporting' offset changed from 13547 to 13539 (in bits) (by -8 bits)
    'unsigned int no_vf_scan' offset changed from 13548 to 13540 (in bits) (by -8 bits)
  ...
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function agp_memory* agp_allocate_memory(agp_bridge_data*, size_t, u32)`, `function agp_bridge_data* agp_backend_acquire(pci_dev*)`, `function void agp_backend_release(agp_bridge_data*)`, `function int agp_bind_memory(agp_memory*, off_t)`, `function int agp_copy_info(agp_bridge_data*, agp_kern_info*)`, `function void agp_enable(agp_bridge_data*, u32)`, `function void agp_free_memory(agp_memory*)`, `function int agp_unbind_memory(agp_memory*)`, `function int aperture_remove_conflicting_pci_devices(pci_dev*, const char*)`, `function int intel_gmch_probe(pci_dev*, pci_dev*, agp_bridge_data*)`, `function int pci_alloc_irq_vectors(pci_dev*, unsigned int, unsigned int, unsigned int)`, `function int pci_assign_resource(pci_dev*, int)`, `function void pci_assign_unassigned_bus_resources(pci_bus*)` … (+84 more)

</details>

<details><summary><code>struct file_operations</code> (fs.h:2129:1)</summary>

```
  type size changed from 2112 to 2176 (in bits)
  1 data member insertion:
    'int (vm_area_desc*)* mmap_prepare', at offset 2112 (in bits) at fs.h:2194:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+132 more)

</details>

<details><summary><code>struct bio</code> (blk_types.h:214:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u8 bi_write_stream', at offset 200 (in bits) at blk_types.h:223:1
  there are data member changes:
    'blk_status_t bi_status' offset changed from 200 to 208 (in bits) (by +8 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct fib6_info</code> (ip6_fib.h:158:1)</summary>

```
  type size changed from 1472 to 1600 (in bits)
  1 data member insertion:
    'list_head purge_link', at offset 1280 (in bits) at ip6_fib.h:201:1
  there are data member changes:
    'callback_head rcu' offset changed from 1280 to 1408 (in bits) (by +128 bits)
    'nexthop* nh' offset changed from 1408 to 1536 (in bits) (by +128 bits)
    'fib6_nh fib6_nh[]' offset changed from 1472 to 1600 (in bits) (by +128 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct folio_queue</code> (folio_queue.h:30:1)</summary>

```
  type size changed from 2688 to 2624 (in bits)
  1 data member deletion:
    'unsigned long int marks3', at offset 2560 (in bits) at folio_queue.h:37:1
  there are data member changes:
    'unsigned int rreq_id' offset changed from 2624 to 2560 (in bits) (by -64 bits)
    'unsigned int debug_id' offset changed from 2656 to 2592 (in bits) (by -64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct gendisk</code> (blkdev.h:142:1)</summary>

```
  type size changed from 4544 to 4736 (in bits)
  1 data member deletion:
    'atomic_t sync_io', at offset 4032 (in bits) at blkdev.h:185:1
  1 data member insertion:
    'mutex rqos_state_mutex', at offset 4480 (in bits) at blkdev.h:221:1
  there are data member changes:
    'disk_events* ev' offset changed from 4096 to 4032 (in bits) (by -64 bits)
    'cdrom_device_info* cdi' offset changed from 4160 to 4096 (in bits) (by -64 bits)
    'int node_id' offset changed from 4224 to 4160 (in bits) (by -64 bits)
    'badblocks* bb' offset changed from 4288 to 4224 (in bits) (by -64 bits)
    'u64 diskseq' offset changed from 4352 to 4288 (in bits) (by -64 bits)
    'lockdep_map lockdep_map' offset changed from 4352 to 4288 (in bits) (by -64 bits)
    'blk_mode_t open_mode' offset changed from 4416 to 4352 (in bits) (by -64 bits)
    'blk_independent_access_ranges* ia_ranges' offset changed from 4480 to 4416 (in bits) (by -64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct io_ring_ctx</code> (io_uring_types.h:239:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'io_mapped_region zcrx_region', at offset 11712 (in bits) at io_uring_types.h:452:1
  2 data member insertions:
    'unsigned int nr_drained', at offset 9280 (in bits) at io_uring_types.h:419:1
    'unsigned int nr_req_allocated', at offset 10976 (in bits) at io_uring_types.h:438:1
  there are data member changes:
    anonymous data member at offset 4096 (in bits) changed from:
      struct {io_uring_cqe* cqe_cached; io_uring_cqe* cqe_sentinel; unsigned int cached_cq_tail; unsigned int cq_entries; io_ev_fd* io_ev_fd; unsigned int cq_extra; void* cq_wait_arg; size_t cq_wait_size;}
    to:
      struct {io_uring_cqe* cqe_cached; io_uring_cqe* cqe_sentinel; unsigned int cached_cq_tail; unsigned int cq_entries; io_ev_fd* io_ev_fd; void* cq_wait_arg; size_t cq_wait_size;}
    type 'io_zcrx_ifq*' of 'io_ring_ctx::ifq' changed:
      entity changed from 'io_zcrx_ifq*' to 'struct xarray' at xarray.h:300:1
      type size changed from 64 to 128 (in bits)
    and name of 'io_ring_ctx::ifq' changed to 'io_ring_ctx::zcrx_ctxs' at io_uring_types.h:395:1
    'u32 pers_next' offset changed from 7104 to 7168 (in bits) (by +64 bits)
    'xarray personalities' offset changed from 7168 to 7232 (in bits) (by +64 bits)
    'io_wq_hash* hash_map' offset changed from 7296 to 7360 (in bits) (by +64 bits)
    'user_struct* user' offset changed from 7360 to 7424 (in bits) (by +64 bits)
    'mm_struct* mm_account' offset changed from 7424 to 7488 (in bits) (by +64 bits)
    'llist_head fallback_llist' offset changed from 7488 to 7552 (in bits) (by +64 bits)
    'delayed_work fallback_work' offset changed from 7552 to 7616 (in bits) (by +64 bits)
    'work_struct exit_work' offset changed from 8256 to 8320 (in bits) (by +64 bits)
    'list_head tctx_list' offset changed from 8512 to 8576 (in bits) (by +64 bits)
    'completion ref_comp' offset changed from 8640 to 8704 (in bits) (by +64 bits)
    'u32 iowq_limits[2]' offset changed from 8896 to 8960 (in bits) (by +64 bits)
    'callback_head poll_wq_task_work' offset changed from 8960 to 9024 (in bits) (by +64 bits)
    'list_head defer_list' offset changed from 9088 to 9152 (in bits) (by +64 bits)
    'io_alloc_cache msg_cache' offset changed from 9216 to 9344 (in bits) (by +128 bits)
    'spinlock_t msg_lock' offset changed from 9408 to 9536 (in bits) (by +128 bits)
    'list_head napi_list' offset changed from 9472 to 9600 (in bits) (by +128 bits)
    'spinlock_t napi_lock' offset changed from 9600 to 9728 (in bits) (by +128 bits)
    'ktime_t napi_busy_poll_dt' offset changed from 9664 to 9792 (in bits) (by +128 bits)
    'bool napi_prefer_busy_poll' offset changed from 9728 to 9856 (in bits) (by +128 bits)
    'u8 napi_track_mode' offset changed from 9736 to 9864 (in bits) (by +128 bits)
    'hlist_head napi_ht[16]' offset changed from 9792 to 9920 (in bits) (by +128 bits)
    'unsigned int evfd_last_cq_tail' offset changed from 10816 to 10944 (in bits) (by +128 bits)
    'mutex mmap_lock' offset changed from 10880 to 11008 (in bits) (by +128 bits)
    'io_mapped_region sq_region' offset changed from 11136 to 11264 (in bits) (by +128 bits)
    'io_mapped_region ring_region' offset changed from 11328 to 11456 (in bits) (by +128 bits)
  ...
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct iommu_device</code> (iommu.h:754:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'bool ready', at offset 416 (in bits) at iommu.h:756:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct iommu_iotlb_gather</code> (iommu.h:362:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct list_head' of 'iommu_iotlb_gather::freelist' changed:
      type name changed from 'list_head' to 'iommu_pages_list'
      type size hasn't changed
      1 data member deletion:
        'list_head* prev', at offset 64 (in bits) at types.h:196:1
      there are data member changes:
        type 'list_head*' of 'list_head::next' changed:
          entity changed from 'list_head*' to 'struct list_head' at types.h:199:1
          type size changed from 64 to 128 (in bits)
        and name of 'list_head::next' changed to 'iommu_pages_list::pages' at iommu.h:333:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct iommu_ops</code> (iommu.h:627:1)</summary>

```
  type size changed from 1728 to 1600 (in bits)
  2 data member deletions:
    'int (device*, enum iommu_dev_features)* dev_enable_feat', at offset 896 (in bits) at iommu.h:655:1
    'int (device*, enum iommu_dev_features)* dev_disable_feat', at offset 960 (in bits) at iommu.h:656:1
  there are data member changes:
    type 'iommu_domain* (unsigned int)*' of 'iommu_ops::domain_alloc' changed:
      pointer type changed from: 'iommu_domain* (unsigned int)*' to: 'iommu_domain* (device*)*'
    and name of 'iommu_ops::domain_alloc' changed to 'iommu_ops::domain_alloc_identity' at iommu.h:629:1
    'void (device*, iopf_fault*, iommu_page_response*)* page_response' offset changed from 1024 to 896 (in bits) (by -128 bits)
    'int (device*)* def_domain_type' offset changed from 1088 to 960 (in bits) (by -128 bits)
    'iommufd_viommu* (device*, iommu_domain*, iommufd_ctx*, unsigned int)* viommu_alloc' offset changed from 1152 to 1024 (in bits) (by -128 bits)
    'const iommu_domain_ops* default_domain_ops' offset changed from 1216 to 1088 (in bits) (by -128 bits)
    'unsigned long int pgsize_bitmap' offset changed from 1280 to 1152 (in bits) (by -128 bits)
    'module* owner' offset changed from 1344 to 1216 (in bits) (by -128 bits)
    'iommu_domain* identity_domain' offset changed from 1408 to 1280 (in bits) (by -128 bits)
    'iommu_domain* blocked_domain' offset changed from 1472 to 1344 (in bits) (by -128 bits)
    'iommu_domain* release_domain' offset changed from 1536 to 1408 (in bits) (by -128 bits)
    'iommu_domain* default_domain' offset changed from 1600 to 1472 (in bits) (by -128 bits)
    'u8 user_pasid_table' offset changed from 1664 to 1536 (in bits) (by -128 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct linux_binfmt</code> (binfmts.h:89:1)</summary>

```
  type size changed from 448 to 384 (in bits)
  1 data member deletion:
    'int (file*)* load_shlib', at offset 256 (in bits) at binfmts.h:93:1
  there are data member changes:
    'int (coredump_params*)* core_dump' offset changed from 320 to 256 (in bits) (by -64 bits)
    'unsigned long int min_coredump' offset changed from 384 to 320 (in bits) (by -64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct mnt_namespace</code> (mount.h:14:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'mntns_flags_t mntns_flags', at offset 1504 (in bits) at mount.h:40:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct msi_domain_info</code> (msi.h:491:1)</summary>

```
  type size changed from 576 to 640 (in bits)
  1 data member insertion:
    'msi_alloc_info_t* alloc_data', at offset 512 (in bits) at msi.h:509:1
  there are data member changes:
    'void* data' offset changed from 512 to 576 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct msi_domain_ops</code> (msi.h:448:1)</summary>

```
  type size changed from 640 to 704 (in bits)
  1 data member insertion:
    'void (irq_domain*, msi_alloc_info_t*)* msi_teardown', at offset 256 (in bits) at msi.h:466:1
  there are data member changes:
    'void (irq_domain*, msi_alloc_info_t*, msi_desc*)* prepare_desc' offset changed from 256 to 320 (in bits) (by +64 bits)
    'void (msi_alloc_info_t*, msi_desc*)* set_desc' offset changed from 320 to 384 (in bits) (by +64 bits)
    'int (irq_domain*, device*, int)* domain_alloc_irqs' offset changed from 384 to 448 (in bits) (by +64 bits)
    'void (irq_domain*, device*)* domain_free_irqs' offset changed from 448 to 512 (in bits) (by +64 bits)
    'void (irq_domain*, device*)* msi_post_free' offset changed from 512 to 576 (in bits) (by +64 bits)
    'int (irq_domain*, irq_fwspec*, irq_hw_number_t*, unsigned int*)* msi_translate' offset changed from 576 to 640 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct nexthop</code> (nexthop.h:142:1)</summary>

```
  type size hasn't changed
  2 data member insertions:
    'bool dead', at offset 824 (in bits) at nexthop.h:155:1
    'spinlock_t lock', at offset 832 (in bits) at nexthop.h:156:1
  there are data member changes:
    'refcount_t refcnt' offset changed from 832 to 864 (in bits) (by +32 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct page_pool</code> (types.h:162:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'xarray dma_mapped', at offset 12416 (in bits) at types.h:228:1
  there are data member changes:
    'atomic_t pages_state_release_cnt' offset changed from 12416 to 12544 (in bits) (by +128 bits)
    'refcount_t user_cnt' offset changed from 12448 to 12576 (in bits) (by +128 bits)
    'u64 destroy_cnt' offset changed from 12480 to 12608 (in bits) (by +128 bits)
    'page_pool_params_slow slow' offset changed from 12544 to 12672 (in bits) (by +128 bits)
    'struct {hlist_node list; u64 detach_time; u32 id;} user' offset changed from 12800 to 12928 (in bits) (by +128 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct per_cpu_zonestat</code> (mmzone.h:728:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 's8[11]' of 'per_cpu_zonestat::vm_stat_diff' changed:
      type name changed from 's8[11]' to 's8[10]'
      array type size changed from 88 to 80
      array type subrange 1 changed length from 11 to 10
    's8 stat_threshold' offset changed from 88 to 80 (in bits) (by -8 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct pglist_data</code> (mmzone.h:1341:1)</summary>

```
  type size changed from 114688 to 112640 (in bits)
  there are data member changes:
    'zone node_zones[4]' size changed from 40960 to 38912 (in bits) (by -2048 bits)
    'zonelist node_zonelists[2]' offset changed from 40960 to 38912 (in bits) (by -2048 bits)
    'int nr_zones' offset changed from 106752 to 104704 (in bits) (by -2048 bits)
    'unsigned long int node_start_pfn' offset changed from 106816 to 104768 (in bits) (by -2048 bits)
    'unsigned long int node_present_pages' offset changed from 106880 to 104832 (in bits) (by -2048 bits)
    'unsigned long int node_spanned_pages' offset changed from 106944 to 104896 (in bits) (by -2048 bits)
    'int node_id' offset changed from 107008 to 104960 (in bits) (by -2048 bits)
    'wait_queue_head_t kswapd_wait' offset changed from 107072 to 105024 (in bits) (by -2048 bits)
    'wait_queue_head_t pfmemalloc_wait' offset changed from 107264 to 105216 (in bits) (by -2048 bits)
    'wait_queue_head_t reclaim_wait[4]' offset changed from 107456 to 105408 (in bits) (by -2048 bits)
    'atomic_t nr_writeback_throttled' offset changed from 108224 to 106176 (in bits) (by -2048 bits)
    'unsigned long int nr_reclaim_start' offset changed from 108288 to 106240 (in bits) (by -2048 bits)
    'task_struct* kswapd' offset changed from 108352 to 106304 (in bits) (by -2048 bits)
    'int kswapd_order' offset changed from 108416 to 106368 (in bits) (by -2048 bits)
    'zone_type kswapd_highest_zoneidx' offset changed from 108448 to 106400 (in bits) (by -2048 bits)
    'int kswapd_failures' offset changed from 108480 to 106432 (in bits) (by -2048 bits)
    'int kcompactd_max_order' offset changed from 108512 to 106464 (in bits) (by -2048 bits)
    'zone_type kcompactd_highest_zoneidx' offset changed from 108544 to 106496 (in bits) (by -2048 bits)
    'wait_queue_head_t kcompactd_wait' offset changed from 108608 to 106560 (in bits) (by -2048 bits)
    'task_struct* kcompactd' offset changed from 108800 to 106752 (in bits) (by -2048 bits)
    'bool proactive_compact_trigger' offset changed from 108864 to 106816 (in bits) (by -2048 bits)
    'unsigned long int totalreserve_pages' offset changed from 108928 to 106880 (in bits) (by -2048 bits)
    'unsigned long int min_unmapped_pages' offset changed from 108992 to 106944 (in bits) (by -2048 bits)
    'unsigned long int min_slab_pages' offset changed from 109056 to 107008 (in bits) (by -2048 bits)
    'lruvec __lruvec' offset changed from 109568 to 107520 (in bits) (by -2048 bits)
    'cacheline_padding _pad1_' offset changed from 109568 to 107520 (in bits) (by -2048 bits)
    'unsigned long int flags' offset changed from 110656 to 108608 (in bits) (by -2048 bits)
    'cacheline_padding _pad2_' offset changed from 111104 to 109056 (in bits) (by -2048 bits)
    'per_cpu_nodestat* per_cpu_nodestats' offset changed from 111104 to 109056 (in bits) (by -2048 bits)
    'atomic_long_t vm_stat[48]' offset changed from 111168 to 109120 (in bits) (by -2048 bits)
    'memory_tier* memtier' offset changed from 114240 to 112192 (in bits) (by -2048 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct phy_driver</code> (phy.h:898:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int (phy_device*)*' of 'phy_driver::match_phy_device' changed:
      pointer type changed from: 'int (phy_device*)*' to: 'int (phy_device*, const phy_driver*)*'
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct queue_limits</code> (blkdev.h:365:1)</summary>

```
  type size changed from 1408 to 1472 (in bits)
  2 data member insertions:
    'unsigned short int max_write_streams', at offset 1200 (in bits) at blkdev.h:411:1
    'unsigned int write_stream_granularity', at offset 1216 (in bits) at blkdev.h:412:1
  there are data member changes:
    'unsigned int max_open_zones' offset changed from 1216 to 1248 (in bits) (by +32 bits)
    'unsigned int max_active_zones' offset changed from 1248 to 1280 (in bits) (by +32 bits)
    'unsigned int dma_alignment' offset changed from 1280 to 1312 (in bits) (by +32 bits)
    'unsigned int dma_pad_mask' offset changed from 1312 to 1344 (in bits) (by +32 bits)
    'blk_integrity integrity' offset changed from 1344 to 1376 (in bits) (by +32 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct request_queue</code> (blkdev.h:459:1)</summary>

```
  type size changed from 7680 to 7744 (in bits)
  there are data member changes:
    type 'struct queue_limits' of 'request_queue::limits' changed, as reported earlier
    'device* dev' offset changed from 2368 to 2432 (in bits) (by +64 bits)
    'rpm_status rpm_status' offset changed from 2432 to 2496 (in bits) (by +64 bits)
    'atomic_t pm_only' offset changed from 2464 to 2528 (in bits) (by +64 bits)
    'blk_queue_stats* stats' offset changed from 2496 to 2560 (in bits) (by +64 bits)
    'rq_qos* rq_qos' offset changed from 2560 to 2624 (in bits) (by +64 bits)
    'mutex rq_qos_mutex' offset changed from 2624 to 2688 (in bits) (by +64 bits)
    'int id' offset changed from 2880 to 2944 (in bits) (by +64 bits)
    'unsigned long int nr_requests' offset changed from 2944 to 3008 (in bits) (by +64 bits)
    'timer_list timeout' offset changed from 3008 to 3072 (in bits) (by +64 bits)
    'work_struct timeout_work' offset changed from 3328 to 3392 (in bits) (by +64 bits)
    'atomic_t nr_active_requests_shared_tags' offset changed from 3584 to 3648 (in bits) (by +64 bits)
    'blk_mq_tags* sched_shared_tags' offset changed from 3648 to 3712 (in bits) (by +64 bits)
    'list_head icq_list' offset changed from 3712 to 3776 (in bits) (by +64 bits)
    'unsigned long int blkcg_pols[1]' offset changed from 3840 to 3904 (in bits) (by +64 bits)
    'blkcg_gq* root_blkg' offset changed from 3904 to 3968 (in bits) (by +64 bits)
    'list_head blkg_list' offset changed from 3968 to 4032 (in bits) (by +64 bits)
    'mutex blkcg_mutex' offset changed from 4096 to 4160 (in bits) (by +64 bits)
    'int node' offset changed from 4352 to 4416 (in bits) (by +64 bits)
    'spinlock_t requeue_lock' offset changed from 4384 to 4448 (in bits) (by +64 bits)
    'list_head requeue_list' offset changed from 4416 to 4480 (in bits) (by +64 bits)
    'delayed_work requeue_work' offset changed from 4544 to 4608 (in bits) (by +64 bits)
    'blk_trace* blk_trace' offset changed from 5248 to 5312 (in bits) (by +64 bits)
    'blk_flush_queue* fq' offset changed from 5312 to 5376 (in bits) (by +64 bits)
    'list_head flush_list' offset changed from 5376 to 5440 (in bits) (by +64 bits)
    'mutex elevator_lock' offset changed from 5504 to 5568 (in bits) (by +64 bits)
    'mutex sysfs_lock' offset changed from 5760 to 5824 (in bits) (by +64 bits)
    'mutex limits_lock' offset changed from 6016 to 6080 (in bits) (by +64 bits)
    'list_head unused_hctx_list' offset changed from 6272 to 6336 (in bits) (by +64 bits)
    'spinlock_t unused_hctx_lock' offset changed from 6400 to 6464 (in bits) (by +64 bits)
    'int mq_freeze_depth' offset changed from 6432 to 6496 (in bits) (by +64 bits)
    'callback_head callback_head' offset changed from 6464 to 6528 (in bits) (by +64 bits)
    'wait_queue_head_t mq_freeze_wq' offset changed from 6592 to 6656 (in bits) (by +64 bits)
    'mutex mq_freeze_lock' offset changed from 6784 to 6848 (in bits) (by +64 bits)
    'blk_mq_tag_set* tag_set' offset changed from 7040 to 7104 (in bits) (by +64 bits)
    'list_head tag_set_list' offset changed from 7104 to 7168 (in bits) (by +64 bits)
    'dentry* debugfs_dir' offset changed from 7232 to 7296 (in bits) (by +64 bits)
    'dentry* sched_debugfs_dir' offset changed from 7296 to 7360 (in bits) (by +64 bits)
  ...
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct rq</code> (sched.h:1097:1)</summary>

```
  type size changed from 26112 to 26624 (in bits)
  there are data member changes:
    type 'struct rt_rq' of 'rq::rt' changed:
      type size changed from 13312 to 13376 (in bits)
      1 data member insertion:
        'task_group* tg', at offset 13312 (in bits) at sched.h:826:1
    'dl_rq dl' offset changed from 17408 to 17472 (in bits) (by +64 bits)
    'sched_dl_entity fair_server' offset changed from 18240 to 18304 (in bits) (by +64 bits)
    'list_head leaf_cfs_rq_list' offset changed from 20224 to 20288 (in bits) (by +64 bits)
    'list_head* tmp_alone_branch' offset changed from 20352 to 20416 (in bits) (by +64 bits)
    type 'unsigned int' of 'rq::nr_uninterruptible' changed:
      type name changed from 'unsigned int' to 'unsigned long int'
      type size changed from 32 to 64 (in bits)
    and offset changed from 20416 to 20480 (in bits) (by +64 bits)
    anonymous data member 'union {task_struct* donor; task_struct* curr;}' offset changed from 20480 to 20544 (in bits) (by +64 bits)
    'sched_dl_entity* dl_server' offset changed from 20544 to 20608 (in bits) (by +64 bits)
    'task_struct* idle' offset changed from 20608 to 20672 (in bits) (by +64 bits)
    'task_struct* stop' offset changed from 20672 to 20736 (in bits) (by +64 bits)
    'unsigned long int next_balance' offset changed from 20736 to 20800 (in bits) (by +64 bits)
    'mm_struct* prev_mm' offset changed from 20800 to 20864 (in bits) (by +64 bits)
    'unsigned int clock_update_flags' offset changed from 20864 to 20928 (in bits) (by +64 bits)
    'u64 clock' offset changed from 20928 to 20992 (in bits) (by +64 bits)
    'u64 clock_task' offset changed from 20992 to 21504 (in bits) (by +512 bits)
    'u64 clock_pelt' offset changed from 21056 to 21568 (in bits) (by +512 bits)
    'unsigned long int lost_idle_time' offset changed from 21120 to 21632 (in bits) (by +512 bits)
    'u64 clock_pelt_idle' offset changed from 21184 to 21696 (in bits) (by +512 bits)
    'u64 clock_idle' offset changed from 21248 to 21760 (in bits) (by +512 bits)
    'atomic_t nr_iowait' offset changed from 21312 to 21824 (in bits) (by +512 bits)
    'u64 last_seen_need_resched_ns' offset changed from 21376 to 21888 (in bits) (by +512 bits)
    'int ticks_without_resched' offset changed from 21440 to 21952 (in bits) (by +512 bits)
    'int membarrier_state' offset changed from 21472 to 21984 (in bits) (by +512 bits)
    'root_domain* rd' offset changed from 21504 to 22016 (in bits) (by +512 bits)
    'sched_domain* sd' offset changed from 21568 to 22080 (in bits) (by +512 bits)
    'unsigned long int cpu_capacity' offset changed from 21632 to 22144 (in bits) (by +512 bits)
    'balance_callback* balance_callback' offset changed from 21696 to 22208 (in bits) (by +512 bits)
    'unsigned char nohz_idle_balance' offset changed from 21760 to 22272 (in bits) (by +512 bits)
    'unsigned char idle_balance' offset changed from 21768 to 22280 (in bits) (by +512 bits)
    'unsigned long int misfit_task_load' offset changed from 21824 to 22336 (in bits) (by +512 bits)
    'int active_balance' offset changed from 21888 to 22400 (in bits) (by +512 bits)
    'int push_cpu' offset changed from 21920 to 22432 (in bits) (by +512 bits)
  ...
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct task_group</code> (sched.h:431:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cgroup_subsys_state' of 'task_group::css' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct trace_array</code> (trace.h:326:1)</summary>

```
  type size changed from 3328 to 3456 (in bits)
  1 data member insertion:
    'list_head marker_list', at offset 2624 (in bits) at trace.h:406:1
  there are data member changes:
    'trace_event_file* trace_marker_file' offset changed from 2624 to 2752 (in bits) (by +128 bits)
    'cpumask_var_t tracing_cpumask' offset changed from 2688 to 2816 (in bits) (by +128 bits)
    'cpumask_var_t pipe_cpumask' offset changed from 2752 to 2880 (in bits) (by +128 bits)
    'int ref' offset changed from 2816 to 2944 (in bits) (by +128 bits)
    'int trace_ref' offset changed from 2848 to 2976 (in bits) (by +128 bits)
    'list_head mod_events' offset changed from 2880 to 3008 (in bits) (by +128 bits)
    'int no_filter_buffering_ref' offset changed from 3008 to 3136 (in bits) (by +128 bits)
    'list_head hist_vars' offset changed from 3072 to 3200 (in bits) (by +128 bits)
    'trace_func_repeats* last_func_repeats' offset changed from 3200 to 3328 (in bits) (by +128 bits)
    'bool ring_buffer_expanded' offset changed from 3264 to 3392 (in bits) (by +128 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct trace_array_cpu</code> (trace.h:185:1)</summary>

```
  type size changed from 1024 to 960 (in bits)
  1 data member deletion:
    'void* buffer_page', at offset 64 (in bits) at trace.h:187:1
  there are data member changes:
    type 'typedef atomic_t' of 'trace_array_cpu::disabled' changed:
      typedef name changed from atomic_t to local_t at local.h:12:1
      underlying type 'struct atomic_t' at types.h:177:1 changed:
        type name changed from 'atomic_t' to 'local_t'
        type size changed from 32 to 64 (in bits)
        there are data member changes:
          type 'int' of 'atomic_t::counter' changed:
            entity changed from 'int' to 'typedef atomic_long_t' at atomic-long.h:13:1
            type size changed from 32 to 64 (in bits)
          and name of 'atomic_t::counter' changed to 'local_t::a' at local.h:11:1
    'unsigned long int entries' offset changed from 128 to 64 (in bits) (by -64 bits)
    'unsigned long int saved_latency' offset changed from 192 to 128 (in bits) (by -64 bits)
    'unsigned long int critical_start' offset changed from 256 to 192 (in bits) (by -64 bits)
    'unsigned long int critical_end' offset changed from 320 to 256 (in bits) (by -64 bits)
    'unsigned long int critical_sequence' offset changed from 384 to 320 (in bits) (by -64 bits)
    'unsigned long int nice' offset changed from 448 to 384 (in bits) (by -64 bits)
    'unsigned long int policy' offset changed from 512 to 448 (in bits) (by -64 bits)
    'unsigned long int rt_priority' offset changed from 576 to 512 (in bits) (by -64 bits)
    'unsigned long int skipped_entries' offset changed from 640 to 576 (in bits) (by -64 bits)
    'u64 preempt_timestamp' offset changed from 704 to 640 (in bits) (by -64 bits)
    'pid_t pid' offset changed from 768 to 704 (in bits) (by -64 bits)
    'kuid_t uid' offset changed from 800 to 736 (in bits) (by -64 bits)
    'char comm[16]' offset changed from 832 to 768 (in bits) (by -64 bits)
    'bool ignore_pid' offset changed from 960 to 896 (in bits) (by -64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>struct zone</code> (mmzone.h:845:1)</summary>

```
  type size changed from 10240 to 9728 (in bits)
  there are data member changes:
    type 'atomic_long_t[11]' of 'zone::vm_stat' changed:
      type name changed from 'atomic_long_t[11]' to 'atomic_long_t[10]'
      array type size changed from 704 to 640
      array type subrange 1 changed length from 11 to 10
    'atomic_long_t vm_numa_event[6]' offset changed from 9408 to 9344 (in bits) (by -64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function sk_buff* __alloc_skb(unsigned int, gfp_t, int, int)` … (+572 more)

</details>

<details><summary><code>enum perf_event_state</code> (perf_event.h:624:1)</summary>

```
  type size hasn't changed
  1 enumerator insertion:
    'perf_event_state::PERF_EVENT_STATE_REVOKED' value '-4'
  1 enumerator change:
    'perf_event_state::PERF_EVENT_STATE_DEAD' from value '-4' to '-5' at perf_event.h:679:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+587 more)

</details>

<details><summary><code>struct hw_perf_event</code> (perf_event.h:155:1)</summary>

```
  type size changed from 1536 to 1664 (in bits)
  there are data member changes:
    anonymous data member at offset 0 (in bits) changed from:
      union {struct {u64 config; u64 last_tag; unsigned long int config_base; unsigned long int event_base; int event_base_rdpmc; int idx; int last_cpu; int flags; hw_perf_event_extra extra_reg; hw_perf_event_extra branch_reg;}; struct {u64 aux_config; unsigned int aux_paused;}; struct {hrtimer hrtimer;}; struct {list_head tp_list;}; struct {u64 pwr_acc; u64 ptsc;}; struct {arch_hw_breakpoint info; rhlist_head bp_list;}; struct {u8 iommu_bank; u8 iommu_cntr; u16 padding; u64 conf; u64 conf1;};}
    to:
      union {struct {u64 config; u64 config1; u64 last_tag; u64 dyn_constraint; unsigned long int config_base; unsigned long int event_base; int event_base_rdpmc; int idx; int last_cpu; int flags; hw_perf_event_extra extra_reg; hw_perf_event_extra branch_reg;}; struct {u64 aux_config; unsigned int aux_paused;}; struct {hrtimer hrtimer;}; struct {list_head tp_list;}; struct {u64 pwr_acc; u64 ptsc;}; struct {arch_hw_breakpoint info; rhlist_head bp_list;}; struct {u8 iommu_bank; u8 iommu_cntr; u16 padding; u64 conf; u64 conf1;};}
    and size changed from 768 to 896 (in bits) (by +128 bits)
    'task_struct* target' offset changed from 768 to 896 (in bits) (by +128 bits)
    'void* addr_filters' offset changed from 832 to 960 (in bits) (by +128 bits)
    'unsigned long int addr_filters_gen' offset changed from 896 to 1024 (in bits) (by +128 bits)
    'int state' offset changed from 960 to 1088 (in bits) (by +128 bits)
    'local64_t prev_count' offset changed from 1024 to 1152 (in bits) (by +128 bits)
    'u64 sample_period' offset changed from 1088 to 1216 (in bits) (by +128 bits)
    anonymous data member 'union {struct {u64 last_period; local64_t period_left;}; struct {u64 saved_metric; u64 saved_slots;};}' offset changed from 1152 to 1280 (in bits) (by +128 bits)
    'u64 interrupts_seq' offset changed from 1280 to 1408 (in bits) (by +128 bits)
    'u64 interrupts' offset changed from 1344 to 1472 (in bits) (by +128 bits)
    'u64 freq_time_stamp' offset changed from 1408 to 1536 (in bits) (by +128 bits)
    'u64 freq_count_stamp' offset changed from 1472 to 1600 (in bits) (by +128 bits)
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+587 more)

</details>

<details><summary><code>struct perf_cgroup</code> (perf_event.h:1123:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cgroup_subsys_state' of 'perf_cgroup::css' changed, as reported earlier
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+587 more)

</details>

<details><summary><code>struct perf_event</code> (perf_event.h:708:1)</summary>

```
  type size changed from 8768 to 9024 (in bits)
  1 data member insertion:
    'list_head pmu_list', at offset 8832 (in bits) at perf_event.h:924:1
  there are data member changes:
    type 'struct hw_perf_event' of 'perf_event::hw' changed, as reported earlier
    'perf_event_context* ctx' offset changed from 4416 to 4544 (in bits) (by +128 bits)
    'perf_event_pmu_context* pmu_ctx' offset changed from 4480 to 4608 (in bits) (by +128 bits)
    'atomic_long_t refcount' offset changed from 4544 to 4672 (in bits) (by +128 bits)
    'atomic64_t child_total_time_enabled' offset changed from 4608 to 4736 (in bits) (by +128 bits)
    'atomic64_t child_total_time_running' offset changed from 4672 to 4800 (in bits) (by +128 bits)
    'mutex child_mutex' offset changed from 4736 to 4864 (in bits) (by +128 bits)
    'list_head child_list' offset changed from 4992 to 5120 (in bits) (by +128 bits)
    'perf_event* parent' offset changed from 5120 to 5248 (in bits) (by +128 bits)
    'int oncpu' offset changed from 5184 to 5312 (in bits) (by +128 bits)
    'int cpu' offset changed from 5216 to 5344 (in bits) (by +128 bits)
    'list_head owner_entry' offset changed from 5248 to 5376 (in bits) (by +128 bits)
    'task_struct* owner' offset changed from 5376 to 5504 (in bits) (by +128 bits)
    'mutex mmap_mutex' offset changed from 5440 to 5568 (in bits) (by +128 bits)
    'atomic_t mmap_count' offset changed from 5696 to 5824 (in bits) (by +128 bits)
    'perf_buffer* rb' offset changed from 5760 to 5888 (in bits) (by +128 bits)
    'list_head rb_entry' offset changed from 5824 to 5952 (in bits) (by +128 bits)
    'unsigned long int rcu_batches' offset changed from 5952 to 6080 (in bits) (by +128 bits)
    'int rcu_pending' offset changed from 6016 to 6144 (in bits) (by +128 bits)
    'wait_queue_head_t waitq' offset changed from 6080 to 6208 (in bits) (by +128 bits)
    'fasync_struct* fasync' offset changed from 6272 to 6400 (in bits) (by +128 bits)
    'unsigned int pending_wakeup' offset changed from 6336 to 6464 (in bits) (by +128 bits)
    'unsigned int pending_kill' offset changed from 6368 to 6496 (in bits) (by +128 bits)
    'unsigned int pending_disable' offset changed from 6400 to 6528 (in bits) (by +128 bits)
    'unsigned long int pending_addr' offset changed from 6464 to 6592 (in bits) (by +128 bits)
    'irq_work pending_irq' offset changed from 6528 to 6656 (in bits) (by +128 bits)
    'irq_work pending_disable_irq' offset changed from 6784 to 6912 (in bits) (by +128 bits)
    'callback_head pending_task' offset changed from 7040 to 7168 (in bits) (by +128 bits)
    'unsigned int pending_work' offset changed from 7168 to 7296 (in bits) (by +128 bits)
    'atomic_t event_limit' offset changed from 7200 to 7328 (in bits) (by +128 bits)
    'perf_addr_filters_head addr_filters' offset changed from 7232 to 7360 (in bits) (by +128 bits)
    'perf_addr_filter_range* addr_filter_ranges' offset changed from 7424 to 7552 (in bits) (by +128 bits)
    'unsigned long int addr_filters_gen' offset changed from 7488 to 7616 (in bits) (by +128 bits)
    'perf_event* aux_event' offset changed from 7552 to 7680 (in bits) (by +128 bits)
    'void (perf_event*)* destroy' offset changed from 7616 to 7744 (in bits) (by +128 bits)
    'callback_head callback_head' offset changed from 7680 to 7808 (in bits) (by +128 bits)
  ...
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+587 more)

</details>

<details><summary><code>struct pmu</code> (perf_event.h:325:1)</summary>

```
  type size changed from 2368 to 2560 (in bits)
  2 data member insertions:
    'spinlock_t events_lock', at offset 128 (in bits) at perf_event.h:332:1
    'list_head events', at offset 192 (in bits) at perf_event.h:333:1
  there are data member changes:
    'module* module' offset changed from 128 to 320 (in bits) (by +192 bits)
    'device* dev' offset changed from 192 to 384 (in bits) (by +192 bits)
    'device* parent' offset changed from 256 to 448 (in bits) (by +192 bits)
    'const attribute_group** attr_groups' offset changed from 320 to 512 (in bits) (by +192 bits)
    'const attribute_group** attr_update' offset changed from 384 to 576 (in bits) (by +192 bits)
    'const char* name' offset changed from 448 to 640 (in bits) (by +192 bits)
    'int type' offset changed from 512 to 704 (in bits) (by +192 bits)
    'int capabilities' offset changed from 544 to 736 (in bits) (by +192 bits)
    'unsigned int scope' offset changed from 576 to 768 (in bits) (by +192 bits)
    'perf_cpu_pmu_context** cpu_pmu_context' offset changed from 640 to 832 (in bits) (by +192 bits)
    'atomic_t exclusive_cnt' offset changed from 704 to 896 (in bits) (by +192 bits)
    'int task_ctx_nr' offset changed from 736 to 928 (in bits) (by +192 bits)
    'int hrtimer_interval_ms' offset changed from 768 to 960 (in bits) (by +192 bits)
    'unsigned int nr_addr_filters' offset changed from 800 to 992 (in bits) (by +192 bits)
    'void (pmu*)* pmu_enable' offset changed from 832 to 1024 (in bits) (by +192 bits)
    'void (pmu*)* pmu_disable' offset changed from 896 to 1088 (in bits) (by +192 bits)
    'int (perf_event*)* event_init' offset changed from 960 to 1152 (in bits) (by +192 bits)
    'void (perf_event*, mm_struct*)* event_mapped' offset changed from 1024 to 1216 (in bits) (by +192 bits)
    'void (perf_event*, mm_struct*)* event_unmapped' offset changed from 1088 to 1280 (in bits) (by +192 bits)
    'int (perf_event*, int)* add' offset changed from 1152 to 1344 (in bits) (by +192 bits)
    'void (perf_event*, int)* del' offset changed from 1216 to 1408 (in bits) (by +192 bits)
    'void (perf_event*, int)* start' offset changed from 1280 to 1472 (in bits) (by +192 bits)
    'void (perf_event*, int)* stop' offset changed from 1344 to 1536 (in bits) (by +192 bits)
    'void (perf_event*)* read' offset changed from 1408 to 1600 (in bits) (by +192 bits)
    'void (pmu*, unsigned int)* start_txn' offset changed from 1472 to 1664 (in bits) (by +192 bits)
    'int (pmu*)* commit_txn' offset changed from 1536 to 1728 (in bits) (by +192 bits)
    'void (pmu*)* cancel_txn' offset changed from 1600 to 1792 (in bits) (by +192 bits)
    'int (perf_event*)* event_idx' offset changed from 1664 to 1856 (in bits) (by +192 bits)
    'void (perf_event_pmu_context*, task_struct*, typedef bool)* sched_task' offset changed from 1728 to 1920 (in bits) (by +192 bits)
    'kmem_cache* task_ctx_cache' offset changed from 1792 to 1984 (in bits) (by +192 bits)
    'void* (perf_event*, void**, int, typedef bool)* setup_aux' offset changed from 1856 to 2048 (in bits) (by +192 bits)
    'void (void*)* free_aux' offset changed from 1920 to 2112 (in bits) (by +192 bits)
    'long int (perf_event*, perf_output_handle*, unsigned long int)* snapshot_aux' offset changed from 1984 to 2176 (in bits) (by +192 bits)
    'int (list_head*)* addr_filters_validate' offset changed from 2048 to 2240 (in bits) (by +192 bits)
    'void (perf_event*)* addr_filters_sync' offset changed from 2112 to 2304 (in bits) (by +192 bits)
  ...
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+587 more)

</details>

<details><summary><code>struct kernel_ethtool_ts_info</code> (ethtool.h:763:1)</summary>

```
  type size changed from 192 to 256 (in bits)
  2 data member insertions:
    'hwtstamp_source phc_source', at offset 128 (in bits) at ethtool.h:844:1
    'int phc_phyindex', at offset 160 (in bits) at ethtool.h:845:1
  there are data member changes:
    'hwtstamp_tx_types tx_types' offset changed from 128 to 192 (in bits) (by +64 bits)
    'hwtstamp_rx_filters rx_filters' offset changed from 160 to 224 (in bits) (by +64 bits)
```

Reaches: `function const char* __ieee80211_create_tpt_led_trigger(ieee80211_hw*, unsigned int, const ieee80211_tpt_blink*, unsigned int)`, `function const char* __ieee80211_get_radio_led_name(ieee80211_hw*)`, `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function u32 ieee80211_calc_rx_airtime(ieee80211_hw*, ieee80211_rx_status*, int)`, `function int ieee80211_emulate_add_chanctx(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function void ieee80211_emulate_change_chanctx(ieee80211_hw*, ieee80211_chanctx_conf*, u32)`, `function void ieee80211_emulate_remove_chanctx(ieee80211_hw*, ieee80211_chanctx_conf*)`, `function int ieee80211_emulate_switch_vif_chanctx(ieee80211_hw*, ieee80211_vif_chanctx_switch*, int, ieee80211_chanctx_switch_mode)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)` … (+691 more)

</details>

<details><summary><code>enum hwtstamp_source</code> (net_tstamp.h:16:1)</summary>

```
  type size hasn't changed
  1 enumerator deletion:
    'hwtstamp_source::HWTSTAMP_SOURCE_UNSPEC' value '0'
```

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function const char* __ieee80211_create_tpt_led_trigger(ieee80211_hw*, unsigned int, const ieee80211_tpt_blink*, unsigned int)`, `function const char* __ieee80211_get_radio_led_name(ieee80211_hw*)`, `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function u32 ieee80211_calc_rx_airtime(ieee80211_hw*, ieee80211_rx_status*, int)` … (+698 more)

</details>

<details><summary><code>struct linux_mib</code> (snmp.h:104:1)</summary>

```
  type size changed from 8576 to 8640 (in bits)
  there are data member changes:
    type 'unsigned long int[134]' of 'linux_mib::mibs' changed:
      type name changed from 'unsigned long int[134]' to 'unsigned long int[135]'
      array type size changed from 8576 to 8640
      array type subrange 1 changed length from 134 to 135
```

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function const char* __ieee80211_create_tpt_led_trigger(ieee80211_hw*, unsigned int, const ieee80211_tpt_blink*, unsigned int)`, `function const char* __ieee80211_get_radio_led_name(ieee80211_hw*)`, `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function u32 ieee80211_calc_rx_airtime(ieee80211_hw*, ieee80211_rx_status*, int)` … (+698 more)

</details>

<details><summary><code>struct net</code> (net_namespace.h:61:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct netns_ipv6' of 'net::ipv6' changed:
      type size hasn't changed
      1 data member insertion:
        'spinlock_t fib_table_hash_lock', at offset 3840 (in bits) at ipv6.h:75:1
      there are data member changes:
        'fib6_table* fib6_main_tbl' offset changed from 3840 to 3904 (in bits) (by +64 bits)
        'list_head fib6_walkers' offset changed from 3904 to 3968 (in bits) (by +64 bits)
        'rwlock_t fib6_walker_lock' offset changed from 4032 to 4096 (in bits) (by +64 bits)
        'spinlock_t fib6_gc_lock' offset changed from 4096 to 4160 (in bits) (by +64 bits)
        'atomic_t ip6_rt_gc_expire' offset changed from 4128 to 4192 (in bits) (by +64 bits)
        'unsigned long int ip6_rt_last_gc' offset changed from 4160 to 4224 (in bits) (by +64 bits)
        'unsigned char flowlabel_has_excl' offset changed from 4224 to 4288 (in bits) (by +64 bits)
        'sock* ndisc_sk' offset changed from 4288 to 4352 (in bits) (by +64 bits)
        'sock* tcp_sk' offset changed from 4352 to 4416 (in bits) (by +64 bits)
        'sock* igmp_sk' offset changed from 4416 to 4480 (in bits) (by +64 bits)
        'sock* mc_autojoin_sk' offset changed from 4480 to 4544 (in bits) (by +64 bits)
        'hlist_head* inet6_addr_lst' offset changed from 4544 to 4608 (in bits) (by +64 bits)
        'spinlock_t addrconf_hash_lock' offset changed from 4608 to 4672 (in bits) (by +64 bits)
        'delayed_work addr_chk_work' offset changed from 4672 to 4736 (in bits) (by +64 bits)
        'atomic_t dev_addr_genid' offset changed from 5376 to 5440 (in bits) (by +64 bits)
        'atomic_t fib6_sernum' offset changed from 5408 to 5472 (in bits) (by +64 bits)
        'seg6_pernet_data* seg6_data' offset changed from 5440 to 5504 (in bits) (by +64 bits)
        'fib_notifier_ops* notifier_ops' offset changed from 5504 to 5568 (in bits) (by +64 bits)
        'fib_notifier_ops* ip6mr_notifier_ops' offset changed from 5568 to 5632 (in bits) (by +64 bits)
        'unsigned int ipmr_seq' offset changed from 5632 to 5696 (in bits) (by +64 bits)
        'struct {hlist_head head; spinlock_t lock; u32 seq;} ip6addrlbl_table' offset changed from 5696 to 5760 (in bits) (by +64 bits)
        'ioam6_pernet_data* ioam6_data' offset changed from 5824 to 5888 (in bits) (by +64 bits)
```

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function const char* __ieee80211_create_tpt_led_trigger(ieee80211_hw*, unsigned int, const ieee80211_tpt_blink*, unsigned int)`, `function const char* __ieee80211_get_radio_led_name(ieee80211_hw*)`, `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function u32 ieee80211_calc_rx_airtime(ieee80211_hw*, ieee80211_rx_status*, int)` … (+698 more)

</details>

<details><summary><code>struct net_device</code> (netdevice.h:2080:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'bool rtnl_link_initializing', at offset 10456 (in bits) at netdevice.h:2370:1
  there are data member changes:
    type 'enum {RTNL_LINK_INITIALIZED=0, RTNL_LINK_INITIALIZING=1, }' of 'net_device::rtnl_link_state' changed:
      entity changed from 'enum {RTNL_LINK_INITIALIZED=0, RTNL_LINK_INITIALIZING=1, }' to 'typedef bool' at types.h:35:1
      type size changed from 32 to 8 (in bits)
      type alignment changed from 32 to 0
    and name of 'net_device::rtnl_link_state' changed to 'net_device::moving_ns' at netdevice.h:2368:1
```

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function const char* __ieee80211_create_tpt_led_trigger(ieee80211_hw*, unsigned int, const ieee80211_tpt_blink*, unsigned int)`, `function const char* __ieee80211_get_radio_led_name(ieee80211_hw*)`, `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function u32 ieee80211_calc_rx_airtime(ieee80211_hw*, ieee80211_rx_status*, int)` … (+698 more)

</details>

<details><summary><code>struct netlink_ext_ack</code> (netlink.h:82:1)</summary>

```
  type size changed from 1088 to 1024 (in bits)
  there are data member changes:
    type 'u8[20]' of 'netlink_ext_ack::cookie' changed:
      type name changed from 'u8[20]' to 'u8[8]'
      array type size changed from 160 to 64
      array type subrange 1 changed length from 20 to 8
    'u8 cookie_len' offset changed from 432 to 336 (in bits) (by -96 bits)
    'char _msg_buf[80]' offset changed from 440 to 344 (in bits) (by -96 bits)
```

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function const char* __ieee80211_create_tpt_led_trigger(ieee80211_hw*, unsigned int, const ieee80211_tpt_blink*, unsigned int)`, `function const char* __ieee80211_get_radio_led_name(ieee80211_hw*)`, `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function u32 ieee80211_calc_rx_airtime(ieee80211_hw*, ieee80211_rx_status*, int)` … (+698 more)

</details>

<details><summary><code>struct sock</code> (sock.h:345:1)</summary>

```
  type size hasn't changed
```

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function const char* __ieee80211_create_tpt_led_trigger(ieee80211_hw*, unsigned int, const ieee80211_tpt_blink*, unsigned int)`, `function const char* __ieee80211_get_radio_led_name(ieee80211_hw*)`, `function void __ieee80211_schedule_txq(ieee80211_hw*, ieee80211_txq*, bool)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_tim(ieee80211_hw*, ieee80211_vif*, u16*, u16*, unsigned int)`, `function u32 ieee80211_calc_rx_airtime(ieee80211_hw*, ieee80211_rx_status*, int)` … (+698 more)

</details>

<details><summary><code>struct address_space_operations</code> (fs.h:435:1)</summary>

```
  type size changed from 1280 to 1216 (in bits)
  1 data member deletion:
    'int (page*, writeback_control*)* writepage', at offset 0 (in bits) at fs.h:436:1
  there are data member changes:
    'int (file*, folio*)* read_folio' offset changed from 64 to 0 (in bits) (by -64 bits)
    'int (address_space*, writeback_control*)* writepages' offset changed from 128 to 64 (in bits) (by -64 bits)
    'typedef bool (address_space*, folio*)* dirty_folio' offset changed from 192 to 128 (in bits) (by -64 bits)
    'void (readahead_control*)* readahead' offset changed from 256 to 192 (in bits) (by -64 bits)
    'int (file*, address_space*, typedef loff_t, unsigned int, folio**, void**)* write_begin' offset changed from 320 to 256 (in bits) (by -64 bits)
    'int (file*, address_space*, typedef loff_t, unsigned int, unsigned int, folio*, void*)* write_end' offset changed from 384 to 320 (in bits) (by -64 bits)
    'typedef sector_t (address_space*, typedef sector_t)* bmap' offset changed from 448 to 384 (in bits) (by -64 bits)
    'void (folio*, typedef size_t, typedef size_t)* invalidate_folio' offset changed from 512 to 448 (in bits) (by -64 bits)
    'typedef bool (folio*, typedef gfp_t)* release_folio' offset changed from 576 to 512 (in bits) (by -64 bits)
    'void (folio*)* free_folio' offset changed from 640 to 576 (in bits) (by -64 bits)
    'typedef ssize_t (kiocb*, iov_iter*)* direct_IO' offset changed from 704 to 640 (in bits) (by -64 bits)
    'int (address_space*, folio*, folio*, enum migrate_mode)* migrate_folio' offset changed from 768 to 704 (in bits) (by -64 bits)
    'int (folio*)* launder_folio' offset changed from 832 to 768 (in bits) (by -64 bits)
    'typedef bool (folio*, typedef size_t, typedef size_t)* is_partially_uptodate' offset changed from 896 to 832 (in bits) (by -64 bits)
    'void (folio*, bool*, bool*)* is_dirty_writeback' offset changed from 960 to 896 (in bits) (by -64 bits)
    'int (address_space*, folio*)* error_remove_folio' offset changed from 1024 to 960 (in bits) (by -64 bits)
    'int (swap_info_struct*, file*, sector_t*)* swap_activate' offset changed from 1088 to 1024 (in bits) (by -64 bits)
    'void (file*)* swap_deactivate' offset changed from 1152 to 1088 (in bits) (by -64 bits)
    'int (kiocb*, iov_iter*)* swap_rw' offset changed from 1216 to 1152 (in bits) (by -64 bits)
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct cgroup</code> (cgroup-defs.h:412:1)</summary>

```
  type size changed from 9216 to 8704 (in bits)
  2 data member deletions:
    'list_head rstat_css_list', at offset 6592 (in bits) at cgroup-defs.h:521:1
    'cgroup* rstat_flush_next', at offset 7168 (in bits) at cgroup-defs.h:535:1
  there are data member changes:
    type 'cgroup_rstat_cpu*' of 'cgroup::rstat_cpu' changed:
      pointer type changed from: 'cgroup_rstat_cpu*' to: 'cgroup_rstat_base_cpu*'
    and name of 'cgroup::rstat_cpu' changed to 'cgroup::rstat_base_cpu' at cgroup-defs.h:557:1
    type 'struct cgroup_subsys_state' of 'cgroup::self' changed:
      type size hasn't changed
      1 data member deletion:
        'list_head rstat_css_node', at offset 512 (in bits) at cgroup-defs.h:181:1
      2 data member insertions:
        'css_rstat_cpu* rstat_cpu', at offset 256 (in bits) at cgroup-defs.h:187:1
        'cgroup_subsys_state* rstat_flush_next', at offset 1600 (in bits) at cgroup-defs.h:245:1
      there are data member changes:
        'list_head sibling' offset changed from 256 to 320 (in bits) (by +64 bits)
        'list_head children' offset changed from 384 to 448 (in bits) (by +64 bits)
        'int id' offset changed from 640 to 576 (in bits) (by -64 bits)
        'unsigned int flags' offset changed from 672 to 608 (in bits) (by -64 bits)
        'u64 serial_nr' offset changed from 704 to 640 (in bits) (by -64 bits)
        'atomic_t online_cnt' offset changed from 768 to 704 (in bits) (by -64 bits)
        'work_struct destroy_work' offset changed from 832 to 768 (in bits) (by -64 bits)
        'rcu_work destroy_rwork' offset changed from 1088 to 1024 (in bits) (by -64 bits)
        'cgroup_subsys_state* parent' offset changed from 1536 to 1472 (in bits) (by -64 bits)
        'int nr_descendants' offset changed from 1600 to 1536 (in bits) (by -64 bits)
    'cacheline_padding _pad_' offset changed from 7168 to 6656 (in bits) (by -512 bits)
    'cgroup_base_stat last_bstat' offset changed from 7232 to 6656 (in bits) (by -576 bits)
    'cgroup_base_stat bstat' offset changed from 7488 to 6912 (in bits) (by -576 bits)
    'prev_cputime prev_cputime' offset changed from 7744 to 7168 (in bits) (by -576 bits)
    'list_head pidlists' offset changed from 7936 to 7360 (in bits) (by -576 bits)
    'mutex pidlist_mutex' offset changed from 8064 to 7488 (in bits) (by -576 bits)
    'wait_queue_head_t offline_waitq' offset changed from 8320 to 7744 (in bits) (by -576 bits)
    'work_struct release_agent_work' offset changed from 8512 to 7936 (in bits) (by -576 bits)
    'psi_group* psi' offset changed from 8768 to 8192 (in bits) (by -576 bits)
    'cgroup_bpf bpf' offset changed from 8832 to 8256 (in bits) (by -576 bits)
    'cgroup_freezer_state freezer' offset changed from 8832 to 8256 (in bits) (by -576 bits)
    'cgroup* ancestors[]' offset changed from 8960 to 8384 (in bits) (by -576 bits)
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct cgroup_root</code> (cgroup-defs.h:577:1)</summary>

```
  type size changed from 43520 to 43008 (in bits)
  there are data member changes:
    type 'struct cgroup' of 'cgroup_root::cgrp' changed, as reported earlier
    'cgroup* cgrp_ancestor_storage' offset changed from 9728 to 9216 (in bits) (by -512 bits)
    'atomic_t nr_cgrps' offset changed from 9792 to 9280 (in bits) (by -512 bits)
    'unsigned int flags' offset changed from 9824 to 9312 (in bits) (by -512 bits)
    'char release_agent_path[4096]' offset changed from 9856 to 9344 (in bits) (by -512 bits)
    'char name[64]' offset changed from 42624 to 42112 (in bits) (by -512 bits)
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct cgroup_subsys</code> (cgroup-defs.h:706:1)</summary>

```
  type size changed from 2048 to 2112 (in bits)
  2 data member insertions:
    'spinlock_t rstat_ss_lock', at offset 2016 (in bits) at cgroup-defs.h:823:1
    'raw_spinlock_t* rstat_ss_cpu_lock', at offset 2048 (in bits) at cgroup-defs.h:824:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct dir_context</code> (fs.h:2071:1)</summary>

```
  type size changed from 128 to 192 (in bits)
  1 data member insertion:
    'int count', at offset 128 (in bits) at fs.h:2092:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct kiocb</code> (fs.h:404:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u8 ki_write_stream', at offset 304 (in bits) at fs.h:413:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct kstat</code> (stat.h:22:1)</summary>

```
  type size changed from 1472 to 1536 (in bits)
  1 data member insertion:
    'u32 atomic_write_unit_max_opt', at offset 1440 (in bits) at stat.h:60:1
  there are data member changes:
    'u32 atomic_write_segments_max' offset changed from 1440 to 1472 (in bits) (by +32 bits)
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct mod_arch_specific</code> (module.h:8:1)</summary>

```
  type size changed from 192 to 320 (in bits)
  1 data member insertion:
    'its_array its_pages', at offset 192 (in bits) at module.h:21:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct module</code> (module.h:414:1)</summary>

```
  type size hasn't changed
  2 data member deletions:
    'int its_num_pages', at offset 9184 (in bits) at module.h:590:1
    'void** its_page_array', at offset 9216 (in bits) at module.h:591:1
  there are data member changes:
    type 'struct mod_arch_specific' of 'module::arch' changed, as reported earlier
    'unsigned long int taints' offset changed from 6784 to 6912 (in bits) (by +128 bits)
    'unsigned int num_bugs' offset changed from 6848 to 6976 (in bits) (by +128 bits)
    'list_head bug_list' offset changed from 6912 to 7040 (in bits) (by +128 bits)
    'bug_entry* bug_table' offset changed from 7040 to 7168 (in bits) (by +128 bits)
    'mod_kallsyms* kallsyms' offset changed from 7104 to 7232 (in bits) (by +128 bits)
    'mod_kallsyms core_kallsyms' offset changed from 7168 to 7296 (in bits) (by +128 bits)
    'module_sect_attrs* sect_attrs' offset changed from 7424 to 7552 (in bits) (by +128 bits)
    'module_notes_attrs* notes_attrs' offset changed from 7488 to 7616 (in bits) (by +128 bits)
    'char* args' offset changed from 7552 to 7680 (in bits) (by +128 bits)
    'void* percpu' offset changed from 7616 to 7744 (in bits) (by +128 bits)
    'unsigned int percpu_size' offset changed from 7680 to 7808 (in bits) (by +128 bits)
    'void* noinstr_text_start' offset changed from 7744 to 7872 (in bits) (by +128 bits)
    'unsigned int noinstr_text_size' offset changed from 7808 to 7936 (in bits) (by +128 bits)
    'unsigned int num_tracepoints' offset changed from 7840 to 7968 (in bits) (by +128 bits)
    'tracepoint_ptr_t* tracepoints_ptrs' offset changed from 7872 to 8000 (in bits) (by +128 bits)
    'unsigned int num_srcu_structs' offset changed from 7936 to 8064 (in bits) (by +128 bits)
    'srcu_struct** srcu_struct_ptrs' offset changed from 8000 to 8128 (in bits) (by +128 bits)
    'jump_entry* jump_entries' offset changed from 8064 to 8192 (in bits) (by +128 bits)
    'unsigned int num_jump_entries' offset changed from 8128 to 8256 (in bits) (by +128 bits)
    'unsigned int num_trace_bprintk_fmt' offset changed from 8160 to 8288 (in bits) (by +128 bits)
    'const char** trace_bprintk_fmt_start' offset changed from 8192 to 8320 (in bits) (by +128 bits)
    'trace_event_call** trace_events' offset changed from 8256 to 8384 (in bits) (by +128 bits)
    'unsigned int num_trace_events' offset changed from 8320 to 8448 (in bits) (by +128 bits)
    'trace_eval_map** trace_evals' offset changed from 8384 to 8512 (in bits) (by +128 bits)
    'unsigned int num_trace_evals' offset changed from 8448 to 8576 (in bits) (by +128 bits)
    'void* kprobes_text_start' offset changed from 8512 to 8640 (in bits) (by +128 bits)
    'unsigned int kprobes_text_size' offset changed from 8576 to 8704 (in bits) (by +128 bits)
    'unsigned long int* kprobe_blacklist' offset changed from 8640 to 8768 (in bits) (by +128 bits)
    'unsigned int num_kprobe_blacklist' offset changed from 8704 to 8832 (in bits) (by +128 bits)
    'int num_static_call_sites' offset changed from 8736 to 8864 (in bits) (by +128 bits)
    'static_call_site* static_call_sites' offset changed from 8768 to 8896 (in bits) (by +128 bits)
    'list_head source_list' offset changed from 8832 to 8960 (in bits) (by +128 bits)
    'list_head target_list' offset changed from 8960 to 9088 (in bits) (by +128 bits)
    'void ()* exit' offset changed from 9088 to 9216 (in bits) (by +128 bits)
  ...
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct sb_writers</code> (fs.h:1306:1)</summary>

```
  type size changed from 2432 to 2496 (in bits)
  1 data member insertion:
    'void* freeze_owner', at offset 128 (in bits) at fs.h:1321:1
  there are data member changes:
    'percpu_rw_semaphore rw_sem[3]' offset changed from 128 to 192 (in bits) (by +64 bits)
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct super_block</code> (fs.h:1313:1)</summary>

```
  type size changed from 10240 to 10752 (in bits)
  there are data member changes:
    type 'struct sb_writers' of 'super_block::s_writers' changed, as reported earlier
    'void* s_fs_info' offset changed from 6976 to 7040 (in bits) (by +64 bits)
    'u32 s_time_gran' offset changed from 7040 to 7104 (in bits) (by +64 bits)
    'time64_t s_time_min' offset changed from 7104 to 7168 (in bits) (by +64 bits)
    'time64_t s_time_max' offset changed from 7168 to 7232 (in bits) (by +64 bits)
    'u32 s_fsnotify_mask' offset changed from 7232 to 7296 (in bits) (by +64 bits)
    'fsnotify_sb_info* s_fsnotify_info' offset changed from 7296 to 7360 (in bits) (by +64 bits)
    'char s_id[32]' offset changed from 7360 to 7424 (in bits) (by +64 bits)
    'uuid_t s_uuid' offset changed from 7616 to 7680 (in bits) (by +64 bits)
    'u8 s_uuid_len' offset changed from 7744 to 7808 (in bits) (by +64 bits)
    'char s_sysfs_name[37]' offset changed from 7752 to 7816 (in bits) (by +64 bits)
    'unsigned int s_max_links' offset changed from 8064 to 8128 (in bits) (by +64 bits)
    'mutex s_vfs_rename_mutex' offset changed from 8128 to 8192 (in bits) (by +64 bits)
    'const char* s_subtype' offset changed from 8384 to 8448 (in bits) (by +64 bits)
    'const dentry_operations* s_d_op' offset changed from 8448 to 8512 (in bits) (by +64 bits)
    'shrinker* s_shrink' offset changed from 8512 to 8576 (in bits) (by +64 bits)
    'atomic_long_t s_remove_count' offset changed from 8576 to 8640 (in bits) (by +64 bits)
    'int s_readonly_remount' offset changed from 8640 to 8704 (in bits) (by +64 bits)
    'errseq_t s_wb_err' offset changed from 8672 to 8736 (in bits) (by +64 bits)
    'workqueue_struct* s_dio_done_wq' offset changed from 8704 to 8768 (in bits) (by +64 bits)
    'hlist_head s_pins' offset changed from 8768 to 8832 (in bits) (by +64 bits)
    'user_namespace* s_user_ns' offset changed from 8832 to 8896 (in bits) (by +64 bits)
    'list_lru s_dentry_lru' offset changed from 8896 to 8960 (in bits) (by +64 bits)
    'list_lru s_inode_lru' offset changed from 8960 to 9024 (in bits) (by +64 bits)
    'callback_head rcu' offset changed from 9024 to 9088 (in bits) (by +64 bits)
    'work_struct destroy_work' offset changed from 9152 to 9216 (in bits) (by +64 bits)
    'mutex s_sync_lock' offset changed from 9408 to 9472 (in bits) (by +64 bits)
    'int s_stack_depth' offset changed from 9664 to 9728 (in bits) (by +64 bits)
    'spinlock_t s_inode_list_lock' offset changed from 9728 to 10240 (in bits) (by +512 bits)
    'list_head s_inodes' offset changed from 9792 to 10304 (in bits) (by +512 bits)
    'spinlock_t s_inode_wblist_lock' offset changed from 9920 to 10432 (in bits) (by +512 bits)
    'list_head s_inodes_wb' offset changed from 9984 to 10496 (in bits) (by +512 bits)
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct super_operations</code> (fs.h:2287:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int (super_block*, enum freeze_holder)*' of 'super_operations::freeze_super' changed:
      pointer type changed from: 'int (super_block*, enum freeze_holder)*' to: 'int (super_block*, enum freeze_holder, void*)*'
    type 'int (super_block*, enum freeze_holder)*' of 'super_operations::thaw_super' changed:
      pointer type changed from: 'int (super_block*, enum freeze_holder)*' to: 'int (super_block*, enum freeze_holder, void*)*'
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct task_struct</code> (sched.h:813:1)</summary>

```
  type size changed from 58880 to 24576 (in bits)
  1 data member insertion:
    'unsigned int in_nf_duplicate', at offset 10828 (in bits) at sched.h:1046:1
  there are data member changes:
    type 'struct thread_struct' of 'task_struct::thread' changed:
      type size changed from 35328 to 1216 (in bits)
      1 data member deletion:
        'fpu fpu', at offset 1536 (in bits) at processor.h:519:1
    and offset changed from 23552 to 23360 (in bits) (by -192 bits)
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct user_struct</code> (user.h:14:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct ratelimit_state' of 'user_struct::ratelimit' changed, as reported earlier
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct vm_area_struct</code> (mm_types.h:779:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'pfnmap_track_ctx* pfnmap_track_ctx', at offset 1344 (in bits) at mm_types.h:913:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+719 more)

</details>

<details><summary><code>struct ratelimit_state</code> (ratelimit_types.h:15:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int' of 'ratelimit_state::printed' changed:
      entity changed from 'int' to 'typedef atomic_t' at types.h:183:1
      type size hasn't changed
    and name of 'ratelimit_state::printed' changed to 'ratelimit_state::rs_n_left' at ratelimit_types.h:21:1
    type 'int' of 'ratelimit_state::missed' changed:
      entity changed from 'int' to 'typedef atomic_t' at types.h:183:1
      type size hasn't changed
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)` … (+720 more)

</details>

## Header-level interfaces

Macros, static inline functions, struct/union/enum tags, typedefs and enumerators defined in provider headers (headers the consumer objects were compiled against that are not consumer code) and named in consumer code. They never appear as ELF symbols, but LinuxKPI has to provide them. Name-based, so an occasional false positive is possible (e.g. a local variable or member sharing a macro's name).

| | count |
|---|---|
| used in v6.15 | 4747 |
| used in v6.16 | 4790 |
| newly used | 53 |
| no longer used | 10 |
| likely renames | 1 |
| macro/inline signature changed | 2 |
| macro body changed | 5 |
| moved to another header | 6 |

### Likely renames (header)

| v6.15 | v6.16 | kind | signature |
|---|---|---|---|
| `from_timer` (include/linux/timer.h) | `timer_container_of` (include/linux/timer.h) | macro | `(var,callback_timer,timer_fieldname)` |

### Newly used (header)

| name | kind | header | signature | used by |
|---|---|---|---|---|
| `BIT_U16` | macro | include/linux/bits.h | `(nr)` | i915,xe |
| `BIT_U32` | macro | include/linux/bits.h | `(nr)` | i915,xe |
| `BIT_U64` | macro | include/linux/bits.h | `(nr)` | i915,xe |
| `BIT_U8` | macro | include/linux/bits.h | `(nr)` | i915,xe |
| `DEFINE_RAW_FLEX` | macro | include/linux/overflow.h | `(type,name,member,count)` | iwlmvm |
| `DIV64_U64_ROUND_CLOSEST` | macro | include/linux/math64.h | `(dividend,divisor)` | i915 |
| `GENMASK_U16` | macro | include/linux/bits.h | `(h,l)` | i915,xe |
| `GENMASK_U32` | macro | include/linux/bits.h | `(h,l)` | i915,xe |
| `GENMASK_U64` | macro | include/linux/bits.h | `(h,l)` | i915,xe |
| `GENMASK_U8` | macro | include/linux/bits.h | `(h,l)` | i915,xe |
| `IEEE80211_EHT_OPER_MCS15_DISABLE` | macro | include/linux/ieee80211.h |  | ath12k |
| `IEEE80211_EML_CAP_EMLSR_PADDING_DELAY_256US` | macro | include/linux/ieee80211.h |  | rtw89_core |
| `IEEE80211_EML_CAP_EMLSR_TRANSITION_DELAY_256US` | macro | include/linux/ieee80211.h |  | rtw89_core |
| `IEEE80211_VHT_MAX_AMPDU_256K` | enumerator | include/linux/ieee80211.h |  | rtw88_8814a |
| `NL80211_EXTERNAL_AUTH_START` | enumerator | include/uapi/linux/nl80211.h |  | brcmfmac-cyw |
| `NL80211_FEATURE_SAE` | enumerator | include/uapi/linux/nl80211.h |  | brcmfmac |
| `NL80211_RRF_ALLOW_20MHZ_ACTIVITY` | enumerator | include/uapi/linux/nl80211.h |  | iwlwifi |
| `NL80211_RXMGMT_FLAG_EXTERNAL_AUTH` | enumerator | include/uapi/linux/nl80211.h |  | brcmfmac-cyw |
| `OPTIMIZER_HIDE_VAR` | macro | include/linux/compiler.h | `(var)` | amdgpu |
| `PM_POST_SUSPEND` | macro | include/linux/suspend.h |  | xe |
| `PM_SUSPEND_PREPARE` | macro | include/linux/suspend.h |  | ath11k,xe |
| `QCOM_SSR_AFTER_POWERUP` | enumerator | include/linux/remoteproc/qcom_rproc.h |  | ath12k |
| `S16_MIN` | macro | include/linux/limits.h |  | rtw89_8851b,rtw89_8851be,rtw89_8852a,rtw89_8852ae,rtw89_8852b,rtw89_8852b_common,rtw89_8852be,rtw89_8852bt,rtw89_8852bte,rtw89_8852c,rtw89_8852ce,rtw89_8922a,rtw89_8922ae,rtw89_core,rtw89_pci |
| `SZ_512M` | macro | include/linux/sizes.h |  | xe |
| `VFM_MODEL` | macro | arch/x86/include/asm/cpu_device_id.h | `(vfm)` | amdgpu |
| `__struct_size` | macro | include/linux/compiler_types.h | `(p)` | iwlmvm |
| `acpi_device_hid` | inline | include/acpi/acpi_bus.h | `const char *(struct acpi_device *device)` | amdgpu |
| `acpi_match_device` | inline | include/linux/acpi.h | `const struct acpi_device_id *(const struct acpi_device_id *ids, const struct device *dev)` | amdgpu |
| `cfg80211_chandef_get_width` | inline | include/net/cfg80211.h | `int(const struct cfg80211_chan_def *c)` | iwlmld |
| `cfg80211_external_auth_params` | struct | include/net/cfg80211.h |  | brcmfmac-cyw |
| `crypto_shash_final` | inline | include/crypto/hash.h | `int(struct shash_desc *desc, u8 *out)` | ath11k,ath12k |
| `crypto_shash_update` | inline | include/crypto/hash.h | `int(struct shash_desc *desc, const u8 *data, unsigned int len)` | ath11k,ath12k |
| `dma_fence_unwrap` | struct | include/linux/dma-fence-unwrap.h |  | amdgpu |
| `dma_fence_unwrap_for_each` | macro | include/linux/dma-fence-unwrap.h | `(fence,cursor,head)` | amdgpu |
| `dma_rmb` | macro | include/asm-generic/barrier.h | `()` | ath11k,ath12k |
| `ieee80211_eml_trans_timeout_in_us` | inline | include/linux/ieee80211.h | `u32(u16 eml_cap)` | ath12k |
| `ieee80211_emlsr_pad_delay_in_us` | inline | include/linux/ieee80211.h | `u32(u16 eml_cap)` | ath12k |
| `ieee80211_emlsr_trans_delay_in_us` | inline | include/linux/ieee80211.h | `u32(u16 eml_cap)` | ath12k |
| `irq_domain_create_linear` | inline | include/linux/irqdomain.h | `struct irq_domain *(struct fwnode_handle *fwnode, unsigned int size, const struct irq_domain_ops *ops, void *host_data)` | amdgpu |
| `llist_add_batch` | inline | include/linux/llist.h | `bool(struct llist_node *new_first, struct llist_node *new_last, struct llist_head *head)` | i915 |
| `mutex_trylock` | macro | include/linux/mutex.h | `(lock)` | amdgpu,drm_display_helper,drm_kms_helper,i915 |
| `of_reserved_mem_lookup` | inline | include/linux/of_reserved_mem.h | `struct reserved_mem *(struct device_node *np)` | ath12k |
| `pm_notifier` | macro | include/linux/suspend.h | `(fn,pri)` | xe |
| `pm_suspend_in_progress` | inline | include/linux/suspend.h | `bool(void)` | xe |
| `ratelimit_state_get_miss` | inline | include/linux/ratelimit.h | `int(struct ratelimit_state *rs)` | i915 |
| `ratelimit_state_reset_interval` | inline | include/linux/ratelimit.h | `void(struct ratelimit_state *rs, int interval_init)` | amdgpu |
| `reserved_mem` | struct | include/linux/of_reserved_mem.h |  | ath12k |
| `roundup_u64` | inline | include/linux/math64.h | `u64(u64 x, u32 y)` | rtw89_core |
| `rproc` | struct | include/linux/remoteproc.h |  | ath12k |
| `sg_next` | inline | include/linux/scatterlist.h | `struct scatterlist *(struct scatterlist *sg)` | i915,ttm,xe |
| `size_mul` | inline | include/linux/overflow.h | `size_t __must_check(size_t factor1, size_t factor2)` | amdgpu |
| `sysfs_update_group` | inline | include/linux/sysfs.h | `int(struct kobject *kobj, const struct attribute_group *grp)` | amdgpu |
| `wait_var_event_timeout` | macro | include/linux/wait_bit.h | `(var,condition,timeout)` | xe |

### No longer used (header)

| name | kind | header | signature | used by |
|---|---|---|---|---|
| `IEEE80211_MAX_AMPDU_BUF_HT` | macro | include/linux/ieee80211.h |  | iwlwifi |
| `MICRO` | macro | include/linux/units.h |  | xe |
| `NLA_U32` | enumerator | include/net/netlink.h |  | iwlmvm |
| `RX_ENC_FLAG_HT_GF` | enumerator | include/net/mac80211.h |  | iwlmvm |
| `crypto_shash_init` | inline | include/crypto/hash.h | `int(struct shash_desc *desc)` | ath11k,ath12k |
| `find_lock_page` | inline | include/linux/pagemap.h | `struct page *(struct address_space *mapping, pgoff_t index)` | i915 |
| `irq_domain_add_linear` | inline | include/linux/irqdomain.h | `struct irq_domain *(struct device_node *of_node, unsigned int size, const struct irq_domain_ops *ops, void *host_data)` | amdgpu |
| `nla_get_u32` | inline | include/net/netlink.h | `u32(const struct nlattr *nla)` | iwlmvm |
| `nla_parse_deprecated` | inline | include/net/netlink.h | `int(struct nlattr **tb, int maxtype, const struct nlattr *head, int len, const struct nla_policy *policy, struct netlink_ext_ack *extack)` | iwlmvm |
| `page_mapped` | inline | include/linux/mm.h | `bool(const struct page *page)` | i915 |

### Signature changed (header)

| name | kind | header | v6.15 | v6.16 |
|---|---|---|---|---|
| `BUILD_BUG_ON_ZERO` | macro | include/linux/build_bug.h | `(e)` | `(e,...)` |
| `intel_vsec_register` | inline | include/linux/intel_vsec.h | `void(struct pci_dev *pdev, struct intel_vsec_platform_info *info)` | `int(struct pci_dev *pdev, struct intel_vsec_platform_info *info)` |

### Moved to another header

| name | v6.15 | v6.16 |
|---|---|---|
| `BITS_PER_TYPE` | include/linux/bitops.h | include/linux/bits.h |
| `PTR_IF` | include/linux/kernel.h | include/linux/util_macros.h |
| `READ` | include/linux/kernel.h | include/linux/types.h |
| `WRITE` | include/linux/kernel.h | include/linux/types.h |
| `devm_add_action_or_reset` | include/linux/device.h | include/linux/device/devres.h |
| `u64_to_user_ptr` | include/linux/kernel.h | include/linux/util_macros.h |

<details><summary>Macro body changed (5)</summary>

| macro | header | v6.15 | v6.16 |
|---|---|---|---|
| `DEFINE_EVENT_PRINT` | include/linux/tracepoint.h | `DECLARE_TRACE(name, PARAMS(proto), PARAMS(args))` | `DECLARE_TRACE_EVENT(name, PARAMS(proto), PARAMS(args))` |
| `MODULE_DEVICE_TABLE` | include/linux/module.h | `extern typeof(name) __mod_device_table__##type##__##name __attribute__ ((unused, alias(__stringify(name))))` | `static typeof(name) __mod_device_table__##type##__##name __attribute__ ((used, alias(__stringify(name))))` |
| `TRACE_EVENT_CONDITION` | include/linux/tracepoint.h | `DECLARE_TRACE_CONDITION(name, PARAMS(proto), PARAMS(args), PARAMS(cond))` | `DECLARE_TRACE_EVENT_CONDITION(name, PARAMS(proto), PARAMS(args), PARAMS(cond))` |
| `timer_setup` | include/linux/timer.h | `__init_timer((timer), (callback), (flags))` | `__timer_init((timer), (callback), (flags))` |
| `u64_to_user_ptr` | include/linux/util_macros.h | `( { typecheck(u64, (x)); (void __user *)(uintptr_t)(x); } )` | `({ typecheck(u64, (x)); (void __user *)(uintptr_t)(x); })` |

</details>

## Same interface, different set of users

| symbol | v6.15 | v6.16 |
|---|---|---|
| `__copy_overflow` | drm,i915 | drm,i915,xe |
| `__dma_sync_single_for_cpu` | ath10k_pci,ath11k,iwlwifi,mt76,rtw88_pci,rtw89_pci | ath10k_pci,ath11k,ath12k,iwlwifi,mt76,rtw88_pci,rtw89_pci |
| `__ioread64_lo_hi` | i915,xe | xe |
| `__kmalloc_noprof` | amdgpu,drm_display_helper,drm,drm_buddy,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath11k_pci,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,rtw88_core,rtw89_core | amdgpu,drm_display_helper,drm,drm_buddy,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath11k_pci,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,iwlmld,iwlmvm,mt76,rtw88_core,rtw89_core |
| `__sw_hweight64` | amdgpu,drm,drm_buddy,i915,xe,iwlwifi,iwlmld,iwlmvm | amdgpu,drm,drm_buddy,i915,xe,ath12k,iwlwifi,iwlmld,iwlmvm |
| `__usecs_to_jiffies` | i915,xe,iwlwifi,iwlmld,iwlmvm,mt7921-common | amdgpu,i915,xe,iwlwifi,iwlmld,iwlmvm,mt7921-common,rtw89_core |
| `__x86_indirect_thunk_r8` | amdgpu,drm,drm_gpuvm,drm_kms_helper,i915,radeon,xe,mt76,mt7615-common,mt7915e,mt7996e,rtw88_8822c,rtw88_core,rtw89_8851b,rtw89_8852a,rtw89_8852b_common,rtw89_core,rtw89_pci | amdgpu,drm,drm_gpuvm,drm_kms_helper,i915,radeon,xe,ath12k,mt76,mt7615-common,mt7915e,mt7996e,rtw88_8822c,rtw88_core,rtw89_8851b,rtw89_8852a,rtw89_8852b_common,rtw89_core,rtw89_pci |
| `__x86_indirect_thunk_r9` | amdgpu,drm,drm_gpuvm,i915,xe,ath11k,ath12k,mt76,rtw88_8822b,rtw88_8822c,rtw88_core,rtw89_core,rtw89_pci | amdgpu,drm,drm_gpuvm,i915,xe,ath11k,ath12k,mt76,mt7996e,rtw88_8822b,rtw88_8822c,rtw89_core,rtw89_pci |
| `__x86_indirect_thunk_rax` | amdgpu,drm_display_helper,drm,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7615e,mt7915e,mt7921-common,mt7921e,mt7925-common,mt7925e,mt792x-lib,mt7996e,rtw88_8723d,rtw88_8723x,rtw88_8814a,rtw88_8821c,rtw88_8822b,rtw88_8822c,rtw88_core,rtw88_pci,rtw89_8851b,rtw89_8852a,rtw89_8852b,rtw89_8852b_common,rtw89_8852bt,rtw89_8852c,rtw89_8922a,rtw89_core,rtw89_pci | amdgpu,drm_display_helper,drm,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7615e,mt7915e,mt7921-common,mt7921e,mt7925-common,mt7925e,mt792x-lib,mt7996e,rtw88_8723d,rtw88_8723x,rtw88_8814a,rtw88_8821c,rtw88_8822b,rtw88_8822c,rtw88_core,rtw88_pci,rtw89_8851b,rtw89_8852a,rtw89_8852b,rtw89_8852b_common,rtw89_8852bt,rtw89_8852c,rtw89_8922a,rtw89_core,rtw89_pci |
| `__xa_alloc` | drm,i915,gpu-sched,xe | amdgpu,drm,i915,gpu-sched,xe |
| `_find_next_zero_bit` | amdgpu,xe,rtw89_core | xe,rtw89_core |
| `cfg80211_mgmt_tx_status_ext` | brcmfmac | brcmfmac,brcmfmac-cyw |
| `cfg80211_rx_mgmt_ext` | brcmfmac | brcmfmac,brcmfmac-cyw |
| `complete` | amdgpu,ath10k_core,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_core,rtw89_core,rtw89_pci | amdgpu,ath10k_core,ath11k,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,mt76,rtw88_core,rtw89_core,rtw89_pci |
| `complete_all` | drm,drm_kms_helper,i915,gpu-sched,xe,ath11k,brcmfmac,rtw88_core,rtw89_core | drm,drm_kms_helper,i915,gpu-sched,xe,ath11k,ath12k,brcmfmac,rtw88_core,rtw89_core |
| `devm_kmemdup` | mt76,mt7615e,mt7915e,mt7921-common,mt7921e,mt7925-common,mt7925e,mt792x-lib,mt7996e | mt76,mt7615e,mt7915e,mt7921-common,mt7921e,mt7925-common,mt7925e,mt792x-lib,mt7996e,rtw89_core |
| `dma_map_page_attrs` | amdgpu,radeon,ttm,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_pci,rtw89_pci | amdgpu,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_pci,rtw89_pci |
| `dma_resv_replace_fences` | xe | amdgpu,xe |
| `dma_unmap_page_attrs` | amdgpu,radeon,ttm,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt76-connac-lib,rtw88_pci,rtw89_pci | amdgpu,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt76-connac-lib,rtw88_pci,rtw89_pci |
| `dmi_first_match` | drm_panel_orientation_quirks,i915,brcmfmac,rtw89_core | drm_panel_orientation_quirks,i915,ath11k,brcmfmac,rtw89_core |
| `drain_workqueue` | amdgpu,i915,ttm | amdgpu,i915,ttm,xe |
| `flush_delayed_work` | amdgpu,i915,radeon,xe,iwlmld,iwlmvm | amdgpu,i915,radeon,xe,iwlmvm |
| `ieee80211_channel_to_freq_khz` | ath10k_core,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7921-common,mt7925-common,rtw88_core,rtw89_8851b,rtw89_8852a,rtw89_8852b_common,rtw89_8852c,rtw89_8922a,rtw89_core | ath10k_core,ath11k,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7921-common,mt7925-common,rtw88_core,rtw89_8851b,rtw89_8852a,rtw89_8852b_common,rtw89_8852c,rtw89_8922a,rtw89_core |
| `ieee80211_freq_khz_to_channel` | ath11k,ath12k,brcmfmac,iwlmld,iwlmvm,mt76-connac-lib,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw89_core | ath11k,ath12k,brcmfmac,brcmfmac-cyw,iwlmld,iwlmvm,mt76-connac-lib,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw89_core |
| `ieee80211_set_active_links` | ath12k,iwlmld,iwlmvm | ath12k,iwlmld,iwlmvm,rtw89_core |
| `ioremap` | amdgpu,i915,radeon,ttm,ath11k,brcmfmac | amdgpu,i915,radeon,ttm,ath11k,ath12k,brcmfmac |
| `iounmap` | amdgpu,i915,radeon,ttm,xe,ath11k,brcmfmac | amdgpu,i915,radeon,ttm,xe,ath11k,ath12k,brcmfmac |
| `is_vmalloc_addr` | i915,ttm,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_pci,rtw89_pci | i915,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_pci,rtw89_pci |
| `kfree` | amdgpu,drm_display_helper,drm,drm_buddy,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath,ath10k_core,ath10k_pci,ath11k,ath11k_pci,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt792x-lib,mt7996e,rtw88_core,rtw89_core | amdgpu,drm_display_helper,drm,drm_buddy,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath,ath10k_core,ath10k_pci,ath11k,ath11k_pci,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt792x-lib,mt7996e,rtw88_core,rtw89_core |
| `ktime_get_real_seconds` | amdgpu,i915 | amdgpu |
| `memcpy` | amdgpu,drm_display_helper,drm,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt76-connac-lib,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw88_core,rtw88_pci,rtw89_core,rtw89_pci | amdgpu,drm_display_helper,drm,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,iwlmld,iwlmvm,mt76,mt76-connac-lib,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw88_core,rtw88_pci,rtw89_core,rtw89_pci |
| `memdup_user` | drm | amdgpu,drm |
| `mhi_power_down_keep_dev` | ath12k | ath11k_pci,ath12k |
| `page_offset_base` | amdgpu,drm,i915,radeon,ttm,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7925-common,rtw88_pci,rtw89_pci | amdgpu,drm,i915,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7925-common,rtw88_pci,rtw89_pci |
| `phys_base` | amdgpu,i915,ttm,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_pci,rtw89_pci | amdgpu,i915,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_pci,rtw89_pci |
| `register_pm_notifier` | amdgpu | amdgpu,xe,ath11k |
| `regulatory_set_wiphy_regd` | ath11k,iwlmld,iwlmvm | ath11k,ath12k,iwlmld,iwlmvm |
| `regulatory_set_wiphy_regd_sync` | ath12k,iwlmld,iwlmvm | iwlmld,iwlmvm |
| `rep_movs_alternative` | i915,xe | i915 |
| `rfkill_pause_polling` | mt7921e,rtw89_core | mt7921e,mt7925e,rtw89_core |
| `rtnl_lock` | ath12k,brcmfmac,iwlmld,iwlmvm | brcmfmac,iwlmld,iwlmvm |
| `rtnl_unlock` | ath12k,brcmfmac,iwlmld,iwlmvm | brcmfmac,iwlmld,iwlmvm |
| `unregister_pm_notifier` | amdgpu | amdgpu,xe,ath11k |
| `vmalloc_to_page` | ttm | ttm,xe |
| `wait_for_completion_timeout` | amdgpu,drm,drm_kms_helper,i915,xe,ath10k_core,ath11k,ath12k,brcmfmac,mt76,rtw88_core,rtw89_core | amdgpu,drm,drm_kms_helper,i915,xe,ath10k_core,ath11k,ath12k,brcmfmac,brcmfmac-cyw,mt76,rtw88_core,rtw89_core |
| `wiphy_rfkill_set_hw_state_reason` | ath10k_core,ath12k,iwlmld,iwlmvm,mt7921-common,rtw89_core | ath10k_core,ath12k,iwlmld,iwlmvm,mt7921-common,mt7925-common,rtw89_core |
| `wiphy_rfkill_start_polling` | mt7921-common,rtw89_core | mt7921-common,mt7925-common,rtw89_core |

