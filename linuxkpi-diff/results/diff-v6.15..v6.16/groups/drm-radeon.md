# Interfaces used by drm/radeon: v6.15 → v6.16

## Symbol-level summary

| | count |
|---|---|
| interfaces used in v6.15 | 274 |
| interfaces used in v6.16 | 272 |
| likely renames | 1 |
| newly used (excluding renames) | 0 |
| no longer used (excluding renames) | 2 |
| export kind/owner/namespace changed | 0 |
| used in both, own declaration changed | 1 |
| changed types reachable from used interfaces | 56 |

## Likely renames

Dropped and newly used symbols with identical signatures (types and parameter names) and similar names.

| v6.15 | v6.16 | signature | used by |
|---|---|---|---|
| `init_timer_key` | `timer_init_key` | `void(struct timer_list* timer, fn(struct timer_list*)->void* func, unsigned int flags, const char* name, struct lock_class_key* key)` | amdgpu,drm,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw88_core,rtw89_core |

## Newly used in v6.16

None.

## No longer used in v6.16

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `console_lock` | func | vmlinux | plain | kernel/printk/printk.c | radeon |
| `console_unlock` | func | vmlinux | plain | kernel/printk/printk.c | radeon |

## Interfaces whose own declaration changed

Return/parameter types, variable types, or interfaces that lost their debug info. `[C]` changed, `[D]` deleted.

**[D] 'cpuinfo_x86 boot_cpu_data'    {boot_cpu_data}** (vmlinux)

## Changed types

Each changed type reachable from an interface this group uses, with the number of those interfaces it reaches, fewest first: low counts are targeted changes, high counts are churn reached through hub types (reachability is transitive through pointers, so e.g. `struct device` or `struct module` pull in hundreds).

| type | declared at | change | used interfaces reached |
|---|---|---|---|
| `struct file_operations` | fs.h:2129:1 | type size changed from 2112 to 2176 (in bits); 1 data member insertion | 1 |
| `struct i2c_board_info` | i2c.h:426:1 | type size changed from 640 to 576 (in bits); 1 data member deletion; there are data member changes | 1 |
| `struct backlight_device` | backlight.h:247:1 | type size changed from 7168 to 6720 (in bits); 2 data member deletions; there are data member changes | 3 |
| `struct pci_dev` | pci.h:332:1 | type size changed from 16768 to 16704 (in bits); 1 data member deletion; there are data member changes | 34 |
| `enum hwtstamp_source` | net_tstamp.h:16:1 | 1 enumerator deletion | 134 |
| `enum perf_event_state` | perf_event.h:624:1 | 1 enumerator insertion; 1 enumerator change | 134 |
| `struct bio` | blk_types.h:214:1 | 1 data member insertion; there are data member changes | 134 |
| `struct fib6_info` | ip6_fib.h:158:1 | type size changed from 1472 to 1600 (in bits); 1 data member insertion; there are data member changes | 134 |
| `struct folio_queue` | folio_queue.h:30:1 | type size changed from 2688 to 2624 (in bits); 1 data member deletion; there are data member changes | 134 |
| `struct gendisk` | blkdev.h:142:1 | type size changed from 4544 to 4736 (in bits); 1 data member deletion; 1 data member insertion; there are data member changes | 134 |
| `struct hw_perf_event` | perf_event.h:155:1 | type size changed from 1536 to 1664 (in bits); there are data member changes | 134 |
| `struct io_ring_ctx` | io_uring_types.h:239:1 | 1 data member deletion; 2 data member insertions; there are data member changes | 134 |
| `struct iommu_device` | iommu.h:754:1 | 1 data member insertion | 134 |
| `struct iommu_iotlb_gather` | iommu.h:362:1 | there are data member changes | 134 |
| `struct iommu_ops` | iommu.h:627:1 | type size changed from 1728 to 1600 (in bits); 2 data member deletions; there are data member changes | 134 |
| `struct kernel_ethtool_ts_info` | ethtool.h:763:1 | type size changed from 192 to 256 (in bits); 2 data member insertions; there are data member changes | 134 |
| `struct linux_binfmt` | binfmts.h:89:1 | type size changed from 448 to 384 (in bits); 1 data member deletion; there are data member changes | 134 |
| `struct linux_mib` | snmp.h:104:1 | type size changed from 8576 to 8640 (in bits); there are data member changes | 134 |
| `struct mnt_namespace` | mount.h:14:1 | 1 data member deletion | 134 |
| `struct msi_domain_info` | msi.h:491:1 | type size changed from 576 to 640 (in bits); 1 data member insertion; there are data member changes | 134 |
| `struct msi_domain_ops` | msi.h:448:1 | type size changed from 640 to 704 (in bits); 1 data member insertion; there are data member changes | 134 |
| `struct net` | net_namespace.h:61:1 | there are data member changes | 134 |
| `struct net_device` | netdevice.h:2080:1 | 1 data member insertion; there are data member changes | 134 |
| `struct netlink_ext_ack` | netlink.h:82:1 | type size changed from 1088 to 1024 (in bits); there are data member changes | 134 |
| `struct nexthop` | nexthop.h:142:1 | 2 data member insertions; there are data member changes | 134 |
| `struct page_pool` | types.h:162:1 | 1 data member insertion; there are data member changes | 134 |
| `struct per_cpu_zonestat` | mmzone.h:728:1 | there are data member changes | 134 |
| `struct perf_cgroup` | perf_event.h:1123:1 | there are data member changes | 134 |
| `struct perf_event` | perf_event.h:708:1 | type size changed from 8768 to 9024 (in bits); 1 data member insertion; there are data member changes | 134 |
| `struct pglist_data` | mmzone.h:1341:1 | type size changed from 114688 to 112640 (in bits); there are data member changes | 134 |
| `struct phy_driver` | phy.h:898:1 | there are data member changes | 134 |
| `struct pmu` | perf_event.h:325:1 | type size changed from 2368 to 2560 (in bits); 2 data member insertions; there are data member changes | 134 |
| `struct queue_limits` | blkdev.h:365:1 | type size changed from 1408 to 1472 (in bits); 2 data member insertions; there are data member changes | 134 |
| `struct request_queue` | blkdev.h:459:1 | type size changed from 7680 to 7744 (in bits); there are data member changes | 134 |
| `struct rq` | sched.h:1097:1 | type size changed from 26112 to 26624 (in bits); there are data member changes | 134 |
| `struct sock` | sock.h:345:1 | type size hasn't changed | 134 |
| `struct task_group` | sched.h:431:1 | there are data member changes | 134 |
| `struct trace_array` | trace.h:326:1 | type size changed from 3328 to 3456 (in bits); 1 data member insertion; there are data member changes | 134 |
| `struct trace_array_cpu` | trace.h:185:1 | type size changed from 1024 to 960 (in bits); 1 data member deletion; there are data member changes | 134 |
| `struct zone` | mmzone.h:845:1 | type size changed from 10240 to 9728 (in bits); there are data member changes | 134 |
| `struct address_space_operations` | fs.h:435:1 | type size changed from 1280 to 1216 (in bits); 1 data member deletion; there are data member changes | 135 |
| `struct cgroup` | cgroup-defs.h:412:1 | type size changed from 9216 to 8704 (in bits); 2 data member deletions; there are data member changes | 135 |
| `struct cgroup_root` | cgroup-defs.h:577:1 | type size changed from 43520 to 43008 (in bits); there are data member changes | 135 |
| `struct cgroup_subsys` | cgroup-defs.h:706:1 | type size changed from 2048 to 2112 (in bits); 2 data member insertions | 135 |
| `struct dir_context` | fs.h:2071:1 | type size changed from 128 to 192 (in bits); 1 data member insertion | 135 |
| `struct kiocb` | fs.h:404:1 | 1 data member insertion | 135 |
| `struct kstat` | stat.h:22:1 | type size changed from 1472 to 1536 (in bits); 1 data member insertion; there are data member changes | 135 |
| `struct mod_arch_specific` | module.h:8:1 | type size changed from 192 to 320 (in bits); 1 data member insertion | 135 |
| `struct module` | module.h:414:1 | 2 data member deletions; there are data member changes | 135 |
| `struct sb_writers` | fs.h:1306:1 | type size changed from 2432 to 2496 (in bits); 1 data member insertion; there are data member changes | 135 |
| `struct super_block` | fs.h:1313:1 | type size changed from 10240 to 10752 (in bits); there are data member changes | 135 |
| `struct super_operations` | fs.h:2287:1 | there are data member changes | 135 |
| `struct task_struct` | sched.h:813:1 | type size changed from 58880 to 24576 (in bits); 1 data member insertion; there are data member changes | 135 |
| `struct user_struct` | user.h:14:1 | there are data member changes | 135 |
| `struct vm_area_struct` | mm_types.h:779:1 | 1 data member insertion | 135 |
| `struct ratelimit_state` | ratelimit_types.h:15:1 | there are data member changes | 136 |

### Details

<details><summary><code>struct file_operations</code> (fs.h:2129:1)</summary>

```
  type size changed from 2112 to 2176 (in bits)
  1 data member insertion:
    'int (vm_area_desc*)* mmap_prepare', at offset 2112 (in bits) at fs.h:2194:1
```

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`

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

Reaches: `function backlight_device* backlight_device_register(const char*, device*, void*, const backlight_ops*, const backlight_properties*)`, `function void backlight_device_unregister(backlight_device*)`, `function void backlight_force_update(backlight_device*, backlight_update_reason)`

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function agp_bridge_data* agp_backend_acquire(pci_dev*)`, `function void agp_backend_release(agp_bridge_data*)`, `function int agp_copy_info(agp_bridge_data*, agp_kern_info*)`, `function void agp_enable(agp_bridge_data*, u32)`, `function int aperture_remove_conflicting_pci_devices(pci_dev*, const char*)`, `function void pci_clear_master(pci_dev*)`, `function void pci_dev_put(pci_dev*)`, `function void pci_disable_device(pci_dev*)`, `function void pci_disable_msi(pci_dev*)`, `function int pci_enable_device(pci_dev*)`, `function int pci_enable_msi(pci_dev*)`, `function u8 pci_find_capability(pci_dev*, int)`, `function pci_dev* pci_get_base_class(unsigned int, pci_dev*)` … (+19 more)

</details>

<details><summary><code>enum hwtstamp_source</code> (net_tstamp.h:16:1)</summary>

```
  type size hasn't changed
  1 enumerator deletion:
    'hwtstamp_source::HWTSTAMP_SOURCE_UNSPEC' value '0'
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

</details>

<details><summary><code>enum perf_event_state</code> (perf_event.h:624:1)</summary>

```
  type size hasn't changed
  1 enumerator insertion:
    'perf_event_state::PERF_EVENT_STATE_REVOKED' value '-4'
  1 enumerator change:
    'perf_event_state::PERF_EVENT_STATE_DEAD' from value '-4' to '-5' at perf_event.h:679:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

</details>

<details><summary><code>struct bio</code> (blk_types.h:214:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u8 bi_write_stream', at offset 200 (in bits) at blk_types.h:223:1
  there are data member changes:
    'blk_status_t bi_status' offset changed from 200 to 208 (in bits) (by +8 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

</details>

<details><summary><code>struct iommu_device</code> (iommu.h:754:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'bool ready', at offset 416 (in bits) at iommu.h:756:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

</details>

<details><summary><code>struct mnt_namespace</code> (mount.h:14:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'mntns_flags_t mntns_flags', at offset 1504 (in bits) at mount.h:40:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

</details>

<details><summary><code>struct msi_domain_info</code> (msi.h:491:1)</summary>

```
  type size changed from 576 to 640 (in bits)
  1 data member insertion:
    'msi_alloc_info_t* alloc_data', at offset 512 (in bits) at msi.h:509:1
  there are data member changes:
    'void* data' offset changed from 512 to 576 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

</details>

<details><summary><code>struct perf_cgroup</code> (perf_event.h:1123:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cgroup_subsys_state' of 'perf_cgroup::css' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

</details>

<details><summary><code>struct phy_driver</code> (phy.h:898:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int (phy_device*)*' of 'phy_driver::match_phy_device' changed:
      pointer type changed from: 'int (phy_device*)*' to: 'int (phy_device*, const phy_driver*)*'
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

</details>

<details><summary><code>struct sock</code> (sock.h:345:1)</summary>

```
  type size hasn't changed
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

</details>

<details><summary><code>struct task_group</code> (sched.h:431:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cgroup_subsys_state' of 'task_group::css' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)`, `function bool __trace_trigger_soft_disabled(trace_event_file*)` … (+119 more)

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

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

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

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

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

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

</details>

<details><summary><code>struct cgroup_subsys</code> (cgroup-defs.h:706:1)</summary>

```
  type size changed from 2048 to 2112 (in bits)
  2 data member insertions:
    'spinlock_t rstat_ss_lock', at offset 2016 (in bits) at cgroup-defs.h:823:1
    'raw_spinlock_t* rstat_ss_cpu_lock', at offset 2048 (in bits) at cgroup-defs.h:824:1
```

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

</details>

<details><summary><code>struct dir_context</code> (fs.h:2071:1)</summary>

```
  type size changed from 128 to 192 (in bits)
  1 data member insertion:
    'int count', at offset 128 (in bits) at fs.h:2092:1
```

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

</details>

<details><summary><code>struct kiocb</code> (fs.h:404:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u8 ki_write_stream', at offset 304 (in bits) at fs.h:413:1
```

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

</details>

<details><summary><code>struct kstat</code> (stat.h:22:1)</summary>

```
  type size changed from 1472 to 1536 (in bits)
  1 data member insertion:
    'u32 atomic_write_unit_max_opt', at offset 1440 (in bits) at stat.h:60:1
  there are data member changes:
    'u32 atomic_write_segments_max' offset changed from 1440 to 1472 (in bits) (by +32 bits)
```

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

</details>

<details><summary><code>struct mod_arch_specific</code> (module.h:8:1)</summary>

```
  type size changed from 192 to 320 (in bits)
  1 data member insertion:
    'its_array its_pages', at offset 192 (in bits) at module.h:21:1
```

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

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

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

</details>

<details><summary><code>struct sb_writers</code> (fs.h:1306:1)</summary>

```
  type size changed from 2432 to 2496 (in bits)
  1 data member insertion:
    'void* freeze_owner', at offset 128 (in bits) at fs.h:1321:1
  there are data member changes:
    'percpu_rw_semaphore rw_sem[3]' offset changed from 128 to 192 (in bits) (by +64 bits)
```

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

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

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

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

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

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

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

</details>

<details><summary><code>struct user_struct</code> (user.h:14:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct ratelimit_state' of 'user_struct::ratelimit' changed, as reported earlier
```

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

</details>

<details><summary><code>struct vm_area_struct</code> (mm_types.h:779:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'pfnmap_track_ctx* pfnmap_track_ctx', at offset 1344 (in bits) at mm_types.h:913:1
```

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)`, `function void __pm_runtime_use_autosuspend(device*, bool)` … (+120 more)

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

Reaches: `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const kernel_param_ops param_ops_int`, `function int ___ratelimit(ratelimit_state*, const char*)`, `function void __folio_put(folio*)`, `function void __free_pages(page*, unsigned int)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __mmap_lock_do_trace_acquire_returned(mm_struct*, bool, bool)`, `function void __mmap_lock_do_trace_released(mm_struct*, bool)`, `function void __mmap_lock_do_trace_start_locking(mm_struct*, bool)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __pm_runtime_disable(device*, bool)`, `function int __pm_runtime_resume(device*, int)`, `function int __pm_runtime_set_status(device*, unsigned int)`, `function int __pm_runtime_suspend(device*, int)` … (+121 more)

</details>

## Header-level interfaces

Macros, static inline functions, struct/union/enum tags, typedefs and enumerators defined in provider headers (headers the consumer objects were compiled against that are not consumer code) and named in consumer code. They never appear as ELF symbols, but LinuxKPI has to provide them. Name-based, so an occasional false positive is possible (e.g. a local variable or member sharing a macro's name).

| | count |
|---|---|
| used in v6.15 | 673 |
| used in v6.16 | 674 |
| newly used | 0 |
| no longer used | 0 |
| likely renames | 0 |
| macro/inline signature changed | 0 |
| macro body changed | 1 |
| moved to another header | 0 |

### Likely renames (header)

None.

### Newly used (header)

None.

### No longer used (header)

None.

### Signature changed (header)

None.

<details><summary>Macro body changed (1)</summary>

| macro | header | v6.15 | v6.16 |
|---|---|---|---|
| `MODULE_DEVICE_TABLE` | include/linux/module.h | `extern typeof(name) __mod_device_table__##type##__##name __attribute__ ((unused, alias(__stringify(name))))` | `static typeof(name) __mod_device_table__##type##__##name __attribute__ ((used, alias(__stringify(name))))` |

</details>

## Same interface, different set of users

| symbol | v6.15 | v6.16 |
|---|---|---|
| `__kmalloc_noprof` | amdgpu,drm_display_helper,drm,drm_buddy,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath11k_pci,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,rtw88_core,rtw89_core | amdgpu,drm_display_helper,drm,drm_buddy,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath11k_pci,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,iwlmld,iwlmvm,mt76,rtw88_core,rtw89_core |
| `__x86_indirect_thunk_r8` | amdgpu,drm,drm_gpuvm,drm_kms_helper,i915,radeon,xe,mt76,mt7615-common,mt7915e,mt7996e,rtw88_8822c,rtw88_core,rtw89_8851b,rtw89_8852a,rtw89_8852b_common,rtw89_core,rtw89_pci | amdgpu,drm,drm_gpuvm,drm_kms_helper,i915,radeon,xe,ath12k,mt76,mt7615-common,mt7915e,mt7996e,rtw88_8822c,rtw88_core,rtw89_8851b,rtw89_8852a,rtw89_8852b_common,rtw89_core,rtw89_pci |
| `__x86_indirect_thunk_rax` | amdgpu,drm_display_helper,drm,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7615e,mt7915e,mt7921-common,mt7921e,mt7925-common,mt7925e,mt792x-lib,mt7996e,rtw88_8723d,rtw88_8723x,rtw88_8814a,rtw88_8821c,rtw88_8822b,rtw88_8822c,rtw88_core,rtw88_pci,rtw89_8851b,rtw89_8852a,rtw89_8852b,rtw89_8852b_common,rtw89_8852bt,rtw89_8852c,rtw89_8922a,rtw89_core,rtw89_pci | amdgpu,drm_display_helper,drm,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7615e,mt7915e,mt7921-common,mt7921e,mt7925-common,mt7925e,mt792x-lib,mt7996e,rtw88_8723d,rtw88_8723x,rtw88_8814a,rtw88_8821c,rtw88_8822b,rtw88_8822c,rtw88_core,rtw88_pci,rtw89_8851b,rtw89_8852a,rtw89_8852b,rtw89_8852b_common,rtw89_8852bt,rtw89_8852c,rtw89_8922a,rtw89_core,rtw89_pci |
| `dma_map_page_attrs` | amdgpu,radeon,ttm,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_pci,rtw89_pci | amdgpu,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_pci,rtw89_pci |
| `dma_unmap_page_attrs` | amdgpu,radeon,ttm,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt76-connac-lib,rtw88_pci,rtw89_pci | amdgpu,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt76-connac-lib,rtw88_pci,rtw89_pci |
| `flush_delayed_work` | amdgpu,i915,radeon,xe,iwlmld,iwlmvm | amdgpu,i915,radeon,xe,iwlmvm |
| `ioremap` | amdgpu,i915,radeon,ttm,ath11k,brcmfmac | amdgpu,i915,radeon,ttm,ath11k,ath12k,brcmfmac |
| `iounmap` | amdgpu,i915,radeon,ttm,xe,ath11k,brcmfmac | amdgpu,i915,radeon,ttm,xe,ath11k,ath12k,brcmfmac |
| `kfree` | amdgpu,drm_display_helper,drm,drm_buddy,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath,ath10k_core,ath10k_pci,ath11k,ath11k_pci,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt792x-lib,mt7996e,rtw88_core,rtw89_core | amdgpu,drm_display_helper,drm,drm_buddy,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath,ath10k_core,ath10k_pci,ath11k,ath11k_pci,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt792x-lib,mt7996e,rtw88_core,rtw89_core |
| `memcpy` | amdgpu,drm_display_helper,drm,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt76-connac-lib,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw88_core,rtw88_pci,rtw89_core,rtw89_pci | amdgpu,drm_display_helper,drm,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,iwlmld,iwlmvm,mt76,mt76-connac-lib,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw88_core,rtw88_pci,rtw89_core,rtw89_pci |
| `page_offset_base` | amdgpu,drm,i915,radeon,ttm,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7925-common,rtw88_pci,rtw89_pci | amdgpu,drm,i915,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7925-common,rtw88_pci,rtw89_pci |

