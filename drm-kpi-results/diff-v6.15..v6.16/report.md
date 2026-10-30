# Kernel interfaces used by DRM: v6.15 → v6.16

| | count |
|---|---|
| interfaces used in v6.15 | 1046 |
| interfaces used in v6.16 | 1050 |
| newly used | 11 |
| no longer used | 7 |
| export kind/owner/namespace changed | 0 |
| used in both, own declaration changed | 6 |
| changed types reachable from used interfaces | 70 |
| used interfaces reaching at least one changed type | 480 |

## Newly used in v6.16

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `compat_vma_mmap_prepare` | func | vmlinux | plain | mm/util.c | i915 |
| `dma_fence_dedup_array` | func | vmlinux | GPL | drivers/dma-buf/dma-fence-unwrap.c | amdgpu |
| `dma_resv_describe` | func | vmlinux | GPL | drivers/dma-buf/dma-resv.c | amdgpu |
| `folio_redirty_for_writepage` | func | vmlinux | plain | mm/page-writeback.c | i915 |
| `generic_handle_irq_safe` | func | vmlinux | GPL | kernel/irq/irqdesc.c | i915 |
| `intel_gmch_gtt_read_entry` | func | vmlinux | plain | drivers/char/agp/intel-gtt.c | i915 |
| `refcount_dec_not_one` | func | vmlinux | plain | lib/refcount.c | drm_shmem_helper |
| `shmem_writeout` | func | vmlinux | GPL | mm/shmem.c | i915,ttm |
| `sysfs_update_group` | func | vmlinux | GPL | fs/sysfs/group.c | amdgpu |
| `timer_init_key` | func | vmlinux | plain | kernel/time/timer.c | amdgpu,drm,drm_kms_helper,gpu-sched,i915,radeon,xe |
| `writeback_iter` | func | vmlinux | GPL | mm/page-writeback.c | i915 |

## No longer used in v6.16

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `clear_page_dirty_for_io` | func | vmlinux | plain | mm/folio-compat.c | i915 |
| `console_lock` | func | vmlinux | plain | kernel/printk/printk.c | radeon |
| `console_unlock` | func | vmlinux | plain | kernel/printk/printk.c | radeon |
| `init_timer_key` | func | vmlinux | plain | kernel/time/timer.c | amdgpu,drm,drm_kms_helper,gpu-sched,i915,radeon,xe |
| `llist_add_batch` | func | vmlinux | GPL | lib/llist.c | drm,i915,xe |
| `pagecache_get_page` | func | vmlinux | plain | mm/folio-compat.c | i915 |
| `sg_next` | func | vmlinux | plain | lib/scatterlist.c | amdgpu,drm,i915,ttm,virtio-gpu,xe |

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

Reaches 62 used interfaces.

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

Reaches 471 used interfaces.

**[D] phys_base** (vmlinux)

## Changed types

Each type that changed and is reachable from an interface DRM uses, with the number of used interfaces it reaches, fewest first: low counts are targeted changes, high counts are churn reached via hub types (reachability is transitive through pointers, so e.g. `struct device` or `struct module` pull in hundreds). Per-interface index: `impacted.tsv`; raw report: `abidiff-leaf.txt`.

| type | declared at | change | used interfaces reached |
|---|---|---|---|
| `struct drm_device` | drm_device.h:57:1 | type size changed from 12480 to 12608 (in bits); 1 data member insertion; there are data member changes | 1 |
| `struct i2c_board_info` | i2c.h:426:1 | type size changed from 640 to 576 (in bits); 1 data member deletion; there are data member changes | 1 |
| `struct dma_fence_ops` | dma-fence.h:126:1 | type size changed from 640 to 512 (in bits); 2 data member deletions; there are data member changes | 2 |
| `struct platform_device_id` | mod_devicetable.h:607:1 | there are data member changes | 2 |
| `struct backlight_device` | backlight.h:247:1 | type size changed from 7168 to 6720 (in bits); 2 data member deletions; there are data member changes | 7 |
| `struct file_operations` | fs.h:2129:1 | type size changed from 2112 to 2176 (in bits); 1 data member insertion | 8 |
| `struct dma_buf_attachment` | dma-buf.h:513:1 | type size changed from 576 to 512 (in bits); 2 data member deletions; there are data member changes | 20 |
| `struct dma_buf_ops` | dma-buf.h:36:1 | type size changed from 832 to 768 (in bits); 1 data member deletion; there are data member changes | 20 |
| `struct pci_dev` | pci.h:332:1 | type size changed from 16768 to 16704 (in bits); 1 data member deletion; there are data member changes | 82 |
| `enum hwtstamp_source` | net_tstamp.h:16:1 | 1 enumerator deletion | 471 |
| `enum perf_event_state` | perf_event.h:624:1 | 1 enumerator insertion; 1 enumerator change | 471 |
| `struct bio` | blk_types.h:214:1 | 1 data member insertion; there are data member changes | 471 |
| `struct blk_mq_tag_set` | blk-mq.h:510:1 | type size changed from 1344 to 1664 (in bits); 1 data member insertion | 471 |
| `struct blkcg` | blk-cgroup.h:94:1 | there are data member changes | 471 |
| `struct coredump_params` | coredump.h:19:1 | type size changed from 704 to 768 (in bits); 1 data member insertion | 471 |
| `struct fib6_info` | ip6_fib.h:158:1 | type size changed from 1472 to 1600 (in bits); 1 data member insertion; there are data member changes | 471 |
| `struct folio_queue` | folio_queue.h:30:1 | type size changed from 2688 to 2624 (in bits); 1 data member deletion; there are data member changes | 471 |
| `struct gendisk` | blkdev.h:142:1 | type size changed from 4544 to 4736 (in bits); 1 data member deletion; 1 data member insertion; there are data member changes | 471 |
| `struct hw_perf_event` | perf_event.h:155:1 | type size changed from 1536 to 1664 (in bits); there are data member changes | 471 |
| `struct io_ring_ctx` | io_uring_types.h:239:1 | 1 data member deletion; 2 data member insertions; there are data member changes | 471 |
| `struct iommu_device` | iommu.h:754:1 | 1 data member insertion | 471 |
| `struct iommu_iotlb_gather` | iommu.h:362:1 | there are data member changes | 471 |
| `struct iommu_ops` | iommu.h:627:1 | type size changed from 1728 to 1600 (in bits); 2 data member deletions; there are data member changes | 471 |
| `struct iova_fq_entry` | dma-iommu.c:105:1 | there are data member changes | 471 |
| `struct kernel_ethtool_ts_info` | ethtool.h:763:1 | type size changed from 192 to 256 (in bits); 2 data member insertions; there are data member changes | 471 |
| `struct kernfs_root` | kernfs-internal.h:36:1 | type size changed from 1856 to 1984 (in bits); 2 data member insertions; there are data member changes | 471 |
| `struct linux_binfmt` | binfmts.h:89:1 | type size changed from 448 to 384 (in bits); 1 data member deletion; there are data member changes | 471 |
| `struct linux_mib` | snmp.h:104:1 | type size changed from 8576 to 8640 (in bits); there are data member changes | 471 |
| `struct mnt_namespace` | mount.h:14:1 | 1 data member deletion | 471 |
| `struct msi_domain_info` | msi.h:491:1 | type size changed from 576 to 640 (in bits); 1 data member insertion; there are data member changes | 471 |
| `struct msi_domain_ops` | msi.h:448:1 | type size changed from 640 to 704 (in bits); 1 data member insertion; there are data member changes | 471 |
| `struct net` | net_namespace.h:61:1 | there are data member changes | 471 |
| `struct net_device` | netdevice.h:2080:1 | 1 data member insertion; there are data member changes | 471 |
| `struct netlink_ext_ack` | netlink.h:82:1 | type size changed from 1088 to 1024 (in bits); there are data member changes | 471 |
| `struct nexthop` | nexthop.h:142:1 | 2 data member insertions; there are data member changes | 471 |
| `struct nfs_client` | nfs_fs_sb.h:29:1 | 1 data member insertion | 471 |
| `struct page_pool` | types.h:162:1 | 1 data member insertion; there are data member changes | 471 |
| `struct per_cpu_zonestat` | mmzone.h:728:1 | there are data member changes | 471 |
| `struct perf_cgroup` | perf_event.h:1123:1 | there are data member changes | 471 |
| `struct perf_event` | perf_event.h:708:1 | type size changed from 8768 to 9024 (in bits); 1 data member insertion; there are data member changes | 471 |
| `struct pglist_data` | mmzone.h:1341:1 | type size changed from 114688 to 112640 (in bits); there are data member changes | 471 |
| `struct phy_driver` | phy.h:898:1 | there are data member changes | 471 |
| `struct pmu` | perf_event.h:325:1 | type size changed from 2368 to 2560 (in bits); 2 data member insertions; there are data member changes | 471 |
| `struct queue_limits` | blkdev.h:365:1 | type size changed from 1408 to 1472 (in bits); 2 data member insertions; there are data member changes | 471 |
| `struct request_queue` | blkdev.h:459:1 | type size changed from 7680 to 7744 (in bits); there are data member changes | 471 |
| `struct rpc_rqst` | xprt.h:54:1 | type size changed from 3520 to 3648 (in bits); 1 data member insertion; there are data member changes | 471 |
| `struct rq` | sched.h:1097:1 | type size changed from 26112 to 26624 (in bits); there are data member changes | 471 |
| `struct sock` | sock.h:345:1 | type size hasn't changed | 471 |
| `struct svc_rqst` | svc.h:166:1 | type size changed from 92544 to 9792 (in bits); 1 data member deletion; 1 data member insertion; there are data member changes | 471 |
| `struct svc_xprt` | svc_xprt.h:52:1 | type size changed from 4160 to 4224 (in bits); 1 data member insertion; there are data member changes | 471 |
| `struct task_group` | sched.h:431:1 | there are data member changes | 471 |
| `struct trace_array` | trace.h:326:1 | type size changed from 3328 to 3456 (in bits); 1 data member insertion; there are data member changes | 471 |
| `struct trace_array_cpu` | trace.h:185:1 | type size changed from 1024 to 960 (in bits); 1 data member deletion; there are data member changes | 471 |
| `struct zone` | mmzone.h:845:1 | type size changed from 10240 to 9728 (in bits); there are data member changes | 471 |
| `struct cgroup` | cgroup-defs.h:412:1 | type size changed from 9216 to 8704 (in bits); 2 data member deletions; there are data member changes | 477 |
| `struct cgroup_root` | cgroup-defs.h:577:1 | type size changed from 43520 to 43008 (in bits); there are data member changes | 477 |
| `struct cgroup_subsys` | cgroup-defs.h:706:1 | type size changed from 2048 to 2112 (in bits); 2 data member insertions | 477 |
| `struct address_space_operations` | fs.h:435:1 | type size changed from 1280 to 1216 (in bits); 1 data member deletion; there are data member changes | 479 |
| `struct dir_context` | fs.h:2071:1 | type size changed from 128 to 192 (in bits); 1 data member insertion | 479 |
| `struct kiocb` | fs.h:404:1 | 1 data member insertion | 479 |
| `struct kstat` | stat.h:22:1 | type size changed from 1472 to 1536 (in bits); 1 data member insertion; there are data member changes | 479 |
| `struct mod_arch_specific` | module.h:8:1 | type size changed from 192 to 320 (in bits); 1 data member insertion | 479 |
| `struct module` | module.h:414:1 | 2 data member deletions; there are data member changes | 479 |
| `struct sb_writers` | fs.h:1306:1 | type size changed from 2432 to 2496 (in bits); 1 data member insertion; there are data member changes | 479 |
| `struct super_block` | fs.h:1313:1 | type size changed from 10240 to 10752 (in bits); there are data member changes | 479 |
| `struct super_operations` | fs.h:2287:1 | there are data member changes | 479 |
| `struct task_struct` | sched.h:813:1 | type size changed from 58880 to 24576 (in bits); 1 data member insertion; there are data member changes | 479 |
| `struct user_struct` | user.h:14:1 | there are data member changes | 479 |
| `struct vm_area_struct` | mm_types.h:779:1 | 1 data member insertion | 479 |
| `struct ratelimit_state` | ratelimit_types.h:15:1 | there are data member changes | 480 |

### Details

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

<details><summary><code>struct dma_fence_ops</code> (dma-fence.h:126:1)</summary>

```
  type size changed from 640 to 512 (in bits)
  2 data member deletions:
    'void (dma_fence*, char*, int)* fence_value_str', at offset 448 (in bits) at dma-fence.h:249:1
    'void (dma_fence*, char*, int)* timeline_value_str', at offset 512 (in bits) at dma-fence.h:259:1
  there are data member changes:
    'void (dma_fence*, typedef ktime_t)* set_deadline' offset changed from 576 to 448 (in bits) (by -128 bits)
```

Reaches: `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`

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

Reaches: `function platform_device* platform_device_register_full(const platform_device_info*)`, `function void platform_device_unregister(platform_device*)`

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

<details><summary><code>struct file_operations</code> (fs.h:2129:1)</summary>

```
  type size changed from 2112 to 2176 (in bits)
  1 data member insertion:
    'int (vm_area_desc*)* mmap_prepare', at offset 2112 (in bits) at fs.h:2194:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`

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

Reaches: `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `function dma_buf_attachment* dma_buf_attach(dma_buf*, device*)`, `function int dma_buf_begin_cpu_access(dma_buf*, dma_data_direction)`, `function void dma_buf_detach(dma_buf*, dma_buf_attachment*)`, `function dma_buf_attachment* dma_buf_dynamic_attach(dma_buf*, device*, const dma_buf_attach_ops*, void*)`, `function int dma_buf_end_cpu_access(dma_buf*, dma_data_direction)`, `function dma_buf* dma_buf_export(const dma_buf_export_info*)`, `function dma_buf* dma_buf_get(int)`, `function sg_table* dma_buf_map_attachment(dma_buf_attachment*, dma_data_direction)`, `function sg_table* dma_buf_map_attachment_unlocked(dma_buf_attachment*, dma_data_direction)`, `function int dma_buf_mmap(dma_buf*, vm_area_struct*, unsigned long int)`, `function void dma_buf_move_notify(dma_buf*)`, `function int dma_buf_pin(dma_buf_attachment*)`, `function void dma_buf_put(dma_buf*)` … (+5 more, see impacted.tsv)

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

Reaches: `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `function dma_buf_attachment* dma_buf_attach(dma_buf*, device*)`, `function int dma_buf_begin_cpu_access(dma_buf*, dma_data_direction)`, `function void dma_buf_detach(dma_buf*, dma_buf_attachment*)`, `function dma_buf_attachment* dma_buf_dynamic_attach(dma_buf*, device*, const dma_buf_attach_ops*, void*)`, `function int dma_buf_end_cpu_access(dma_buf*, dma_data_direction)`, `function dma_buf* dma_buf_export(const dma_buf_export_info*)`, `function dma_buf* dma_buf_get(int)`, `function sg_table* dma_buf_map_attachment(dma_buf_attachment*, dma_data_direction)`, `function sg_table* dma_buf_map_attachment_unlocked(dma_buf_attachment*, dma_data_direction)`, `function int dma_buf_mmap(dma_buf*, vm_area_struct*, unsigned long int)`, `function void dma_buf_move_notify(dma_buf*)`, `function int dma_buf_pin(dma_buf_attachment*)`, `function void dma_buf_put(dma_buf*)` … (+5 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function agp_memory* agp_allocate_memory(agp_bridge_data*, size_t, u32)`, `function agp_bridge_data* agp_backend_acquire(pci_dev*)`, `function void agp_backend_release(agp_bridge_data*)`, `function int agp_bind_memory(agp_memory*, off_t)`, `function int agp_copy_info(agp_bridge_data*, agp_kern_info*)`, `function void agp_enable(agp_bridge_data*, u32)`, `function void agp_free_memory(agp_memory*)`, `function int agp_unbind_memory(agp_memory*)`, `function int aperture_remove_conflicting_pci_devices(pci_dev*, const char*)`, `function int intel_gmch_probe(pci_dev*, pci_dev*, agp_bridge_data*)`, `function int pci_alloc_irq_vectors(pci_dev*, unsigned int, unsigned int, unsigned int)`, `function void pci_assign_unassigned_bus_resources(pci_bus*)`, `function int pci_bus_alloc_resource(pci_bus*, resource*, resource_size_t, resource_size_t, resource_size_t, unsigned long int, resource_alignf, void*)` … (+67 more, see impacted.tsv)

</details>

<details><summary><code>enum hwtstamp_source</code> (net_tstamp.h:16:1)</summary>

```
  type size hasn't changed
  1 enumerator deletion:
    'hwtstamp_source::HWTSTAMP_SOURCE_UNSPEC' value '0'
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>enum perf_event_state</code> (perf_event.h:624:1)</summary>

```
  type size hasn't changed
  1 enumerator insertion:
    'perf_event_state::PERF_EVENT_STATE_REVOKED' value '-4'
  1 enumerator change:
    'perf_event_state::PERF_EVENT_STATE_DEAD' from value '-4' to '-5' at perf_event.h:679:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct bio</code> (blk_types.h:214:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u8 bi_write_stream', at offset 200 (in bits) at blk_types.h:223:1
  there are data member changes:
    'blk_status_t bi_status' offset changed from 200 to 208 (in bits) (by +8 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct blk_mq_tag_set</code> (blk-mq.h:510:1)</summary>

```
  type size changed from 1344 to 1664 (in bits)
  1 data member insertion:
    'rw_semaphore update_nr_hwq_lock', at offset 1344 (in bits) at blk-mq.h:535:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct blkcg</code> (blk-cgroup.h:94:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cgroup_subsys_state' of 'blkcg::css' changed:
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
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct coredump_params</code> (coredump.h:19:1)</summary>

```
  type size changed from 704 to 768 (in bits)
  1 data member insertion:
    'pid* pid', at offset 704 (in bits) at coredump.h:31:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct iommu_device</code> (iommu.h:754:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'bool ready', at offset 416 (in bits) at iommu.h:756:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct iova_fq_entry</code> (dma-iommu.c:105:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct list_head' of 'iova_fq_entry::freelist' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct kernfs_root</code> (kernfs-internal.h:36:1)</summary>

```
  type size changed from 1856 to 1984 (in bits)
  2 data member insertions:
    'spinlock_t kernfs_idr_lock', at offset 320 (in bits) at kernfs-internal.h:41:1
    'rwlock_t kernfs_rename_lock', at offset 1792 (in bits) at kernfs-internal.h:55:1
  there are data member changes:
    'u32 last_id_lowbits' offset changed from 320 to 352 (in bits) (by +32 bits)
    'u32 id_highbits' offset changed from 352 to 384 (in bits) (by +32 bits)
    'kernfs_syscall_ops* syscall_ops' offset changed from 384 to 448 (in bits) (by +64 bits)
    'list_head supers' offset changed from 448 to 512 (in bits) (by +64 bits)
    'wait_queue_head_t deactivate_waitq' offset changed from 576 to 640 (in bits) (by +64 bits)
    'rw_semaphore kernfs_rwsem' offset changed from 768 to 832 (in bits) (by +64 bits)
    'rw_semaphore kernfs_iattr_rwsem' offset changed from 1088 to 1152 (in bits) (by +64 bits)
    'rw_semaphore kernfs_supers_rwsem' offset changed from 1408 to 1472 (in bits) (by +64 bits)
    'callback_head rcu' offset changed from 1728 to 1856 (in bits) (by +128 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct mnt_namespace</code> (mount.h:14:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'mntns_flags_t mntns_flags', at offset 1504 (in bits) at mount.h:40:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct msi_domain_info</code> (msi.h:491:1)</summary>

```
  type size changed from 576 to 640 (in bits)
  1 data member insertion:
    'msi_alloc_info_t* alloc_data', at offset 512 (in bits) at msi.h:509:1
  there are data member changes:
    'void* data' offset changed from 512 to 576 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct nfs_client</code> (nfs_fs_sb.h:29:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'netns_tracker cl_ns_tracker', at offset 6400 (in bits) at nfs_fs_sb.h:128:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct perf_cgroup</code> (perf_event.h:1123:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cgroup_subsys_state' of 'perf_cgroup::css' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct phy_driver</code> (phy.h:898:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int (phy_device*)*' of 'phy_driver::match_phy_device' changed:
      pointer type changed from: 'int (phy_device*)*' to: 'int (phy_device*, const phy_driver*)*'
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct rpc_rqst</code> (xprt.h:54:1)</summary>

```
  type size changed from 3520 to 3648 (in bits)
  1 data member insertion:
    'unsigned int rq_seqno_count', at offset 1504 (in bits) at xprt.h:72:1
  there are data member changes:
    type 'typedef u32' of 'rpc_rqst::rq_seqno' changed:
      entity changed from 'typedef u32' to 'u32[3]'
      type size changed from 32 to 96 (in bits)
    and name of 'rpc_rqst::rq_seqno' changed to 'rpc_rqst::rq_seqnos' at xprt.h:71:1
    'int rq_enc_pages_num' offset changed from 1440 to 1536 (in bits) (by +96 bits)
    'page** rq_enc_pages' offset changed from 1472 to 1600 (in bits) (by +128 bits)
    'void (rpc_rqst*)* rq_release_snd_buf' offset changed from 1536 to 1664 (in bits) (by +128 bits)
    anonymous data member 'union {list_head rq_list; rb_node rq_recv;}' offset changed from 1600 to 1728 (in bits) (by +128 bits)
    'list_head rq_xmit' offset changed from 1792 to 1920 (in bits) (by +128 bits)
    'list_head rq_xmit2' offset changed from 1920 to 2048 (in bits) (by +128 bits)
    'void* rq_buffer' offset changed from 2048 to 2176 (in bits) (by +128 bits)
    'size_t rq_callsize' offset changed from 2112 to 2240 (in bits) (by +128 bits)
    'void* rq_rbuffer' offset changed from 2176 to 2304 (in bits) (by +128 bits)
    'size_t rq_rcvsize' offset changed from 2240 to 2368 (in bits) (by +128 bits)
    'size_t rq_xmit_bytes_sent' offset changed from 2304 to 2432 (in bits) (by +128 bits)
    'size_t rq_reply_bytes_recvd' offset changed from 2368 to 2496 (in bits) (by +128 bits)
    'xdr_buf rq_private_buf' offset changed from 2432 to 2560 (in bits) (by +128 bits)
    'unsigned long int rq_majortimeo' offset changed from 3008 to 3136 (in bits) (by +128 bits)
    'unsigned long int rq_minortimeo' offset changed from 3072 to 3200 (in bits) (by +128 bits)
    'unsigned long int rq_timeout' offset changed from 3136 to 3264 (in bits) (by +128 bits)
    'ktime_t rq_rtt' offset changed from 3200 to 3328 (in bits) (by +128 bits)
    'unsigned int rq_retries' offset changed from 3264 to 3392 (in bits) (by +128 bits)
    'unsigned int rq_connect_cookie' offset changed from 3296 to 3424 (in bits) (by +128 bits)
    'atomic_t rq_pin' offset changed from 3328 to 3456 (in bits) (by +128 bits)
    'u32 rq_bytes_sent' offset changed from 3360 to 3488 (in bits) (by +128 bits)
    'ktime_t rq_xtime' offset changed from 3392 to 3520 (in bits) (by +128 bits)
    'int rq_ntrans' offset changed from 3456 to 3584 (in bits) (by +128 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct sock</code> (sock.h:345:1)</summary>

```
  type size hasn't changed
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct svc_rqst</code> (svc.h:166:1)</summary>

```
  type size changed from 92544 to 9792 (in bits)
  1 data member deletion:
    'kvec rq_vec[259]', at offset 24768 (in bits) at svc.h:197:1
  1 data member insertion:
    'unsigned long int rq_maxpages', at offset 5888 (in bits) at svc.h:201:1
  there are data member changes:
    type 'page*[260]' of 'svc_rqst::rq_pages' changed:
      entity changed from 'page*[260]' to 'page**'
      type size changed from 16640 to 64 (in bits)
    and offset changed from 5888 to 5952 (in bits) (by +64 bits)
    'page** rq_respages' offset changed from 22528 to 6016 (in bits) (by -16512 bits)
    'page** rq_next_page' offset changed from 22592 to 6080 (in bits) (by -16512 bits)
    'page** rq_page_end' offset changed from 22656 to 6144 (in bits) (by -16512 bits)
    'folio_batch rq_fbatch' offset changed from 22720 to 6208 (in bits) (by -16512 bits)
    type 'bio_vec[259]' of 'svc_rqst::rq_bvec' changed:
      entity changed from 'bio_vec[259]' to 'bio_vec*'
      type size changed from 33152 to 64 (in bits)
    and offset changed from 57920 to 8256 (in bits) (by -49664 bits)
    '__be32 rq_xid' offset changed from 91072 to 8320 (in bits) (by -82752 bits)
    'u32 rq_prog' offset changed from 91104 to 8352 (in bits) (by -82752 bits)
    'u32 rq_vers' offset changed from 91136 to 8384 (in bits) (by -82752 bits)
    'u32 rq_proc' offset changed from 91168 to 8416 (in bits) (by -82752 bits)
    'u32 rq_prot' offset changed from 91200 to 8448 (in bits) (by -82752 bits)
    'int rq_cachetype' offset changed from 91232 to 8480 (in bits) (by -82752 bits)
    'unsigned long int rq_flags' offset changed from 91264 to 8512 (in bits) (by -82752 bits)
    'ktime_t rq_qtime' offset changed from 91328 to 8576 (in bits) (by -82752 bits)
    'void* rq_argp' offset changed from 91392 to 8640 (in bits) (by -82752 bits)
    'void* rq_resp' offset changed from 91456 to 8704 (in bits) (by -82752 bits)
    '__be32* rq_accept_statp' offset changed from 91520 to 8768 (in bits) (by -82752 bits)
    'void* rq_auth_data' offset changed from 91584 to 8832 (in bits) (by -82752 bits)
    '__be32 rq_auth_stat' offset changed from 91648 to 8896 (in bits) (by -82752 bits)
    'int rq_auth_slack' offset changed from 91680 to 8928 (in bits) (by -82752 bits)
    'int rq_reserved' offset changed from 91712 to 8960 (in bits) (by -82752 bits)
    'ktime_t rq_stime' offset changed from 91776 to 9024 (in bits) (by -82752 bits)
    'cache_req rq_chandle' offset changed from 91840 to 9088 (in bits) (by -82752 bits)
    'auth_domain* rq_client' offset changed from 91968 to 9216 (in bits) (by -82752 bits)
    'auth_domain* rq_gssclient' offset changed from 92032 to 9280 (in bits) (by -82752 bits)
    'task_struct* rq_task' offset changed from 92096 to 9344 (in bits) (by -82752 bits)
    'net* rq_bc_net' offset changed from 92160 to 9408 (in bits) (by -82752 bits)
    'int rq_err' offset changed from 92224 to 9472 (in bits) (by -82752 bits)
  ...
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct svc_xprt</code> (svc_xprt.h:52:1)</summary>

```
  type size changed from 4160 to 4224 (in bits)
  1 data member insertion:
    'ktime_t xpt_qtime', at offset 192 (in bits) at svc_xprt.h:56:1
  there are data member changes:
    'list_head xpt_list' offset changed from 192 to 256 (in bits) (by +64 bits)
    'lwq_node xpt_ready' offset changed from 320 to 384 (in bits) (by +64 bits)
    'unsigned long int xpt_flags' offset changed from 384 to 448 (in bits) (by +64 bits)
    'svc_serv* xpt_server' offset changed from 448 to 512 (in bits) (by +64 bits)
    'atomic_t xpt_reserved' offset changed from 512 to 576 (in bits) (by +64 bits)
    'atomic_t xpt_nr_rqsts' offset changed from 544 to 608 (in bits) (by +64 bits)
    'mutex xpt_mutex' offset changed from 576 to 640 (in bits) (by +64 bits)
    'spinlock_t xpt_lock' offset changed from 832 to 896 (in bits) (by +64 bits)
    'void* xpt_auth_cache' offset changed from 896 to 960 (in bits) (by +64 bits)
    'list_head xpt_deferred' offset changed from 960 to 1024 (in bits) (by +64 bits)
    '__kernel_sockaddr_storage xpt_local' offset changed from 1088 to 1152 (in bits) (by +64 bits)
    'size_t xpt_locallen' offset changed from 2112 to 2176 (in bits) (by +64 bits)
    '__kernel_sockaddr_storage xpt_remote' offset changed from 2176 to 2240 (in bits) (by +64 bits)
    'size_t xpt_remotelen' offset changed from 3200 to 3264 (in bits) (by +64 bits)
    'char xpt_remotebuf[58]' offset changed from 3264 to 3328 (in bits) (by +64 bits)
    'list_head xpt_users' offset changed from 3776 to 3840 (in bits) (by +64 bits)
    'net* xpt_net' offset changed from 3904 to 3968 (in bits) (by +64 bits)
    'netns_tracker ns_tracker' offset changed from 3968 to 4032 (in bits) (by +64 bits)
    'const cred* xpt_cred' offset changed from 3968 to 4032 (in bits) (by +64 bits)
    'rpc_xprt* xpt_bc_xprt' offset changed from 4032 to 4096 (in bits) (by +64 bits)
    'rpc_xprt_switch* xpt_bc_xps' offset changed from 4096 to 4160 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

</details>

<details><summary><code>struct task_group</code> (sched.h:431:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cgroup_subsys_state' of 'task_group::css' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+456 more, see impacted.tsv)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+462 more, see impacted.tsv)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+462 more, see impacted.tsv)

</details>

<details><summary><code>struct cgroup_subsys</code> (cgroup-defs.h:706:1)</summary>

```
  type size changed from 2048 to 2112 (in bits)
  2 data member insertions:
    'spinlock_t rstat_ss_lock', at offset 2016 (in bits) at cgroup-defs.h:823:1
    'raw_spinlock_t* rstat_ss_cpu_lock', at offset 2048 (in bits) at cgroup-defs.h:824:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+462 more, see impacted.tsv)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

</details>

<details><summary><code>struct dir_context</code> (fs.h:2071:1)</summary>

```
  type size changed from 128 to 192 (in bits)
  1 data member insertion:
    'int count', at offset 128 (in bits) at fs.h:2092:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

</details>

<details><summary><code>struct kiocb</code> (fs.h:404:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u8 ki_write_stream', at offset 304 (in bits) at fs.h:413:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

</details>

<details><summary><code>struct kstat</code> (stat.h:22:1)</summary>

```
  type size changed from 1472 to 1536 (in bits)
  1 data member insertion:
    'u32 atomic_write_unit_max_opt', at offset 1440 (in bits) at stat.h:60:1
  there are data member changes:
    'u32 atomic_write_segments_max' offset changed from 1440 to 1472 (in bits) (by +32 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

</details>

<details><summary><code>struct mod_arch_specific</code> (module.h:8:1)</summary>

```
  type size changed from 192 to 320 (in bits)
  1 data member insertion:
    'its_array its_pages', at offset 192 (in bits) at module.h:21:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

</details>

<details><summary><code>struct sb_writers</code> (fs.h:1306:1)</summary>

```
  type size changed from 2432 to 2496 (in bits)
  1 data member insertion:
    'void* freeze_owner', at offset 128 (in bits) at fs.h:1321:1
  there are data member changes:
    'percpu_rw_semaphore rw_sem[3]' offset changed from 128 to 192 (in bits) (by +64 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

</details>

<details><summary><code>struct user_struct</code> (user.h:14:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct ratelimit_state' of 'user_struct::ratelimit' changed, as reported earlier
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

</details>

<details><summary><code>struct vm_area_struct</code> (mm_types.h:779:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'pfnmap_track_ctx* pfnmap_track_ctx', at offset 1344 (in bits) at mm_types.h:913:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+464 more, see impacted.tsv)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int` … (+465 more, see impacted.tsv)

</details>

## Same interface, different set of DRM users

| symbol | v6.15 | v6.16 |
|---|---|---|
| `__copy_overflow` | drm,i915 | drm,i915,xe |
| `__ioread64_lo_hi` | i915,xe | xe |
| `__usecs_to_jiffies` | i915,xe | amdgpu,i915,xe |
| `__xa_alloc` | drm,gpu-sched,i915,xe | amdgpu,drm,gpu-sched,i915,xe |
| `_find_next_zero_bit` | amdgpu,xe | xe |
| `dma_fence_unwrap_first` | virtio-gpu | amdgpu,virtio-gpu |
| `dma_fence_unwrap_next` | virtio-gpu | amdgpu,virtio-gpu |
| `dma_map_page_attrs` | amdgpu,radeon,ttm | amdgpu,radeon,ttm,xe |
| `dma_resv_replace_fences` | xe | amdgpu,xe |
| `dma_unmap_page_attrs` | amdgpu,radeon,ttm | amdgpu,radeon,ttm,xe |
| `drain_workqueue` | amdgpu,i915,ttm | amdgpu,i915,ttm,xe |
| `is_vmalloc_addr` | i915,ttm,virtio-gpu | i915,ttm,virtio-gpu,xe |
| `ktime_get_real_seconds` | amdgpu,i915 | amdgpu |
| `memdup_user` | drm,virtio-gpu | amdgpu,drm,virtio-gpu |
| `page_offset_base` | amdgpu,drm,i915,radeon,ttm | amdgpu,drm,i915,radeon,ttm,xe |
| `phys_base` | amdgpu,i915,ttm | amdgpu,i915,ttm,xe |
| `register_pm_notifier` | amdgpu | amdgpu,xe |
| `rep_movs_alternative` | i915,xe | i915 |
| `snprintf` | amdgpu,amdxcp,drm,drm_display_helper,i915,radeon,virtio-gpu,xe | amdgpu,amdxcp,drm,drm_display_helper,i915,radeon,xe |
| `unregister_pm_notifier` | amdgpu | amdgpu,xe |
| `vmalloc_to_page` | ttm,virtio-gpu | ttm,virtio-gpu,xe |

