# Interfaces used by drm: v6.16 → v6.17

## Symbol-level summary

| | count |
|---|---|
| interfaces used in v6.16 | 1022 |
| interfaces used in v6.17 | 1043 |
| likely renames | 1 |
| newly used (excluding renames) | 23 |
| no longer used (excluding renames) | 1 |
| export kind/owner/namespace changed | 0 |
| used in both, own declaration changed | 5 |
| changed types reachable from used interfaces | 70 |

## Likely renames

Dropped and newly used symbols with identical signatures (types and parameter names) and similar names.

| v6.16 | v6.17 | signature | used by |
|---|---|---|---|
| `alloc_workqueue` | `alloc_workqueue_noprof` | `struct workqueue_struct*(const char* fmt, unsigned int flags, int max_active, ?)` | amdgpu,drm_display_helper,i915,radeon,gpu-sched,ttm,xe,ath10k_core,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_core,rtw89_core |

## Newly used in v6.17

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `__devm_regmap_init` | func | vmlinux | GPL | drivers/base/regmap/regmap.c | xe |
| `__put_task_struct_rcu_cb` | func | vmlinux | GPL | kernel/fork.c | amdgpu,xe |
| `device_property_present` | func | vmlinux | GPL | drivers/base/property.c | drm |
| `dma_fence_driver_name` | func | vmlinux | plain | drivers/dma-buf/dma-fence.c | i915 |
| `dma_fence_init64` | func | vmlinux | plain | drivers/dma-buf/dma-fence.c | amdgpu |
| `dma_fence_timeline_name` | func | vmlinux | plain | drivers/dma-buf/dma-fence.c | i915 |
| `dummy_irq_chip` | func | vmlinux | GPL | include/linux/irq.h | xe |
| `fwnode_create_software_node` | func | vmlinux | GPL | drivers/base/swnode.c | xe |
| `fwnode_device_is_available` | func | vmlinux | GPL | drivers/base/property.c | drm |
| `fwnode_find_reference` | func | vmlinux | GPL | drivers/base/property.c | drm |
| `fwnode_remove_software_node` | func | vmlinux | GPL | drivers/base/swnode.c | xe |
| `i2c_bus_type` | data | vmlinux | GPL | include/linux/i2c.h | xe |
| `i2c_unregister_device` | func | vmlinux | GPL | drivers/i2c/i2c-core-base.c | xe |
| `i2c_verify_adapter` | func | vmlinux | plain | drivers/i2c/i2c-core-base.c | xe |
| `int_pow` | func | vmlinux | GPL | lib/math/int_pow.c | i915,xe |
| `intlog10` | func | vmlinux | plain | lib/math/int_log.c | i915,xe |
| `irq_dispose_mapping` | func | vmlinux | GPL | kernel/irq/irqdomain.c | xe |
| `kernel_write` | func | vmlinux | plain | fs/read_write.c | i915 |
| `platform_device_add` | func | vmlinux | GPL | drivers/base/platform.c | xe |
| `platform_device_add_resources` | func | vmlinux | GPL | drivers/base/platform.c | xe |
| `platform_device_alloc` | func | vmlinux | GPL | drivers/base/platform.c | xe |
| `platform_device_put` | func | vmlinux | GPL | drivers/base/platform.c | xe |
| `pm_hibernate_is_recovering` | func | vmlinux | GPL | drivers/base/power/main.c | amdgpu |

## No longer used in v6.17

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `__put_task_struct` | func | vmlinux | GPL | kernel/fork.c | amdgpu,xe |

## Interfaces whose own declaration changed

Return/parameter types, variable types, or interfaces that lost their debug info. `[C]` changed, `[D]` deleted.

**[C] 'function int shmem_writeout(folio*, writeback_control*)' at shmem.c:1580:1 has some sub-type changes:** (vmlinux)

```
    parameter 3 of type 'list_head*' was added
    parameter 2 of type 'writeback_control*' changed:
      pointer type changed from: 'writeback_control*' to: 'swap_iocb**'
```

**[C] 'function int wbinvd_on_all_cpus()' at cache-smp.c:17:1 has some sub-type changes:** (vmlinux)

```
    return type changed:
      type name changed from 'int' to 'void'
      type size changed from 32 to 0 (in bits)
```

**[C] 'const dma_fence_ops dma_fence_array_ops' was changed at dma-fence.h:651:1:** (vmlinux)

```
    size of symbol changed from 64 to 56
    type of variable changed:
      in unqualified underlying type 'struct dma_fence_ops' at dma-fence.h:128:1:
        type size changed from 512 to 448 (in bits)
        1 data member deletion:
          'bool use_64bit_seqno', at offset 0 (in bits) at dma-fence.h:133:1
        there are data member changes:
          'const char* (dma_fence*)* get_driver_name' offset changed from 64 to 0 (in bits) (by -64 bits)
          'const char* (dma_fence*)* get_timeline_name' offset changed from 128 to 64 (in bits) (by -64 bits)
          'typedef bool (dma_fence*)* enable_signaling' offset changed from 192 to 128 (in bits) (by -64 bits)
          'typedef bool (dma_fence*)* signaled' offset changed from 256 to 192 (in bits) (by -64 bits)
          'long int (dma_fence*, typedef bool, long int)* wait' offset changed from 320 to 256 (in bits) (by -64 bits)
          'void (dma_fence*)* release' offset changed from 384 to 320 (in bits) (by -64 bits)
          'void (dma_fence*, typedef ktime_t)* set_deadline' offset changed from 448 to 384 (in bits) (by -64 bits)
```

**[C] 'const dma_fence_ops dma_fence_chain_ops' was changed at dma-fence.h:652:1:** (vmlinux)

```
    size of symbol changed from 64 to 56
    type of variable changed:
      unqualified underlying type 'struct dma_fence_ops' changed at dma-fence.h:126:1, as reported earlier
```

**[C] 'efi efi' was changed at efi.h:668:1:** (vmlinux)

```
    size of symbol changed from 272 to 280
    type of variable changed:
      type size changed from 2176 to 2240 (in bits)
      1 data member insertion:
        'unsigned long int ovmf_debug_log', at offset 576 (in bits) at efi.h:646:1
      there are data member changes:
        'unsigned long int mokvar_table' offset changed from 576 to 640 (in bits) (by +64 bits)
        'unsigned long int coco_secret' offset changed from 640 to 704 (in bits) (by +64 bits)
        'unsigned long int unaccepted' offset changed from 704 to 768 (in bits) (by +64 bits)
        'efi_get_time_t* get_time' offset changed from 768 to 832 (in bits) (by +64 bits)
        'efi_set_time_t* set_time' offset changed from 832 to 896 (in bits) (by +64 bits)
        'efi_get_wakeup_time_t* get_wakeup_time' offset changed from 896 to 960 (in bits) (by +64 bits)
        'efi_set_wakeup_time_t* set_wakeup_time' offset changed from 960 to 1024 (in bits) (by +64 bits)
        'efi_get_variable_t* get_variable' offset changed from 1024 to 1088 (in bits) (by +64 bits)
        'efi_get_next_variable_t* get_next_variable' offset changed from 1088 to 1152 (in bits) (by +64 bits)
        'efi_set_variable_t* set_variable' offset changed from 1152 to 1216 (in bits) (by +64 bits)
        'efi_set_variable_t* set_variable_nonblocking' offset changed from 1216 to 1280 (in bits) (by +64 bits)
        'efi_query_variable_info_t* query_variable_info' offset changed from 1280 to 1344 (in bits) (by +64 bits)
        'efi_query_variable_info_t* query_variable_info_nonblocking' offset changed from 1344 to 1408 (in bits) (by +64 bits)
        'efi_update_capsule_t* update_capsule' offset changed from 1408 to 1472 (in bits) (by +64 bits)
        'efi_query_capsule_caps_t* query_capsule_caps' offset changed from 1472 to 1536 (in bits) (by +64 bits)
        'efi_get_next_high_mono_count_t* get_next_high_mono_count' offset changed from 1536 to 1600 (in bits) (by +64 bits)
        'efi_reset_system_t* reset_system' offset changed from 1600 to 1664 (in bits) (by +64 bits)
        'efi_memory_map memmap' offset changed from 1664 to 1728 (in bits) (by +64 bits)
        'unsigned long int flags' offset changed from 2112 to 2176 (in bits) (by +64 bits)
```

## Changed types

Each changed type reachable from an interface this group uses, with the number of those interfaces it reaches, fewest first: low counts are targeted changes, high counts are churn reached through hub types (reachability is transitive through pointers, so e.g. `struct device` or `struct module` pull in hundreds).

| type | declared at | change | used interfaces reached |
|---|---|---|---|
| `struct drm_connector` | drm_connector.h:1843:1 | type size changed from 17856 to 18240 (in bits); 1 data member deletion; 1 data member insertion; there are data member changes | 1 |
| `struct drm_file` | drm_file.h:164:1 | type size changed from 3264 to 3328 (in bits); 1 data member insertion | 1 |
| `struct drm_mode_config_funcs` | drm_mode_config.h:47:1 | there are data member changes | 1 |
| `struct i2c_client` | i2c.h:331:1 | type size changed from 6336 to 6400 (in bits); there are data member changes | 1 |
| `struct irq_domain_info` | irqdomain.h:289:1 | type size changed from 768 to 832 (in bits); 1 data member insertion; there are data member changes | 1 |
| `struct auxiliary_device` | auxiliary_bus.h:142:1 | type size changed from 6336 to 6400 (in bits); there are data member changes | 2 |
| `struct platform_device` | platform_device.h:23:1 | type size changed from 6400 to 6464 (in bits); there are data member changes | 2 |
| `struct thermal_cooling_device` | thermal.h:123:1 | type size changed from 6784 to 6848 (in bits); there are data member changes | 2 |
| `struct cec_adapter` | cec.h:234:1 | type size changed from 11584 to 11648 (in bits); there are data member changes | 3 |
| `struct input_dev` | input.h:137:1 | type size changed from 10816 to 10880 (in bits); there are data member changes | 3 |
| `struct rc_dev` | rc-core.h:157:1 | type size changed from 9600 to 9664 (in bits); there are data member changes | 3 |
| `struct rchan` | relay.h:59:1 | type size changed from 2944 to 2880 (in bits); 1 data member deletion; there are data member changes | 5 |
| `struct rchan_buf` | relay.h:34:1 | 1 data member deletion; 1 data member insertion; there are data member changes | 5 |
| `struct rchan_callbacks` | relay.h:80:1 | there are data member changes | 5 |
| `struct sched_dl_entity` | sched.h:635:1 | type size changed from 1984 to 1920 (in bits); 1 data member deletion; there are data member changes | 6 |
| `struct backlight_device` | backlight.h:246:1 | type size changed from 6720 to 6784 (in bits); there are data member changes | 7 |
| `struct i2c_adapter` | i2c.h:733:1 | type size changed from 8256 to 8320 (in bits); there are data member changes | 10 |
| `struct pci_bus` | pci.h:652:1 | type size changed from 8192 to 8256 (in bits); there are data member changes | 81 |
| `struct pci_dev` | pci.h:332:1 | type size changed from 16704 to 16768 (in bits); 1 data member insertion; there are data member changes | 81 |
| `struct pci_sriov` | pci.h:467:1 | 1 data member insertion; there are data member changes | 81 |
| `enum phy_interface_t` | phy.h:110:1 | 4 enumerator insertions; 1 enumerator change | 453 |
| `struct acpi_device` | acpi_bus.h:471:1 | type size changed from 11136 to 11200 (in bits); there are data member changes | 453 |
| `struct blk_integrity` | blkdev.h:116:1 | type size changed from 48 to 56 (in bits); 1 data member insertion | 453 |
| `struct bpf_link` | bpf.h:1694:1 | type size changed from 576 to 640 (in bits); 2 data member insertions; there are data member changes | 453 |
| `struct bpf_map` | bpf.h:263:1 | 2 data member insertions; there are data member changes | 453 |
| `struct bpf_offloaded_map` | bpf.h:601:1 | there are data member changes | 453 |
| `struct bpf_prog_aux` | bpf.h:1541:1 | type size changed from 9280 to 10304 (in bits); 1 data member insertion | 453 |
| `struct bpf_xdp_link` | dev.c:9881:1 | type size changed from 704 to 768 (in bits); there are data member changes | 453 |
| `struct device_link` | device.h:707:1 | type size changed from 6592 to 6656 (in bits); there are data member changes | 453 |
| `struct devlink_port` | devlink.h:123:1 | there are data member changes | 453 |
| `struct devlink_rate` | devlink.h:102:1 | type size changed from 704 to 960 (in bits); 1 data member insertion | 453 |
| `struct ethtool_ops` | ethtool.h:1083:1 | type size changed from 5056 to 5184 (in bits); 2 data member insertions; there are data member changes | 453 |
| `struct ethtool_rmon_stats` | ethtool.h:559:1 | type size changed from 1600 to 1728 (in bits); there are data member changes | 453 |
| `struct fs_struct` | fs_struct.h:9:1 | 1 data member deletion; there are data member changes | 453 |
| `struct inet6_dev` | if_inet6.h:167:1 | there are data member changes | 453 |
| `struct io_ring_ctx` | io_uring_types.h:237:1 | type size changed from 12288 to 11776 (in bits); 2 data member deletions; there are data member changes | 453 |
| `struct iommu_ops` | iommu.h:621:1 | 1 data member deletion; 1 data member insertion; there are data member changes | 453 |
| `struct linux_mib` | snmp.h:104:1 | type size changed from 8640 to 8704 (in bits); there are data member changes | 453 |
| `struct mdio_device` | mdio.h:28:1 | type size changed from 6592 to 6656 (in bits); there are data member changes | 453 |
| `struct mii_bus` | phy.h:334:1 | type size changed from 20928 to 18944 (in bits); 1 data member deletion; there are data member changes | 453 |
| `struct mount` | mount.h:50:1 | type size changed from 2944 to 2816 (in bits); 1 data member deletion; 2 data member insertions; there are data member changes | 453 |
| `struct mountpoint` | mount.h:43:1 | type size changed from 320 to 256 (in bits); 1 data member deletion | 453 |
| `struct msi_domain_info` | msi.h:499:1 | type size changed from 640 to 704 (in bits); 1 data member insertion; there are data member changes | 453 |
| `struct napi_config` | netdevice.h:367:1 | 1 data member insertion; there are data member changes | 453 |
| `struct neigh_table` | neighbour.h:202:1 | type size changed from 4800 to 5056 (in bits); 1 data member insertion; there are data member changes | 453 |
| `struct net_device` | netdevice.h:2084:1 | 1 data member insertion; there are data member changes | 453 |
| `struct per_cpu_nodestat` | mmzone.h:758:1 | type size changed from 392 to 384 (in bits); there are data member changes | 453 |
| `struct pglist_data` | mmzone.h:1356:1 | there are data member changes | 453 |
| `struct phy_device` | phy.h:606:1 | 1 data member deletion; 1 data member insertion; there are data member changes | 453 |
| `struct pneigh_entry` | neighbour.h:178:1 | type size changed from 256 to 384 (in bits); 2 data member insertions; there are data member changes | 453 |
| `struct queue_limits` | blkdev.h:368:1 | type size changed from 1472 to 1536 (in bits); 3 data member insertions; there are data member changes | 453 |
| `struct request_queue` | blkdev.h:465:1 | type size changed from 7744 to 7808 (in bits); there are data member changes | 453 |
| `struct request_sock_ops` | request_sock.h:28:1 | type size changed from 512 to 448 (in bits); 1 data member deletion; there are data member changes | 453 |
| `struct rq` | sched.h:1099:1 | type size changed from 26624 to 26112 (in bits); there are data member changes | 453 |
| `struct sched_entity` | sched.h:568:1 | type size hasn't changed | 453 |
| `struct sock` | sock.h:351:1 | type size changed from 6080 to 6144 (in bits); 1 data member insertion; there are data member changes | 453 |
| `struct task_group` | sched.h:431:1 | 1 data member insertion | 453 |
| `struct wq_device` | workqueue.c:7047:1 | type size changed from 5824 to 5888 (in bits); there are data member changes | 453 |
| `struct writeback_control` | writeback.h:43:1 | type size changed from 2624 to 2496 (in bits); 3 data member deletions; there are data member changes | 455 |
| `struct address_space_operations` | fs.h:438:1 | there are data member changes | 459 |
| `struct block_device` | blk_types.h:41:1 | type size changed from 7424 to 7488 (in bits); there are data member changes | 459 |
| `struct cgroup_subsys` | cgroup-defs.h:735:1 | there are data member changes | 459 |
| `struct css_rstat_cpu` | cgroup-defs.h:373:1 | type size changed from 128 to 256 (in bits); 2 data member insertions | 459 |
| `struct file_ra_state` | fs.h:1052:1 | 1 data member insertion; there are data member changes | 459 |
| `struct inode_operations` | fs.h:2221:1 | there are data member changes | 459 |
| `struct mm_struct` | mm_types.h:933:1 | type size changed from 10240 to 11264 (in bits); there are data member changes | 459 |
| `struct pid` | pid.h:55:1 | type size changed from 1088 to 1152 (in bits); 2 data member deletions; there are data member changes | 459 |
| `struct super_block` | fs.h:1325:1 | 1 data member insertion; there are data member changes | 459 |
| `struct super_operations` | fs.h:2338:1 | type size changed from 1664 to 1728 (in bits); 1 data member insertion; there are data member changes | 459 |
| `struct task_struct` | sched.h:812:1 | type size changed from 24576 to 25088 (in bits); 1 data member insertion; there are data member changes | 459 |

### Details

<details><summary><code>struct drm_connector</code> (drm_connector.h:1843:1)</summary>

```
  type size changed from 17856 to 18240 (in bits)
  1 data member deletion:
    'hdr_sink_metadata hdr_sink_metadata', at offset 16064 (in bits) at drm_connector.h:2245:1
  1 data member insertion:
    'drm_connector_cec cec', at offset 17856 (in bits) at drm_connector.h:2307:1
  there are data member changes:
    type 'struct drm_display_info' of 'drm_connector::display_info' changed:
      type size changed from 1600 to 1728 (in bits)
      1 data member insertion:
        'hdr_sink_metadata hdr_sink_metadata', at offset 1216 (in bits) at drm_connector.h:805:1
      there are data member changes:
        'bool non_desktop' offset changed from 1216 to 1312 (in bits) (by +96 bits)
        'drm_monitor_range_info monitor_range' offset changed from 1232 to 1328 (in bits) (by +96 bits)
        'drm_luminance_range_info luminance_range' offset changed from 1280 to 1376 (in bits) (by +96 bits)
        'u8 mso_stream_count' offset changed from 1344 to 1440 (in bits) (by +96 bits)
        'u8 mso_pixel_overlap' offset changed from 1352 to 1448 (in bits) (by +96 bits)
        'u32 max_dsc_bpp' offset changed from 1376 to 1472 (in bits) (by +96 bits)
        'u8* vics' offset changed from 1408 to 1536 (in bits) (by +128 bits)
        'int vics_len' offset changed from 1472 to 1600 (in bits) (by +128 bits)
        'u32 quirks' offset changed from 1504 to 1632 (in bits) (by +128 bits)
        'u16 source_physical_address' offset changed from 1536 to 1664 (in bits) (by +128 bits)
    'const drm_connector_funcs* funcs' offset changed from 3200 to 3328 (in bits) (by +128 bits)
    'drm_property_blob* edid_blob_ptr' offset changed from 3264 to 3392 (in bits) (by +128 bits)
    'drm_object_properties properties' offset changed from 3328 to 3456 (in bits) (by +128 bits)
    'drm_property* scaling_mode_property' offset changed from 11584 to 11712 (in bits) (by +128 bits)
    'drm_property* vrr_capable_property' offset changed from 11648 to 11776 (in bits) (by +128 bits)
    'drm_property* colorspace_property' offset changed from 11712 to 11840 (in bits) (by +128 bits)
    'drm_property_blob* path_blob_ptr' offset changed from 11776 to 11904 (in bits) (by +128 bits)
    'unsigned int max_bpc' offset changed from 11840 to 11968 (in bits) (by +128 bits)
    'drm_property* max_bpc_property' offset changed from 11904 to 12032 (in bits) (by +128 bits)
    'drm_privacy_screen* privacy_screen' offset changed from 11968 to 12096 (in bits) (by +128 bits)
    'notifier_block privacy_screen_notifier' offset changed from 12032 to 12160 (in bits) (by +128 bits)
    'drm_property* privacy_screen_sw_state_property' offset changed from 12224 to 12352 (in bits) (by +128 bits)
    'drm_property* privacy_screen_hw_state_property' offset changed from 12288 to 12416 (in bits) (by +128 bits)
    'drm_property* broadcast_rgb_property' offset changed from 12352 to 12480 (in bits) (by +128 bits)
    'uint8_t polled' offset changed from 12416 to 12544 (in bits) (by +128 bits)
    'int dpms' offset changed from 12448 to 12576 (in bits) (by +128 bits)
    'const drm_connector_helper_funcs* helper_private' offset changed from 12480 to 12608 (in bits) (by +128 bits)
    'drm_cmdline_mode cmdline_mode' offset changed from 12544 to 12672 (in bits) (by +128 bits)
    'drm_connector_force force' offset changed from 13312 to 13440 (in bits) (by +128 bits)
  ...
```

Reaches: `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`

</details>

<details><summary><code>struct drm_file</code> (drm_file.h:164:1)</summary>

```
  type size changed from 3264 to 3328 (in bits)
  1 data member insertion:
    'dentry* debugfs_client', at offset 3264 (in bits) at drm_file.h:412:1
```

Reaches: `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`

</details>

<details><summary><code>struct drm_mode_config_funcs</code> (drm_mode_config.h:47:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'drm_framebuffer* (drm_device*, drm_file*, const drm_mode_fb_cmd2*)*' of 'drm_mode_config_funcs::fb_create' changed:
      pointer type changed from: 'drm_framebuffer* (drm_device*, drm_file*, const drm_mode_fb_cmd2*)*' to: 'drm_framebuffer* (drm_device*, drm_file*, const drm_format_info*, const drm_mode_fb_cmd2*)*'
    type 'const drm_format_info* (const drm_mode_fb_cmd2*)*' of 'drm_mode_config_funcs::get_format_info' changed:
      pointer type changed from: 'const drm_format_info* (const drm_mode_fb_cmd2*)*' to: 'const drm_format_info* (typedef u32, typedef u64)*'
```

Reaches: `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`

</details>

<details><summary><code>struct i2c_client</code> (i2c.h:331:1)</summary>

```
  type size changed from 6336 to 6400 (in bits)
  there are data member changes:
    type 'struct device' of 'i2c_client::dev' changed, as reported earlier
    'int init_irq' offset changed from 6016 to 6080 (in bits) (by +64 bits)
    'int irq' offset changed from 6048 to 6112 (in bits) (by +64 bits)
    'list_head detected' offset changed from 6080 to 6144 (in bits) (by +64 bits)
    'void* devres_group_id' offset changed from 6208 to 6272 (in bits) (by +64 bits)
    'dentry* debugfs' offset changed from 6272 to 6336 (in bits) (by +64 bits)
```

Reaches: `function i2c_client* i2c_new_client_device(i2c_adapter*, const i2c_board_info*)`

</details>

<details><summary><code>struct irq_domain_info</code> (irqdomain.h:289:1)</summary>

```
  type size changed from 768 to 832 (in bits)
  1 data member insertion:
    'device* dev', at offset 512 (in bits) at irqdomain.h:305:1
  there are data member changes:
    'irq_domain* parent' offset changed from 512 to 576 (in bits) (by +64 bits)
    'irq_domain_chip_generic_info* dgc_info' offset changed from 576 to 640 (in bits) (by +64 bits)
    'int (irq_domain*)* init' offset changed from 640 to 704 (in bits) (by +64 bits)
    'void (irq_domain*)* exit' offset changed from 704 to 768 (in bits) (by +64 bits)
```

Reaches: `function irq_domain* irq_domain_instantiate(const irq_domain_info*)`

</details>

<details><summary><code>struct auxiliary_device</code> (auxiliary_bus.h:142:1)</summary>

```
  type size changed from 6336 to 6400 (in bits)
  there are data member changes:
    type 'struct device' of 'auxiliary_device::dev' changed, as reported earlier
    'const char* name' offset changed from 5760 to 5824 (in bits) (by +64 bits)
    'u32 id' offset changed from 5824 to 5888 (in bits) (by +64 bits)
    'struct {xarray irqs; mutex lock; bool irq_dir_exists;} sysfs' offset changed from 5888 to 5952 (in bits) (by +64 bits)
```

Reaches: `function int __auxiliary_device_add(auxiliary_device*, const char*)`, `function int auxiliary_device_init(auxiliary_device*)`

</details>

<details><summary><code>struct platform_device</code> (platform_device.h:23:1)</summary>

```
  type size changed from 6400 to 6464 (in bits)
  there are data member changes:
    type 'struct device' of 'platform_device::dev' changed, as reported earlier
    'u64 platform_dma_mask' offset changed from 5888 to 5952 (in bits) (by +64 bits)
    'device_dma_parameters dma_parms' offset changed from 5952 to 6016 (in bits) (by +64 bits)
    'u32 num_resources' offset changed from 6080 to 6144 (in bits) (by +64 bits)
    'resource* resource' offset changed from 6144 to 6208 (in bits) (by +64 bits)
    'const platform_device_id* id_entry' offset changed from 6208 to 6272 (in bits) (by +64 bits)
    'const char* driver_override' offset changed from 6272 to 6336 (in bits) (by +64 bits)
    'mfd_cell* mfd_cell' offset changed from 6336 to 6400 (in bits) (by +64 bits)
    'pdev_archdata archdata' offset changed from 6400 to 6464 (in bits) (by +64 bits)
```

Reaches: `function platform_device* platform_device_register_full(const platform_device_info*)`, `function void platform_device_unregister(platform_device*)`

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

Reaches: `function cpufreq_policy* cpufreq_cpu_get(unsigned int)`, `function void cpufreq_cpu_put(cpufreq_policy*)`

</details>

<details><summary><code>struct cec_adapter</code> (cec.h:234:1)</summary>

```
  type size changed from 11584 to 11648 (in bits)
  there are data member changes:
    type 'struct cec_devnode' of 'cec_adapter::devnode' changed:
      type size changed from 7360 to 7424 (in bits)
      there are data member changes:
        type 'struct device' of 'cec_devnode::dev' changed, as reported earlier
        'cdev cdev' offset changed from 5760 to 5824 (in bits) (by +64 bits)
        'int minor' offset changed from 6592 to 6656 (in bits) (by +64 bits)
        'mutex lock' offset changed from 6656 to 6720 (in bits) (by +64 bits)
        'bool registered' offset changed from 6912 to 6976 (in bits) (by +64 bits)
        'bool unregistered' offset changed from 6920 to 6984 (in bits) (by +64 bits)
        'mutex lock_fhs' offset changed from 6976 to 7040 (in bits) (by +64 bits)
        'list_head fhs' offset changed from 7232 to 7296 (in bits) (by +64 bits)
    'mutex lock' offset changed from 7680 to 7744 (in bits) (by +64 bits)
    'rc_dev* rc' offset changed from 7936 to 8000 (in bits) (by +64 bits)
    'list_head transmit_queue' offset changed from 8000 to 8064 (in bits) (by +64 bits)
    'unsigned int transmit_queue_sz' offset changed from 8128 to 8192 (in bits) (by +64 bits)
    'list_head wait_queue' offset changed from 8192 to 8256 (in bits) (by +64 bits)
    'cec_data* transmitting' offset changed from 8320 to 8384 (in bits) (by +64 bits)
    'bool transmit_in_progress' offset changed from 8384 to 8448 (in bits) (by +64 bits)
    'bool transmit_in_progress_aborted' offset changed from 8392 to 8456 (in bits) (by +64 bits)
    'unsigned int xfer_timeout_ms' offset changed from 8416 to 8480 (in bits) (by +64 bits)
    'task_struct* kthread_config' offset changed from 8448 to 8512 (in bits) (by +64 bits)
    'completion config_completion' offset changed from 8512 to 8576 (in bits) (by +64 bits)
    'task_struct* kthread' offset changed from 8768 to 8832 (in bits) (by +64 bits)
    'wait_queue_head_t kthread_waitq' offset changed from 8832 to 8896 (in bits) (by +64 bits)
    'const cec_adap_ops* ops' offset changed from 9024 to 9088 (in bits) (by +64 bits)
    'void* priv' offset changed from 9088 to 9152 (in bits) (by +64 bits)
    'u32 capabilities' offset changed from 9152 to 9216 (in bits) (by +64 bits)
    'u8 available_log_addrs' offset changed from 9184 to 9248 (in bits) (by +64 bits)
    'u16 phys_addr' offset changed from 9200 to 9264 (in bits) (by +64 bits)
    'bool needs_hpd' offset changed from 9216 to 9280 (in bits) (by +64 bits)
    'bool is_enabled' offset changed from 9224 to 9288 (in bits) (by +64 bits)
    'bool is_claiming_log_addrs' offset changed from 9232 to 9296 (in bits) (by +64 bits)
    'bool is_configuring' offset changed from 9240 to 9304 (in bits) (by +64 bits)
    'bool must_reconfigure' offset changed from 9248 to 9312 (in bits) (by +64 bits)
    'bool is_configured' offset changed from 9256 to 9320 (in bits) (by +64 bits)
    'bool cec_pin_is_high' offset changed from 9264 to 9328 (in bits) (by +64 bits)
    'bool adap_controls_phys_addr' offset changed from 9272 to 9336 (in bits) (by +64 bits)
    'u8 last_initiator' offset changed from 9280 to 9344 (in bits) (by +64 bits)
  ...
```

Reaches: `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`

</details>

<details><summary><code>struct input_dev</code> (input.h:137:1)</summary>

```
  type size changed from 10816 to 10880 (in bits)
  there are data member changes:
    type 'struct device' of 'input_dev::dev' changed, as reported earlier
    'list_head h_list' offset changed from 10112 to 10176 (in bits) (by +64 bits)
    'list_head node' offset changed from 10240 to 10304 (in bits) (by +64 bits)
    'unsigned int num_vals' offset changed from 10368 to 10432 (in bits) (by +64 bits)
    'unsigned int max_vals' offset changed from 10400 to 10464 (in bits) (by +64 bits)
    'input_value* vals' offset changed from 10432 to 10496 (in bits) (by +64 bits)
    'bool devres_managed' offset changed from 10496 to 10560 (in bits) (by +64 bits)
    'ktime_t timestamp[3]' offset changed from 10560 to 10624 (in bits) (by +64 bits)
    'bool inhibited' offset changed from 10752 to 10816 (in bits) (by +64 bits)
```

Reaches: `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`

</details>

<details><summary><code>struct rc_dev</code> (rc-core.h:157:1)</summary>

```
  type size changed from 9600 to 9664 (in bits)
  there are data member changes:
    type 'struct device' of 'rc_dev::dev' changed, as reported earlier
    'bool managed_alloc' offset changed from 5760 to 5824 (in bits) (by +64 bits)
    'bool registered' offset changed from 5768 to 5832 (in bits) (by +64 bits)
    'bool idle' offset changed from 5776 to 5840 (in bits) (by +64 bits)
    'bool encode_wakeup' offset changed from 5784 to 5848 (in bits) (by +64 bits)
    'unsigned int minor' offset changed from 5792 to 5856 (in bits) (by +64 bits)
    'const attribute_group* sysfs_groups[5]' offset changed from 5824 to 5888 (in bits) (by +64 bits)
    'const char* device_name' offset changed from 6144 to 6208 (in bits) (by +64 bits)
    'const char* input_phys' offset changed from 6208 to 6272 (in bits) (by +64 bits)
    'input_id input_id' offset changed from 6272 to 6336 (in bits) (by +64 bits)
    'const char* driver_name' offset changed from 6336 to 6400 (in bits) (by +64 bits)
    'const char* map_name' offset changed from 6400 to 6464 (in bits) (by +64 bits)
    'rc_map rc_map' offset changed from 6464 to 6528 (in bits) (by +64 bits)
    'mutex lock' offset changed from 6784 to 6848 (in bits) (by +64 bits)
    'ir_raw_event_ctrl* raw' offset changed from 7040 to 7104 (in bits) (by +64 bits)
    'input_dev* input_dev' offset changed from 7104 to 7168 (in bits) (by +64 bits)
    'rc_driver_type driver_type' offset changed from 7168 to 7232 (in bits) (by +64 bits)
    'u32 users' offset changed from 7200 to 7264 (in bits) (by +64 bits)
    'u64 allowed_protocols' offset changed from 7232 to 7296 (in bits) (by +64 bits)
    'u64 enabled_protocols' offset changed from 7296 to 7360 (in bits) (by +64 bits)
    'u64 allowed_wakeup_protocols' offset changed from 7360 to 7424 (in bits) (by +64 bits)
    'rc_proto wakeup_protocol' offset changed from 7424 to 7488 (in bits) (by +64 bits)
    'rc_scancode_filter scancode_filter' offset changed from 7456 to 7520 (in bits) (by +64 bits)
    'rc_scancode_filter scancode_wakeup_filter' offset changed from 7520 to 7584 (in bits) (by +64 bits)
    'u32 scancode_mask' offset changed from 7584 to 7648 (in bits) (by +64 bits)
    'void* priv' offset changed from 7616 to 7680 (in bits) (by +64 bits)
    'spinlock_t keylock' offset changed from 7680 to 7744 (in bits) (by +64 bits)
    'bool keypressed' offset changed from 7712 to 7776 (in bits) (by +64 bits)
    'u8 last_toggle' offset changed from 7720 to 7784 (in bits) (by +64 bits)
    'u32 last_keycode' offset changed from 7744 to 7808 (in bits) (by +64 bits)
    'rc_proto last_protocol' offset changed from 7776 to 7840 (in bits) (by +64 bits)
    'u64 last_scancode' offset changed from 7808 to 7872 (in bits) (by +64 bits)
    'unsigned long int keyup_jiffies' offset changed from 7872 to 7936 (in bits) (by +64 bits)
    'timer_list timer_keyup' offset changed from 7936 to 8000 (in bits) (by +64 bits)
    'timer_list timer_repeat' offset changed from 8256 to 8320 (in bits) (by +64 bits)
    'u32 timeout' offset changed from 8576 to 8640 (in bits) (by +64 bits)
    'u32 min_timeout' offset changed from 8608 to 8672 (in bits) (by +64 bits)
    'u32 max_timeout' offset changed from 8640 to 8704 (in bits) (by +64 bits)
  ...
```

Reaches: `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`

</details>

<details><summary><code>struct rchan</code> (relay.h:59:1)</summary>

```
  type size changed from 2944 to 2880 (in bits)
  1 data member deletion:
    'size_t last_toobig', at offset 448 (in bits) at relay.h:68:1
  there are data member changes:
    'rchan_buf** buf' offset changed from 512 to 448 (in bits) (by -64 bits)
    'int is_global' offset changed from 576 to 512 (in bits) (by -64 bits)
    'list_head list' offset changed from 640 to 576 (in bits) (by -64 bits)
    'dentry* parent' offset changed from 768 to 704 (in bits) (by -64 bits)
    'int has_base_filename' offset changed from 832 to 768 (in bits) (by -64 bits)
    'char base_filename[255]' offset changed from 864 to 800 (in bits) (by -64 bits)
```

Reaches: `function int relay_buf_full(rchan_buf*)`, `function void relay_close(rchan*)`, `function void relay_flush(rchan*)`, `function rchan* relay_open(const char*, dentry*, size_t, size_t, const rchan_callbacks*, void*)`, `function size_t relay_switch_subbuf(rchan_buf*, size_t)`

</details>

<details><summary><code>struct rchan_buf</code> (relay.h:34:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'size_t prev_padding', at offset 1152 (in bits) at relay.h:50:1
  1 data member insertion:
    'rchan_buf_stats stats', at offset 928 (in bits) at relay.h:62:1
  there are data member changes:
    'page** page_array' offset changed from 960 to 1024 (in bits) (by +64 bits)
    'unsigned int page_count' offset changed from 1024 to 1088 (in bits) (by +64 bits)
    'unsigned int finalized' offset changed from 1056 to 1120 (in bits) (by +64 bits)
    'size_t* padding' offset changed from 1088 to 1152 (in bits) (by +64 bits)
```

Reaches: `function int relay_buf_full(rchan_buf*)`, `function void relay_close(rchan*)`, `function void relay_flush(rchan*)`, `function rchan* relay_open(const char*, dentry*, size_t, size_t, const rchan_callbacks*, void*)`, `function size_t relay_switch_subbuf(rchan_buf*, size_t)`

</details>

<details><summary><code>struct rchan_callbacks</code> (relay.h:80:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int (rchan_buf*, void*, void*, typedef size_t)*' of 'rchan_callbacks::subbuf_start' changed:
      pointer type changed from: 'int (rchan_buf*, void*, void*, typedef size_t)*' to: 'int (rchan_buf*, void*, void*)*'
```

Reaches: `function int relay_buf_full(rchan_buf*)`, `function void relay_close(rchan*)`, `function void relay_flush(rchan*)`, `function rchan* relay_open(const char*, dentry*, size_t, size_t, const rchan_callbacks*, void*)`, `function size_t relay_switch_subbuf(rchan_buf*, size_t)`

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`

</details>

<details><summary><code>struct backlight_device</code> (backlight.h:246:1)</summary>

```
  type size changed from 6720 to 6784 (in bits)
  there are data member changes:
    type 'struct device' of 'backlight_device::dev' changed, as reported earlier
    'int use_count' offset changed from 6656 to 6720 (in bits) (by +64 bits)
```

Reaches: `function backlight_device* backlight_device_get_by_name(const char*)`, `function backlight_device* backlight_device_register(const char*, device*, void*, const backlight_ops*, const backlight_properties*)`, `function int backlight_device_set_brightness(backlight_device*, unsigned long int)`, `function void backlight_device_unregister(backlight_device*)`, `function void backlight_force_update(backlight_device*, backlight_update_reason)`, `function backlight_device* devm_backlight_device_register(device*, const char*, device*, void*, const backlight_ops*, const backlight_properties*)`, `function backlight_device* devm_of_find_backlight(device*)`

</details>

<details><summary><code>struct i2c_adapter</code> (i2c.h:733:1)</summary>

```
  type size changed from 8256 to 8320 (in bits)
  there are data member changes:
    type 'struct device' of 'i2c_adapter::dev' changed, as reported earlier
    'unsigned long int locked_flags' offset changed from 6656 to 6720 (in bits) (by +64 bits)
    'int nr' offset changed from 6720 to 6784 (in bits) (by +64 bits)
    'char name[48]' offset changed from 6752 to 6816 (in bits) (by +64 bits)
    'completion dev_released' offset changed from 7168 to 7232 (in bits) (by +64 bits)
    'mutex userspace_clients_lock' offset changed from 7424 to 7488 (in bits) (by +64 bits)
    'list_head userspace_clients' offset changed from 7680 to 7744 (in bits) (by +64 bits)
    'i2c_bus_recovery_info* bus_recovery_info' offset changed from 7808 to 7872 (in bits) (by +64 bits)
    'const i2c_adapter_quirks* quirks' offset changed from 7872 to 7936 (in bits) (by +64 bits)
    'irq_domain* host_notify_domain' offset changed from 7936 to 8000 (in bits) (by +64 bits)
    'regulator* bus_regulator' offset changed from 8000 to 8064 (in bits) (by +64 bits)
    'dentry* debugfs' offset changed from 8064 to 8128 (in bits) (by +64 bits)
    'unsigned long int addrs_in_instantiation[2]' offset changed from 8128 to 8192 (in bits) (by +64 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function int __i2c_transfer(i2c_adapter*, i2c_msg*, int)`, `function i2c_adapter* i2c_acpi_find_adapter_by_handle(acpi_handle)`, `function int i2c_add_adapter(i2c_adapter*)`, `function void i2c_del_adapter(i2c_adapter*)`, `function i2c_adapter* i2c_get_adapter(int)`, `function i2c_client* i2c_new_client_device(i2c_adapter*, const i2c_board_info*)`, `function void i2c_put_adapter(i2c_adapter*)`, `function int i2c_transfer(i2c_adapter*, i2c_msg*, int)`

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function agp_memory* agp_allocate_memory(agp_bridge_data*, size_t, u32)`, `function agp_bridge_data* agp_backend_acquire(pci_dev*)`, `function void agp_backend_release(agp_bridge_data*)`, `function int agp_bind_memory(agp_memory*, off_t)`, `function int agp_copy_info(agp_bridge_data*, agp_kern_info*)`, `function void agp_enable(agp_bridge_data*, u32)`, `function void agp_free_memory(agp_memory*)`, `function int agp_unbind_memory(agp_memory*)`, `function int aperture_remove_conflicting_pci_devices(pci_dev*, const char*)`, `function int intel_gmch_probe(pci_dev*, pci_dev*, agp_bridge_data*)`, `function int pci_alloc_irq_vectors(pci_dev*, unsigned int, unsigned int, unsigned int)`, `function void pci_assign_unassigned_bus_resources(pci_bus*)`, `function int pci_bus_alloc_resource(pci_bus*, resource*, resource_size_t, resource_size_t, resource_size_t, unsigned long int, resource_alignf, void*)` … (+66 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function agp_memory* agp_allocate_memory(agp_bridge_data*, size_t, u32)`, `function agp_bridge_data* agp_backend_acquire(pci_dev*)`, `function void agp_backend_release(agp_bridge_data*)`, `function int agp_bind_memory(agp_memory*, off_t)`, `function int agp_copy_info(agp_bridge_data*, agp_kern_info*)`, `function void agp_enable(agp_bridge_data*, u32)`, `function void agp_free_memory(agp_memory*)`, `function int agp_unbind_memory(agp_memory*)`, `function int aperture_remove_conflicting_pci_devices(pci_dev*, const char*)`, `function int intel_gmch_probe(pci_dev*, pci_dev*, agp_bridge_data*)`, `function int pci_alloc_irq_vectors(pci_dev*, unsigned int, unsigned int, unsigned int)`, `function void pci_assign_unassigned_bus_resources(pci_bus*)`, `function int pci_bus_alloc_resource(pci_bus*, resource*, resource_size_t, resource_size_t, resource_size_t, unsigned long int, resource_alignf, void*)` … (+66 more)

</details>

<details><summary><code>struct pci_sriov</code> (pci.h:467:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u16 vf_rebar_cap', at offset 960 (in bits) at pci.h:492:1
  there are data member changes:
    'bool drivers_autoprobe' offset changed from 960 to 976 (in bits) (by +16 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function agp_memory* agp_allocate_memory(agp_bridge_data*, size_t, u32)`, `function agp_bridge_data* agp_backend_acquire(pci_dev*)`, `function void agp_backend_release(agp_bridge_data*)`, `function int agp_bind_memory(agp_memory*, off_t)`, `function int agp_copy_info(agp_bridge_data*, agp_kern_info*)`, `function void agp_enable(agp_bridge_data*, u32)`, `function void agp_free_memory(agp_memory*)`, `function int agp_unbind_memory(agp_memory*)`, `function int aperture_remove_conflicting_pci_devices(pci_dev*, const char*)`, `function int intel_gmch_probe(pci_dev*, pci_dev*, agp_bridge_data*)`, `function int pci_alloc_irq_vectors(pci_dev*, unsigned int, unsigned int, unsigned int)`, `function void pci_assign_unassigned_bus_resources(pci_bus*)`, `function int pci_bus_alloc_resource(pci_bus*, resource*, resource_size_t, resource_size_t, resource_size_t, unsigned long int, resource_alignf, void*)` … (+66 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct blk_integrity</code> (blkdev.h:116:1)</summary>

```
  type size changed from 48 to 56 (in bits)
  1 data member insertion:
    'unsigned char pi_tuple_size', at offset 48 (in bits) at blkdev.h:123:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct bpf_offloaded_map</code> (bpf.h:601:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct bpf_map' of 'bpf_offloaded_map::map' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct bpf_prog_aux</code> (bpf.h:1541:1)</summary>

```
  type size changed from 9280 to 10304 (in bits)
  1 data member insertion:
    'bpf_stream stream[2]', at offset 9280 (in bits) at bpf.h:1690:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct bpf_xdp_link</code> (dev.c:9881:1)</summary>

```
  type size changed from 704 to 768 (in bits)
  there are data member changes:
    type 'struct bpf_link' of 'bpf_xdp_link::link' changed, as reported earlier
    'net_device* dev' offset changed from 576 to 640 (in bits) (by +64 bits)
    'int flags' offset changed from 640 to 704 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct devlink_rate</code> (devlink.h:102:1)</summary>

```
  type size changed from 704 to 960 (in bits)
  1 data member insertion:
    'u32 tc_bw[8]', at offset 704 (in bits) at devlink.h:126:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct mountpoint</code> (mount.h:43:1)</summary>

```
  type size changed from 320 to 256 (in bits)
  1 data member deletion:
    'int m_count', at offset 256 (in bits) at mount.h:47:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct napi_config</code> (netdevice.h:367:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'u8 threaded', at offset 256 (in bits) at netdevice.h:372:1
  there are data member changes:
    'unsigned int napi_id' offset changed from 256 to 288 (in bits) (by +32 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct neigh_table</code> (neighbour.h:202:1)</summary>

```
  type size changed from 4800 to 5056 (in bits)
  1 data member insertion:
    'mutex phash_lock', at offset 4736 (in bits) at neighbour.h:243:1
  there are data member changes:
    'pneigh_entry** phash_buckets' offset changed from 4736 to 4992 (in bits) (by +256 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct sched_entity</code> (sched.h:568:1)</summary>

```
  type size hasn't changed
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct task_group</code> (sched.h:431:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'scx_task_group scx', at offset 2112 (in bits) at sched.h:500:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

</details>

<details><summary><code>struct wq_device</code> (workqueue.c:7047:1)</summary>

```
  type size changed from 5824 to 5888 (in bits)
  there are data member changes:
    type 'struct device' of 'wq_device::dev' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)`, `function int __auxiliary_device_add(auxiliary_device*, const char*)` … (+438 more)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations` … (+440 more)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

</details>

<details><summary><code>struct cgroup_subsys</code> (cgroup-defs.h:735:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'raw_spinlock_t*' of 'cgroup_subsys::rstat_ss_cpu_lock' changed:
      pointer type changed from: 'raw_spinlock_t*' to: 'llist_head*'
    and name of 'cgroup_subsys::rstat_ss_cpu_lock' changed to 'cgroup_subsys::lhead' at cgroup-defs.h:821:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

</details>

<details><summary><code>struct css_rstat_cpu</code> (cgroup-defs.h:373:1)</summary>

```
  type size changed from 128 to 256 (in bits)
  2 data member insertions:
    'llist_node lnode', at offset 128 (in bits) at cgroup-defs.h:382:1
    'cgroup_subsys_state* owner', at offset 192 (in bits) at cgroup-defs.h:383:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

</details>

<details><summary><code>struct super_block</code> (fs.h:1325:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'unsigned int s_d_flags', at offset 8160 (in bits) at fs.h:1408:1
  there are data member changes:
    name of 'super_block::s_d_op' changed to 'super_block::__s_d_op' at fs.h:1422:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

</details>

<details><summary><code>struct super_operations</code> (fs.h:2338:1)</summary>

```
  type size changed from 1664 to 1728 (in bits)
  1 data member insertion:
    'int (super_block*, block_device*)* remove_bdev', at offset 1600 (in bits) at fs.h:2381:1
  there are data member changes:
    'void (super_block*)* shutdown' offset changed from 1600 to 1664 (in bits) (by +64 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

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

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint` … (+444 more)

</details>

## Header-level interfaces

Macros, static inline functions, struct/union/enum tags, typedefs and enumerators defined in provider headers (headers the consumer objects were compiled against that are not consumer code) and named in consumer code. They never appear as ELF symbols, but LinuxKPI has to provide them. Name-based, so an occasional false positive is possible (e.g. a local variable or member sharing a macro's name).

| | count |
|---|---|
| used in v6.16 | 2493 |
| used in v6.17 | 2524 |
| newly used | 38 |
| no longer used | 5 |
| likely renames | 1 |
| macro/inline signature changed | 4 |
| macro body changed | 6 |
| moved to another header | 0 |

### Likely renames (header)

| v6.16 | v6.17 | kind | signature |
|---|---|---|---|
| `call_mmap` (include/linux/fs.h) | `vfs_mmap` (include/linux/fs.h) | inline | `int(struct file *file, struct vm_area_struct *vma)` |

### Newly used (header)

| name | kind | header | signature | used by |
|---|---|---|---|---|
| `BUS_NOTIFY_ADD_DEVICE` | enumerator | include/linux/device/bus.h |  | xe |
| `DEFINE_RES_IRQ_NAMED` | macro | include/linux/ioport.h | `(_irq,_name)` | xe |
| `EFBIG` | macro | include/uapi/asm-generic/errno-base.h |  | i915 |
| `EIOCBQUEUED` | macro | include/linux/errno.h |  | i915 |
| `ENOTRECOVERABLE` | macro | include/uapi/asm-generic/errno.h |  | xe |
| `HWMON_P_CAP` | macro | include/linux/hwmon.h |  | xe |
| `I2C_CLIENT_HOST_NOTIFY` | macro | include/linux/i2c.h |  | xe |
| `I2C_MAX_FAST_MODE_PLUS_FREQ` | macro | include/linux/i2c.h |  | xe |
| `INTEL_DG_NVM_REGIONS` | macro | include/linux/intel_dg_nvm_aux.h |  | xe |
| `ITER_SOURCE` | macro | include/linux/uio.h |  | i915 |
| `KERN_CONT` | macro | include/linux/kern_levels.h |  | i915 |
| `MAX_RW_COUNT` | macro | include/linux/fs.h |  | i915 |
| `O_LARGEFILE` | macro | include/uapi/asm-generic/fcntl.h |  | i915 |
| `PCI_PM_CTRL_STATE_MASK` | macro | include/uapi/linux/pci_regs.h |  | xe |
| `PROPERTY_ENTRY_STRING` | macro | include/linux/property.h | `(_name_,_val_)` | xe |
| `PROPERTY_ENTRY_U32` | macro | include/linux/property.h | `(_name_,_val_)` | xe |
| `__always_unused` | macro | include/linux/compiler_attributes.h |  | amdgpu |
| `alloc_workqueue` | macro | include/linux/workqueue.h | `(...)` | i915,iwlwifi,radeon,rtw88_core,rtw89_core,ttm,xe |
| `atomic64_add_return` | inline | include/linux/atomic/atomic-instrumented.h | `s64(s64 i, atomic64_t *v)` | xe |
| `cec_msg` | struct | include/uapi/linux/cec.h |  | drm,drm_display_helper,drm_kms_helper |
| `devm_regmap_init` | macro | include/linux/regmap.h | `(dev,bus,bus_context,config)` | xe |
| `dst_dev` | inline | include/net/dst.h | `struct net_device *(const struct dst_entry *dst)` | xe |
| `force_o_largefile` | macro | include/linux/fcntl.h | `()` | i915 |
| `hwmon_power_cap` | enumerator | include/linux/hwmon.h |  | xe |
| `i2c_client` | struct | include/linux/i2c.h |  | xe |
| `init_sync_kiocb` | inline | include/linux/fs.h | `void(struct kiocb *kiocb, struct file *filp)` | i915 |
| `intel_dg_nvm_dev` | struct | include/linux/intel_dg_nvm_aux.h |  | xe |
| `intel_dg_nvm_region` | struct | include/linux/intel_dg_nvm_aux.h |  | xe |
| `iov_iter` | struct | include/linux/uio.h |  | i915 |
| `iov_iter_ubuf` | inline | include/linux/uio.h | `void(struct iov_iter *i, unsigned int direction, void __user *buf, size_t count)` | i915 |
| `irq_dispose_mapping` | inline | include/linux/irqdomain.h | `void(unsigned int virq)` | xe |
| `kiocb` | struct | include/linux/fs.h |  | i915 |
| `kmap_local_page_try_from_panic` | inline | include/linux/highmem-internal.h | `void *(struct page *page)` | i915,ttm |
| `pm_hibernate_is_recovering` | inline | include/linux/suspend.h | `bool(void)` | amdgpu |
| `prefetch_range` | inline | include/linux/prefetch.h | `void(void *addr, size_t len)` | xe |
| `property_entry` | struct | include/linux/property.h |  | xe |
| `regmap_config` | struct | include/linux/regmap.h |  | xe |
| `str_true_false` | inline | include/linux/string_choices.h | `const char *(bool v)` | i915 |

### No longer used (header)

| name | kind | header | signature | used by |
|---|---|---|---|---|
| `acpi_device_hid` | inline | include/acpi/acpi_bus.h | `const char *(struct acpi_device *device)` | amdgpu |
| `address_space_operations` | struct | include/linux/fs.h |  | i915 |
| `kmap_local_folio` | inline | include/linux/highmem-internal.h | `void *(struct folio *folio, size_t offset)` | i915 |
| `memcpy_to_folio` | inline | include/linux/highmem.h | `void(struct folio *folio, size_t offset, const char *from, size_t len)` | i915 |
| `offset_in_folio` | macro | include/linux/mm.h | `(folio,p)` | i915 |

### Signature changed (header)

| name | kind | header | v6.16 | v6.17 |
|---|---|---|---|---|
| `__dma_fence_is_later` | inline | include/linux/dma-fence.h | `bool(u64 f1, u64 f2, const struct dma_fence_ops *ops)` | `bool(struct dma_fence *fence, u64 f1, u64 f2)` |
| `crc32` | inline | include/linux/crc32.h | `(seed,data,length)` | `u32(u32 crc, const void *p, size_t len)` |
| `ref_tracker_dir_init` | inline | include/linux/ref_tracker.h | `void(struct ref_tracker_dir *dir, unsigned int quarantine_count, const char *name)` | `void(struct ref_tracker_dir *dir, unsigned int quarantine_count, const char *class)` |
| `vm_get_page_prot` | inline | include/linux/mm.h | `pgprot_t(unsigned long vm_flags)` | `pgprot_t(vm_flags_t vm_flags)` |

<details><summary>Macro body changed (6)</summary>

| macro | header | v6.16 | v6.17 |
|---|---|---|---|
| `GENMASK` | include/linux/bits.h | `(GENMASK_INPUT_CHECK(h, l) + __GENMASK(h, l))` | `GENMASK_TYPE(unsigned long, h, l)` |
| `GENMASK_ULL` | include/linux/bits.h | `(GENMASK_INPUT_CHECK(h, l) + __GENMASK_ULL(h, l))` | `GENMASK_TYPE(unsigned long long, h, l)` |
| `MODULE_PARM_DESC` | include/linux/moduleparam.h | `__MODULE_INFO(parm, _parm, #_parm "" desc)` | `MODULE_INFO(parm, #_parm "" desc)` |
| `VSEC_CAP_CRASHLOG` | include/linux/intel_vsec.h | `BIT(2)` | `BIT(3)` |
| `VSEC_CAP_TELEMETRY` | include/linux/intel_vsec.h | `BIT(0)` | `BIT(1)` |
| `alloc_ordered_workqueue_lockdep_map` | include/linux/workqueue.h | `alloc_workqueue_lockdep_map(fmt, WQ_UNBOUND \| __WQ_ORDERED \| (flags), 1, lockdep_map, ##args)` | `alloc_hooks(alloc_workqueue_lockdep_map(fmt, WQ_UNBOUND \| __WQ_ORDERED \| (flags), 1, lockdep_map, ##args))` |

</details>

## Same interface, different set of users

| symbol | v6.16 | v6.17 |
|---|---|---|
| `__dev_fwnode` | drm | drm,i915,xe |
| `__sw_hweight64` | amdgpu,drm,drm_buddy,i915,xe,ath12k,iwlwifi,iwlmld,iwlmvm | amdgpu,drm,drm_buddy,i915,xe,ath12k,iwlwifi,iwlmld,iwlmvm,rtw89_core |
| `__x86_indirect_thunk_rbx` | amdgpu,drm_kms_helper,i915 | amdgpu,drm,drm_kms_helper,i915 |
| `__x86_indirect_thunk_rcx` | amdgpu,drm_kms_helper,i915,radeon,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt7615-common,mt7915e,mt7925-common,mt7925e,mt7996e,rtw88_8723d,rtw88_8814a,rtw88_8821c,rtw88_8822b,rtw88_8822c,rtw88_core,rtw88_pci,rtw89_8922a,rtw89_core,rtw89_pci | amdgpu,drm,drm_kms_helper,i915,radeon,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt7615-common,mt7915e,mt7925-common,mt7925e,mt7996e,rtw88_8723d,rtw88_8814a,rtw88_8821c,rtw88_8822b,rtw88_8822c,rtw88_core,rtw88_pci,rtw89_8922a,rtw89_core,rtw89_pci |
| `bus_register_notifier` | i915 | i915,xe |
| `bus_unregister_notifier` | i915 | i915,xe |
| `cec_fill_conn_info_from_drm` | amdgpu,i915,xe | amdgpu,drm_display_helper,i915,xe |
| `cec_notifier_conn_register` | amdgpu,i915,xe | amdgpu,drm_display_helper,i915,xe |
| `cec_notifier_conn_unregister` | amdgpu,i915,xe | amdgpu,drm_display_helper,i915,xe |
| `cec_notifier_set_phys_addr` | amdgpu,i915,xe | amdgpu,drm_display_helper,i915,xe |
| `debugfs_remove` | drm,i915,ttm,mt7915e,mt7996e | amdgpu,drm,i915,ttm,mt7915e,mt7996e |
| `devm_kfree` | drm_kms_helper,mt76-connac-lib,mt7915e,mt7925-common,mt792x-lib,rtw89_core | mt76-connac-lib,mt7915e,mt7925-common,mt792x-lib,rtw89_core |
| `devm_kmalloc` | drm_display_helper,drm_kms_helper,xe,ath10k_core,brcmfmac,iwlwifi,mt76,mt76-connac-lib,mt7615-common,mt7915e,mt7925-common,mt792x-lib,mt7996e,rtw89_core | drm_display_helper,xe,ath10k_core,brcmfmac,iwlwifi,mt76,mt76-connac-lib,mt7615-common,mt7915e,mt7925-common,mt792x-lib,mt7996e,rtw89_core |
| `devm_release_action` | xe | drm,xe |
| `generic_handle_irq_safe` | i915 | i915,xe |
| `i2c_new_client_device` | amdgpu,radeon | amdgpu,radeon,xe |
| `irq_create_mapping_affinity` | amdgpu | amdgpu,xe |
| `irq_domain_instantiate` | amdgpu | amdgpu,xe |
| `irq_domain_remove` | amdgpu | amdgpu,xe |
| `ktime_get_with_offset` | amdgpu,i915,xe,ath10k_core,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt792x-lib,mt7996e | amdgpu,i915,xe,ath10k_core,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7915e,mt792x-lib,mt7996e,rtw89_core |
| `platform_device_unregister` | amdxcp,drm,i915 | amdxcp,drm,i915,xe |
| `si_meminfo` | amdgpu,ttm,xe | amdgpu,ttm,xe,ath12k |
| `synchronize_rcu` | drm,i915,ath11k,ath12k,rtw89_core | drm,i915,xe,ath11k,ath12k,rtw89_core |

