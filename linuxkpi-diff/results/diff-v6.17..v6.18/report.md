# Kernel interfaces used by DRM: v6.17 → v6.18

| | count |
|---|---|
| interfaces used in v6.17 | 1071 |
| interfaces used in v6.18 | 1082 |
| likely renames | 0 |
| newly used (excluding renames) | 13 |
| no longer used (excluding renames) | 2 |
| export kind/owner/namespace changed | 0 |
| used in both, own declaration changed | 7 |
| changed types reachable from used interfaces | 58 |
| used interfaces reaching at least one changed type | 507 |

## Likely renames

None.

## Newly used in v6.18

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `USER_PTR_MAX` | data | vmlinux | plain | arch/x86/include/asm/uaccess_64.h | drm,i915,radeon |
| `devm_i2c_add_adapter` | func | vmlinux | GPL | drivers/i2c/i2c-core-base.c | amdgpu |
| `devm_remove_action_nowarn` | func | vmlinux | GPL | drivers/base/devres.c | xe |
| `down_write_trylock` | func | vmlinux | plain | kernel/locking/rwsem.c | xe |
| `hrtimer_cb_get_time` | func | vmlinux | GPL | kernel/time/hrtimer.c | amdgpu,i915,xe |
| `krealloc_node_align_noprof` | func | vmlinux | plain | mm/slub.c | amdgpu,drm,drm_kms_helper,i915,xe |
| `kvrealloc_node_align_noprof` | func | vmlinux | plain | mm/slub.c | drm_exec |
| `pm_hibernation_mode_is_suspend` | func | vmlinux | GPL | kernel/power/hibernate.c | amdgpu |
| `system_percpu_wq` | data | vmlinux | plain | include/linux/workqueue.h | amdgpu,drm,drm_display_helper,drm_kms_helper,gpu-sched,i915,radeon,virtio-gpu,xe |
| `system_state` | func | vmlinux | plain | include/linux/kernel.h | amdgpu |
| `vcalloc_noprof` | func | vmlinux | plain | mm/util.c | radeon |
| `video_is_primary_device` | func | vmlinux | plain | arch/x86/video/video-common.c | drm |
| `vmalloc_array_noprof` | func | vmlinux | plain | mm/util.c | radeon |

## No longer used in v6.18

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `krealloc_noprof` | func | vmlinux | plain | mm/slub.c | amdgpu,drm,drm_kms_helper,i915,xe |
| `kvrealloc_noprof` | func | vmlinux | plain | mm/slub.c | drm_exec |

## Interfaces whose own declaration changed

Return/parameter types, variable types, or interfaces that lost their debug info. `[C]` changed, `[D]` deleted.

**[C] 'function void* __kvmalloc_node_noprof(size_t, gfp_t, int)' at slub.c:7103:1 has some sub-type changes:** (vmlinux)

```
    parameter 4 of type 'int' was added
    parameter 2 of type 'typedef gfp_t' changed:
      entity changed from 'typedef gfp_t' to compatible type 'unsigned long int'
      type size changed from 32 to 64 (in bits)
    parameter 3 of type 'int' changed:
      entity changed from 'int' to compatible type 'typedef gfp_t' at types.h:163:1
      type size hasn't changed
```

**[C] 'function void* mempool_alloc_noprof(mempool_t*, gfp_t)' at mempool.c:408:1 has some sub-type changes:** (vmlinux)

```
    parameter 1 of type 'mempool_t*' changed:
      pointer type changed from: 'mempool_t*' to: 'mempool_t*'
```

**[C] 'function void mempool_exit(mempool_t*)' at mempool.c:186:1 has some sub-type changes:** (vmlinux)

```
    parameter 1 of type 'mempool_t*' changed:
      pointer type changed from: 'mempool_t*' to: 'mempool_t*'
```

**[C] 'function void mempool_free(void*, mempool_t*)' at mempool.c:522:1 has some sub-type changes:** (vmlinux)

```
    parameter 2 of type 'mempool_t*' changed:
      pointer type changed from: 'mempool_t*' to: 'mempool_t*'
```

**[C] 'function int mempool_init_noprof(mempool_t*, int, mempool_alloc_t*, mempool_free_t*, void*)' at mempool.c:267:1 has some sub-type changes:** (vmlinux)

```
    parameter 1 of type 'mempool_t*' changed:
      pointer type changed from: 'mempool_t*' to: 'mempool_t*'
```

**[C] 'function void pci_release_resource(pci_dev*, int)' at setup-res.c:412:1 has some sub-type changes:** (vmlinux)

```
    return type changed:
      type name changed from 'void' to 'int'
      type size changed from 0 to 32 (in bits)
```

**[C] 'uts_namespace init_uts_ns' was changed at ns_common.h:27:1:** (vmlinux)

```
    size of symbol changed from 432 to 488
    type of variable changed:
      type size changed from 3456 to 3904 (in bits)
      there are data member changes:
        type 'struct ns_common' of 'uts_namespace::ns' changed:
          type size changed from 192 to 640 (in bits)
          1 data member deletion:
            'refcount_t count', at offset 160 (in bits) at ns_common.h:13:1
          3 data member insertions:
            'u32 ns_type', at offset 0 (in bits) at ns_common.h:41:1
            'refcount_t __ns_ref', at offset 224 (in bits) at ns_common.h:45:1
            'union {struct {u64 ns_id; rb_node ns_tree_node; list_head ns_list_node;}; callback_head ns_rcu;}', at offset 256 (in bits)
          there are data member changes:
            'dentry* stashed' offset changed from 0 to 64 (in bits) (by +64 bits)
            'const proc_ns_operations* ops' offset changed from 64 to 128 (in bits) (by +64 bits)
            'unsigned int inum' offset changed from 128 to 192 (in bits) (by +64 bits)
```

Reaches 490 used interfaces.

## Changed types

Each type that changed and is reachable from an interface DRM uses, with the number of used interfaces it reaches, fewest first: low counts are targeted changes, high counts are churn reached via hub types (reachability is transitive through pointers, so e.g. `struct device` or `struct module` pull in hundreds). Per-interface index: `impacted.tsv`; raw report: `abidiff-leaf.txt`.

| type | declared at | change | used interfaces reached |
|---|---|---|---|
| `struct drm_device` | drm_device.h:68:1 | type size changed from 12608 to 12352 (in bits); 1 data member deletion; there are data member changes | 1 |
| `struct kmem_cache_args` | slab.h:281:1 | type size changed from 256 to 320 (in bits); 1 data member insertion | 1 |
| `struct ma_state` | maple_tree.h:438:1 | type size changed from 576 to 704 (in bits); 2 data member insertions; there are data member changes | 1 |
| `enum hwmon_sensor_types` | hwmon.h:20:1 | 1 enumerator insertion; 5 enumerator changes | 2 |
| `struct swap_info_struct` | swap.h:297:1 | type size changed from 2816 to 2752 (in bits); 1 data member deletion; there are data member changes | 2 |
| `struct virtio_device` | virtio.h:152:1 | type size changed from 6464 to 6592 (in bits); 2 data member insertions; there are data member changes | 10 |
| `struct pci_dev` | pci.h:337:1 | 2 data member insertions; there are data member changes | 82 |
| `enum bpf_arg_type` | bpf.h:784:1 | 1 enumerator change | 490 |
| `enum bpf_reg_type` | bpf.h:941:1 | 1 enumerator change | 490 |
| `enum bpf_return_type` | bpf.h:843:1 | 1 enumerator change | 490 |
| `struct bio` | blk_types.h:214:1 | 1 data member deletion; there are data member changes | 490 |
| `struct bio_set` | bio.h:641:1 | there are data member changes | 490 |
| `struct block_device_operations` | blkdev.h:1650:1 | there are data member changes | 490 |
| `struct bpf_map` | bpf.h:290:1 | type size changed from 1920 to 2240 (in bits); 2 data member insertions; there are data member changes | 490 |
| `struct bpf_map_ops` | bpf.h:82:1 | type size changed from 2752 to 2816 (in bits); 1 data member insertion; there are data member changes | 490 |
| `struct bpf_map_owner` | bpf.h:282:1 | type size changed from 256 to 320 (in bits); 1 data member insertion | 490 |
| `struct bpf_offloaded_map` | bpf.h:619:1 | type size changed from 2240 to 2560 (in bits); there are data member changes | 490 |
| `struct bpf_prog` | bpf.h:1693:1 | type size changed from 576 to 768 (in bits); there are data member changes | 490 |
| `struct bpf_prog_aux` | bpf.h:1582:1 | type size changed from 10304 to 10368 (in bits); 2 data member insertions; there are data member changes | 490 |
| `struct btf_record` | bpf.h:254:1 | 1 data member insertion | 490 |
| `struct dst_entry` | dst.h:26:1 | type size hasn't changed | 490 |
| `struct gendisk` | blkdev.h:143:1 | there are data member changes | 490 |
| `struct kmem_cache` | slab.h:234:1 | type size changed from 5632 to 5696 (in bits); 3 data member insertions; there are data member changes | 490 |
| `struct kmem_cache_cpu` | slub.c:400:1 | type size changed from 256 to 384 (in bits); there are data member changes | 490 |
| `struct kmem_cache_node` | slub.c:441:1 | type size changed from 512 to 576 (in bits); 1 data member insertion | 490 |
| `struct mnt_namespace` | mount.h:10:1 | type size changed from 1536 to 1600 (in bits); 4 data member deletions; 1 data member insertion; there are data member changes | 490 |
| `struct mount` | mount.h:49:1 | 1 data member insertion; there are data member changes | 490 |
| `struct msi_domain_ops` | msi.h:453:1 | type size changed from 704 to 640 (in bits); 1 data member deletion; there are data member changes | 490 |
| `struct net` | net_namespace.h:61:1 | type size changed from 30208 to 30720 (in bits); there are data member changes | 490 |
| `struct per_cpu_nodestat` | mmzone.h:762:1 | type size changed from 384 to 392 (in bits); there are data member changes | 490 |
| `struct perf_buffer` | internal.h:13:1 | there are data member changes | 490 |
| `struct perf_event` | perf_event.h:764:1 | there are data member changes | 490 |
| `struct pglist_data` | mmzone.h:1360:1 | there are data member changes | 490 |
| `struct proc_ns_operations` | proc_ns.h:17:1 | type size changed from 512 to 448 (in bits); 1 data member deletion; there are data member changes | 490 |
| `struct proto` | sock.h:1251:1 | type size changed from 3584 to 3520 (in bits); 1 data member deletion; there are data member changes | 490 |
| `struct sock` | sock.h:352:1 | 1 data member deletion; 1 data member insertion; there are data member changes | 490 |
| `union bpf_attr` | bpf.h:1484:1 | type size changed from 1216 to 1344 (in bits); 1 data member deletion; 1 data member insertion; there are data member changes | 490 |
| `struct trace_iterator` | trace_events.h:96:1 | type size changed from 132736 to 132608 (in bits); there are data member changes | 492 |
| `struct pid_namespace` | pid_namespace.h:26:1 | type size changed from 2304 to 2752 (in bits); there are data member changes | 494 |
| `struct cgroup` | cgroup-defs.h:438:1 | there are data member changes | 496 |
| `struct cgroup_namespace` | cgroup.h:786:1 | type size changed from 384 to 832 (in bits); there are data member changes | 496 |
| `struct cgroup_root` | cgroup-defs.h:603:1 | there are data member changes | 496 |
| `struct cgroup_subsys` | cgroup-defs.h:732:1 | type size changed from 2112 to 2048 (in bits); 1 data member deletion; there are data member changes | 496 |
| `struct user_namespace` | user_namespace.h:76:1 | type size changed from 4736 to 5184 (in bits); there are data member changes | 496 |
| `struct arch_uprobe` | uprobes.h:25:1 | type size changed from 256 to 320 (in bits); 1 data member insertion | 498 |
| `struct attribute_group` | sysfs.h:99:1 | there are data member changes | 498 |
| `struct bin_attribute` | sysfs.h:304:1 | type size changed from 704 to 576 (in bits); 2 data member deletions; there are data member changes | 498 |
| `struct dentry` | dcache.h:92:1 | type size hasn't changed | 498 |
| `struct file` | fs.h:1099:1 | type size hasn't changed | 498 |
| `struct inode` | fs.h:675:1 | there are data member changes | 498 |
| `struct mm_struct` | mm_types.h:937:1 | type size hasn't changed | 498 |
| `struct page` | mm_types.h:73:1 | there are data member changes | 498 |
| `struct signal_struct` | signal.h:94:1 | type size changed from 8768 to 9088 (in bits); 1 data member insertion; there are data member changes | 498 |
| `struct super_block` | fs.h:1328:1 | type size changed from 10752 to 10240 (in bits); there are data member changes | 498 |
| `struct uprobes_state` | uprobes.h:186:1 | type size changed from 64 to 128 (in bits); 1 data member insertion | 498 |
| `struct vm_area_desc` | mm_types.h:786:1 | type size changed from 576 to 640 (in bits); 1 data member insertion; there are data member changes | 498 |
| `struct vm_operations_struct` | mm.h:586:1 | type size changed from 1024 to 960 (in bits); 1 data member deletion | 498 |
| `struct hrtimer_clock_base` | hrtimer_defs.h:47:1 | 1 data member deletion; there are data member changes | 504 |

### Details

<details><summary><code>struct drm_device</code> (drm_device.h:68:1)</summary>

```
  type size changed from 12608 to 12352 (in bits)
  1 data member deletion:
    'mutex struct_mutex', at offset 1088 (in bits) at drm_device.h:199:1
  there are data member changes:
    'mutex master_mutex' offset changed from 1344 to 1088 (in bits) (by -256 bits)
    'atomic_t open_count' offset changed from 1600 to 1344 (in bits) (by -256 bits)
    'mutex filelist_mutex' offset changed from 1664 to 1408 (in bits) (by -256 bits)
    'list_head filelist' offset changed from 1920 to 1664 (in bits) (by -256 bits)
    'list_head filelist_internal' offset changed from 2048 to 1792 (in bits) (by -256 bits)
    'mutex clientlist_mutex' offset changed from 2176 to 1920 (in bits) (by -256 bits)
    'list_head clientlist' offset changed from 2432 to 2176 (in bits) (by -256 bits)
    'bool vblank_disable_immediate' offset changed from 2560 to 2304 (in bits) (by -256 bits)
    'drm_vblank_crtc* vblank' offset changed from 2624 to 2368 (in bits) (by -256 bits)
    'spinlock_t vblank_time_lock' offset changed from 2688 to 2432 (in bits) (by -256 bits)
    'spinlock_t vbl_lock' offset changed from 2720 to 2464 (in bits) (by -256 bits)
    'u32 max_vblank_count' offset changed from 2752 to 2496 (in bits) (by -256 bits)
    'list_head vblank_event_list' offset changed from 2816 to 2560 (in bits) (by -256 bits)
    'spinlock_t event_lock' offset changed from 2944 to 2688 (in bits) (by -256 bits)
    'unsigned int num_crtcs' offset changed from 2976 to 2720 (in bits) (by -256 bits)
    'drm_mode_config mode_config' offset changed from 3008 to 2752 (in bits) (by -256 bits)
    'mutex object_name_lock' offset changed from 11840 to 11584 (in bits) (by -256 bits)
    'idr object_name_idr' offset changed from 12096 to 11840 (in bits) (by -256 bits)
    'drm_vma_offset_manager* vma_offset_manager' offset changed from 12288 to 12032 (in bits) (by -256 bits)
    'drm_vram_mm* vram_mm' offset changed from 12352 to 12096 (in bits) (by -256 bits)
    'switch_power_state switch_power_state' offset changed from 12416 to 12160 (in bits) (by -256 bits)
    'drm_fb_helper* fb_helper' offset changed from 12480 to 12224 (in bits) (by -256 bits)
    'dentry* debugfs_root' offset changed from 12544 to 12288 (in bits) (by -256 bits)
```

Reaches: `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`

</details>

<details><summary><code>struct kmem_cache_args</code> (slab.h:281:1)</summary>

```
  type size changed from 256 to 320 (in bits)
  1 data member insertion:
    'unsigned int sheaf_capacity', at offset 256 (in bits) at slab.h:368:1
```

Reaches: `function kmem_cache* __kmem_cache_create_args(const char*, unsigned int, kmem_cache_args*, slab_flags_t)`

</details>

<details><summary><code>struct ma_state</code> (maple_tree.h:438:1)</summary>

```
  type size changed from 576 to 704 (in bits)
  2 data member insertions:
    'slab_sheaf* sheaf', at offset 384 (in bits) at maple_tree.h:445:1
    'unsigned long int node_request', at offset 512 (in bits) at maple_tree.h:447:1
  there are data member changes:
    type 'maple_alloc*' of 'ma_state::alloc' changed:
      pointer type changed from: 'maple_alloc*' to: 'maple_node*'
    and offset changed from 384 to 448 (in bits) (by +64 bits)
    'maple_status status' offset changed from 448 to 576 (in bits) (by +128 bits)
    'unsigned char depth' offset changed from 480 to 608 (in bits) (by +128 bits)
    'unsigned char offset' offset changed from 488 to 616 (in bits) (by +128 bits)
    'unsigned char mas_flags' offset changed from 496 to 624 (in bits) (by +128 bits)
    'unsigned char end' offset changed from 504 to 632 (in bits) (by +128 bits)
    'store_type store_type' offset changed from 512 to 640 (in bits) (by +128 bits)
```

Reaches: `function void* mas_find(ma_state*, unsigned long int)`

</details>

<details><summary><code>enum hwmon_sensor_types</code> (hwmon.h:20:1)</summary>

```
  type size hasn't changed
  1 enumerator insertion:
    'hwmon_sensor_types::hwmon_energy64' value '6'
  5 enumerator changes:
    'hwmon_sensor_types::hwmon_humidity' from value '6' to '7' at hwmon.h:20:1
    'hwmon_sensor_types::hwmon_fan' from value '7' to '8' at hwmon.h:20:1
    'hwmon_sensor_types::hwmon_pwm' from value '8' to '9' at hwmon.h:20:1
    'hwmon_sensor_types::hwmon_intrusion' from value '9' to '10' at hwmon.h:20:1
    'hwmon_sensor_types::hwmon_max' from value '10' to '11' at hwmon.h:20:1
```

Reaches: `function device* devm_hwmon_device_register_with_info(device*, const char*, void*, const hwmon_chip_info*, const attribute_group**)`, `function device* hwmon_device_register_with_info(device*, const char*, void*, const hwmon_chip_info*, const attribute_group**)`

</details>

<details><summary><code>struct swap_info_struct</code> (swap.h:297:1)</summary>

```
  type size changed from 2816 to 2752 (in bits)
  1 data member deletion:
    'atomic_long_t frag_cluster_nr[1]', at offset 1344 (in bits) at swap.h:313:1
  there are data member changes:
    'unsigned int pages' offset changed from 1408 to 1344 (in bits) (by -64 bits)
    'atomic_long_t inuse_pages' offset changed from 1472 to 1408 (in bits) (by -64 bits)
    'swap_sequential_cluster* global_cluster' offset changed from 1536 to 1472 (in bits) (by -64 bits)
    'spinlock_t global_cluster_lock' offset changed from 1600 to 1536 (in bits) (by -64 bits)
    'rb_root swap_extent_root' offset changed from 1664 to 1600 (in bits) (by -64 bits)
    'block_device* bdev' offset changed from 1728 to 1664 (in bits) (by -64 bits)
    'file* swap_file' offset changed from 1792 to 1728 (in bits) (by -64 bits)
    'completion comp' offset changed from 1856 to 1792 (in bits) (by -64 bits)
    'spinlock_t lock' offset changed from 2112 to 2048 (in bits) (by -64 bits)
    'spinlock_t cont_lock' offset changed from 2144 to 2080 (in bits) (by -64 bits)
    'work_struct discard_work' offset changed from 2176 to 2112 (in bits) (by -64 bits)
    'work_struct reclaim_work' offset changed from 2432 to 2368 (in bits) (by -64 bits)
    'list_head discard_clusters' offset changed from 2688 to 2624 (in bits) (by -64 bits)
    'plist_node avail_lists[]' offset changed from 2816 to 2752 (in bits) (by -64 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`

</details>

<details><summary><code>struct virtio_device</code> (virtio.h:152:1)</summary>

```
  type size changed from 6464 to 6592 (in bits)
  2 data member insertions:
    'const virtio_map_ops* map', at offset 6144 (in bits) at virtio.h:173:1
    'virtio_map vmap', at offset 6528 (in bits) at virtio.h:177:1
  there are data member changes:
    'list_head vqs' offset changed from 6144 to 6208 (in bits) (by +64 bits)
    anonymous data member 'union {u64 features; u64 features_array[2];}' offset changed from 6272 to 6336 (in bits) (by +64 bits)
    'void* priv' offset changed from 6400 to 6464 (in bits) (by +64 bits)
```

Reaches: `function int __register_virtio_driver(virtio_driver*, module*)`, `function void unregister_virtio_driver(virtio_driver*)`, `function void virtio_check_driver_offered_feature(const virtio_device*, unsigned int)`, `function void virtio_reset_device(virtio_device*)`, `function int virtqueue_add_sgs(virtqueue*, scatterlist**, unsigned int, unsigned int, void*, gfp_t)`, `function void virtqueue_disable_cb(virtqueue*)`, `function bool virtqueue_enable_cb(virtqueue*)`, `function void* virtqueue_get_buf(virtqueue*, unsigned int*)`, `function bool virtqueue_kick_prepare(virtqueue*)`, `function bool virtqueue_notify(virtqueue*)`

</details>

<details><summary><code>struct pci_dev</code> (pci.h:337:1)</summary>

```
  type size hasn't changed
  2 data member insertions:
    'unsigned int aspm_l0s_support', at offset 1472 (in bits) at pci.h:415:1
    'unsigned int aspm_l1_support', at offset 1473 (in bits) at pci.h:416:1
  there are data member changes:
    'unsigned int ltr_path' offset changed from 1472 to 1474 (in bits) (by +2 bits)
    'unsigned int pasid_no_tlp' offset changed from 1473 to 1475 (in bits) (by +2 bits)
    'unsigned int eetlp_prefix_max' offset changed from 1474 to 1476 (in bits) (by +2 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function agp_memory* agp_allocate_memory(agp_bridge_data*, size_t, u32)`, `function agp_bridge_data* agp_backend_acquire(pci_dev*)`, `function void agp_backend_release(agp_bridge_data*)`, `function int agp_bind_memory(agp_memory*, off_t)`, `function int agp_copy_info(agp_bridge_data*, agp_kern_info*)`, `function void agp_enable(agp_bridge_data*, u32)`, `function void agp_free_memory(agp_memory*)`, `function int agp_unbind_memory(agp_memory*)`, `function int aperture_remove_conflicting_pci_devices(pci_dev*, const char*)`, `function int intel_gmch_probe(pci_dev*, pci_dev*, agp_bridge_data*)`, `function int pci_alloc_irq_vectors(pci_dev*, unsigned int, unsigned int, unsigned int)`, `function void pci_assign_unassigned_bus_resources(pci_bus*)`, `function int pci_bus_alloc_resource(pci_bus*, resource*, resource_size_t, resource_size_t, resource_size_t, unsigned long int, resource_alignf, void*)` … (+67 more, see impacted.tsv)

</details>

<details><summary><code>enum bpf_arg_type</code> (bpf.h:784:1)</summary>

```
  type size hasn't changed
  1 enumerator change:
    'bpf_arg_type::__BPF_ARG_TYPE_LIMIT' from value '134217727' to '268435455' at bpf.h:802:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>enum bpf_reg_type</code> (bpf.h:941:1)</summary>

```
  type size hasn't changed
  1 enumerator change:
    'bpf_reg_type::__BPF_REG_TYPE_LIMIT' from value '134217727' to '268435455' at bpf.h:959:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>enum bpf_return_type</code> (bpf.h:843:1)</summary>

```
  type size hasn't changed
  1 enumerator change:
    'bpf_return_type::__BPF_RET_TYPE_LIMIT' from value '134217727' to '268435455' at bpf.h:861:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct bio</code> (blk_types.h:214:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'bio_vec bi_inline_vecs[]', at offset 960 (in bits) at blk_types.h:278:1
  there are data member changes:
    type 'struct bio_issue' of 'bio::bi_issue' changed:
      entity changed from 'struct bio_issue' to 'typedef u64' at int-ll64.h:23:1
      type size hasn't changed
    and name of 'bio::bi_issue' changed to 'bio::issue_time_ns' at blk_types.h:242:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct bio_set</code> (bio.h:641:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'typedef mempool_t' of 'bio_set::bio_pool' changed:
      underlying type 'struct mempool_s' at mempool.h:18:1 changed:
        type name changed from 'mempool_s' to 'mempool'
        type size hasn't changed
    type 'typedef mempool_t' of 'bio_set::bvec_pool' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct block_device_operations</code> (blkdev.h:1650:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int (block_device*, hd_geometry*)*' of 'block_device_operations::getgeo' changed:
      pointer type changed from: 'int (block_device*, hd_geometry*)*' to: 'int (gendisk*, hd_geometry*)*'
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct bpf_map</code> (bpf.h:290:1)</summary>

```
  type size changed from 1920 to 2240 (in bits)
  2 data member insertions:
    'u8 sha[32]', at offset 0 (in bits) at bpf.h:296:1
    'char* excl_prog_sha', at offset 2176 (in bits) at bpf.h:337:1
  there are data member changes:
    'const bpf_map_ops* ops' offset changed from 0 to 256 (in bits) (by +256 bits)
    'bpf_map* inner_map_meta' offset changed from 64 to 320 (in bits) (by +256 bits)
    'void* security' offset changed from 128 to 384 (in bits) (by +256 bits)
    'bpf_map_type map_type' offset changed from 192 to 448 (in bits) (by +256 bits)
    'u32 key_size' offset changed from 224 to 480 (in bits) (by +256 bits)
    'u32 value_size' offset changed from 256 to 512 (in bits) (by +256 bits)
    'u32 max_entries' offset changed from 288 to 544 (in bits) (by +256 bits)
    'u64 map_extra' offset changed from 320 to 576 (in bits) (by +256 bits)
    'u32 map_flags' offset changed from 384 to 640 (in bits) (by +256 bits)
    'u32 id' offset changed from 416 to 672 (in bits) (by +256 bits)
    'btf_record* record' offset changed from 448 to 704 (in bits) (by +256 bits)
    'int numa_node' offset changed from 512 to 768 (in bits) (by +256 bits)
    'u32 btf_key_type_id' offset changed from 544 to 800 (in bits) (by +256 bits)
    'u32 btf_value_type_id' offset changed from 576 to 832 (in bits) (by +256 bits)
    'u32 btf_vmlinux_value_type_id' offset changed from 608 to 864 (in bits) (by +256 bits)
    'btf* btf' offset changed from 640 to 896 (in bits) (by +256 bits)
    'char name[16]' offset changed from 704 to 960 (in bits) (by +256 bits)
    'mutex freeze_mutex' offset changed from 832 to 1088 (in bits) (by +256 bits)
    'atomic64_t refcnt' offset changed from 1088 to 1344 (in bits) (by +256 bits)
    'atomic64_t usercnt' offset changed from 1152 to 1408 (in bits) (by +256 bits)
    anonymous data member 'union {work_struct work; callback_head rcu;}' offset changed from 1216 to 1472 (in bits) (by +256 bits)
    'atomic64_t writecnt' offset changed from 1472 to 1728 (in bits) (by +256 bits)
    'spinlock_t owner_lock' offset changed from 1536 to 1792 (in bits) (by +256 bits)
    'bpf_map_owner* owner' offset changed from 1600 to 1856 (in bits) (by +256 bits)
    'bool bypass_spec_v1' offset changed from 1664 to 1920 (in bits) (by +256 bits)
    'bool frozen' offset changed from 1672 to 1928 (in bits) (by +256 bits)
    'bool free_after_mult_rcu_gp' offset changed from 1680 to 1936 (in bits) (by +256 bits)
    'bool free_after_rcu_gp' offset changed from 1688 to 1944 (in bits) (by +256 bits)
    'atomic64_t sleepable_refcnt' offset changed from 1728 to 1984 (in bits) (by +256 bits)
    's64* elem_count' offset changed from 1792 to 2048 (in bits) (by +256 bits)
    'u64 cookie' offset changed from 1856 to 2112 (in bits) (by +256 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct bpf_map_ops</code> (bpf.h:82:1)</summary>

```
  type size changed from 2752 to 2816 (in bits)
  1 data member insertion:
    'int (bpf_map*, typedef u32, void*)* map_get_hash', at offset 1216 (in bits) at bpf.h:113:1
  there are data member changes:
    'void* (bpf_map*, file*, int)* map_fd_get_ptr' offset changed from 1216 to 1280 (in bits) (by +64 bits)
    'void (bpf_map*, void*, typedef bool)* map_fd_put_ptr' offset changed from 1280 to 1344 (in bits) (by +64 bits)
    'int (bpf_map*, bpf_insn*)* map_gen_lookup' offset changed from 1344 to 1408 (in bits) (by +64 bits)
    'typedef u32 (void*)* map_fd_sys_lookup_elem' offset changed from 1408 to 1472 (in bits) (by +64 bits)
    'void (bpf_map*, void*, seq_file*)* map_seq_show_elem' offset changed from 1472 to 1536 (in bits) (by +64 bits)
    'int (const bpf_map*, const btf*, const btf_type*, const btf_type*)* map_check_btf' offset changed from 1536 to 1600 (in bits) (by +64 bits)
    'int (bpf_map*, bpf_prog_aux*)* map_poke_track' offset changed from 1600 to 1664 (in bits) (by +64 bits)
    'void (bpf_map*, bpf_prog_aux*)* map_poke_untrack' offset changed from 1664 to 1728 (in bits) (by +64 bits)
    'void (bpf_map*, typedef u32, bpf_prog*, bpf_prog*)* map_poke_run' offset changed from 1728 to 1792 (in bits) (by +64 bits)
    'int (const bpf_map*, u64*, typedef u32)* map_direct_value_addr' offset changed from 1792 to 1856 (in bits) (by +64 bits)
    'int (const bpf_map*, typedef u64, u32*)* map_direct_value_meta' offset changed from 1856 to 1920 (in bits) (by +64 bits)
    'int (bpf_map*, vm_area_struct*)* map_mmap' offset changed from 1920 to 1984 (in bits) (by +64 bits)
    'typedef __poll_t (bpf_map*, file*, poll_table_struct*)* map_poll' offset changed from 1984 to 2048 (in bits) (by +64 bits)
    'unsigned long int (file*, unsigned long int, unsigned long int, unsigned long int, unsigned long int)* map_get_unmapped_area' offset changed from 2048 to 2112 (in bits) (by +64 bits)
    'int (bpf_local_storage_map*, void*, typedef u32)* map_local_storage_charge' offset changed from 2112 to 2176 (in bits) (by +64 bits)
    'void (bpf_local_storage_map*, void*, typedef u32)* map_local_storage_uncharge' offset changed from 2176 to 2240 (in bits) (by +64 bits)
    'bpf_local_storage** (void*)* map_owner_storage_ptr' offset changed from 2240 to 2304 (in bits) (by +64 bits)
    'long int (bpf_map*, typedef u64, typedef u64)* map_redirect' offset changed from 2304 to 2368 (in bits) (by +64 bits)
    'typedef bool (const bpf_map*, const bpf_map*)* map_meta_equal' offset changed from 2368 to 2432 (in bits) (by +64 bits)
    'int (bpf_verifier_env*, bpf_func_state*, bpf_func_state*)* map_set_for_each_callback_args' offset changed from 2432 to 2496 (in bits) (by +64 bits)
    'long int (bpf_map*, typedef bpf_callback_t, void*, typedef u64)* map_for_each_callback' offset changed from 2496 to 2560 (in bits) (by +64 bits)
    'typedef u64 (const bpf_map*)* map_mem_usage' offset changed from 2560 to 2624 (in bits) (by +64 bits)
    'int* map_btf_id' offset changed from 2624 to 2688 (in bits) (by +64 bits)
    'const bpf_iter_seq_info* iter_seq_info' offset changed from 2688 to 2752 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct bpf_map_owner</code> (bpf.h:282:1)</summary>

```
  type size changed from 256 to 320 (in bits)
  1 data member insertion:
    'bpf_attach_type expected_attach_type', at offset 256 (in bits) at bpf.h:292:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct bpf_offloaded_map</code> (bpf.h:619:1)</summary>

```
  type size changed from 2240 to 2560 (in bits)
  there are data member changes:
    type 'struct bpf_map' of 'bpf_offloaded_map::map' changed, as reported earlier
    'net_device* netdev' offset changed from 1920 to 2240 (in bits) (by +320 bits)
    'const bpf_map_dev_ops* dev_ops' offset changed from 1984 to 2304 (in bits) (by +320 bits)
    'void* dev_priv' offset changed from 2048 to 2368 (in bits) (by +320 bits)
    'list_head offloads' offset changed from 2112 to 2432 (in bits) (by +320 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct bpf_prog</code> (bpf.h:1693:1)</summary>

```
  type size changed from 576 to 768 (in bits)
  there are data member changes:
    data member u8 tag[8] at offset 160 (in bits) became anonymous data member 'union {u8 digest[32]; u8 tag[8];}'
    and size changed from 64 to 256 (in bits) (by +192 bits)
    'bpf_prog_stats* stats' offset changed from 256 to 448 (in bits) (by +192 bits)
    'int* active' offset changed from 320 to 512 (in bits) (by +192 bits)
    'unsigned int (void*, const bpf_insn*)* bpf_func' offset changed from 384 to 576 (in bits) (by +192 bits)
    'bpf_prog_aux* aux' offset changed from 448 to 640 (in bits) (by +192 bits)
    'sock_fprog_kern* orig_prog' offset changed from 512 to 704 (in bits) (by +192 bits)
    anonymous data member 'union {struct {struct {} __empty_insns; sock_filter insns[];}; struct {struct {} __empty_insnsi; bpf_insn insnsi[];};}' offset changed from 576 to 768 (in bits) (by +192 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct bpf_prog_aux</code> (bpf.h:1582:1)</summary>

```
  type size changed from 10304 to 10368 (in bits)
  2 data member insertions:
    'bool kprobe_write_ctx', at offset 1336 (in bits) at bpf.h:1642:1
    'bpf_prog_aux* main_prog_aux', at offset 1984 (in bits) at bpf.h:1652:1
  there are data member changes:
    'void* jit_data' offset changed from 1984 to 2048 (in bits) (by +64 bits)
    'bpf_jit_poke_descriptor* poke_tab' offset changed from 2048 to 2112 (in bits) (by +64 bits)
    'bpf_kfunc_desc_tab* kfunc_tab' offset changed from 2112 to 2176 (in bits) (by +64 bits)
    'bpf_kfunc_btf_tab* kfunc_btf_tab' offset changed from 2176 to 2240 (in bits) (by +64 bits)
    'u32 size_poke_tab' offset changed from 2240 to 2304 (in bits) (by +64 bits)
    'bpf_ksym ksym' offset changed from 2304 to 2368 (in bits) (by +64 bits)
    'const bpf_prog_ops* ops' offset changed from 7104 to 7168 (in bits) (by +64 bits)
    'const bpf_struct_ops* st_ops' offset changed from 7168 to 7232 (in bits) (by +64 bits)
    'bpf_map** used_maps' offset changed from 7232 to 7296 (in bits) (by +64 bits)
    'mutex used_maps_mutex' offset changed from 7296 to 7360 (in bits) (by +64 bits)
    'btf_mod_pair* used_btfs' offset changed from 7552 to 7616 (in bits) (by +64 bits)
    'bpf_prog* prog' offset changed from 7616 to 7680 (in bits) (by +64 bits)
    'user_struct* user' offset changed from 7680 to 7744 (in bits) (by +64 bits)
    'u64 load_time' offset changed from 7744 to 7808 (in bits) (by +64 bits)
    'u32 verified_insns' offset changed from 7808 to 7872 (in bits) (by +64 bits)
    'int cgroup_atype' offset changed from 7840 to 7904 (in bits) (by +64 bits)
    'bpf_map* cgroup_storage[2]' offset changed from 7872 to 7936 (in bits) (by +64 bits)
    'char name[16]' offset changed from 8000 to 8064 (in bits) (by +64 bits)
    'typedef u64 (typedef u64, typedef u64, typedef u64, typedef u64, typedef u64)* bpf_exception_cb' offset changed from 8128 to 8192 (in bits) (by +64 bits)
    'void* security' offset changed from 8192 to 8256 (in bits) (by +64 bits)
    'bpf_token* token' offset changed from 8256 to 8320 (in bits) (by +64 bits)
    'bpf_prog_offload* offload' offset changed from 8320 to 8384 (in bits) (by +64 bits)
    'btf* btf' offset changed from 8384 to 8448 (in bits) (by +64 bits)
    'bpf_func_info* func_info' offset changed from 8448 to 8512 (in bits) (by +64 bits)
    'bpf_func_info_aux* func_info_aux' offset changed from 8512 to 8576 (in bits) (by +64 bits)
    'bpf_line_info* linfo' offset changed from 8576 to 8640 (in bits) (by +64 bits)
    'void** jited_linfo' offset changed from 8640 to 8704 (in bits) (by +64 bits)
    'u32 func_info_cnt' offset changed from 8704 to 8768 (in bits) (by +64 bits)
    'u32 nr_linfo' offset changed from 8736 to 8800 (in bits) (by +64 bits)
    'u32 linfo_idx' offset changed from 8768 to 8832 (in bits) (by +64 bits)
    'module* mod' offset changed from 8832 to 8896 (in bits) (by +64 bits)
    'u32 num_exentries' offset changed from 8896 to 8960 (in bits) (by +64 bits)
    'exception_table_entry* extable' offset changed from 8960 to 9024 (in bits) (by +64 bits)
    anonymous data member 'union {work_struct work; callback_head rcu;}' offset changed from 9024 to 9088 (in bits) (by +64 bits)
    'bpf_stream stream[2]' offset changed from 9280 to 9344 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct btf_record</code> (bpf.h:254:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'int task_work_off', at offset 224 (in bits) at bpf.h:265:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct dst_entry</code> (dst.h:26:1)</summary>

```
  type size hasn't changed
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct gendisk</code> (blkdev.h:143:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct bio_set' of 'gendisk::bio_split' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct kmem_cache</code> (slab.h:234:1)</summary>

```
  type size changed from 5632 to 5696 (in bits)
  3 data member insertions:
    'slub_percpu_sheaves* cpu_sheaves', at offset 64 (in bits) at slab.h:243:1
    'lock_class_key lock_key', at offset 64 (in bits) at slab.h:241:1
    'unsigned int sheaf_capacity', at offset 480 (in bits) at slab.h:257:1
  there are data member changes:
    'slab_flags_t flags' offset changed from 64 to 128 (in bits) (by +64 bits)
    'unsigned long int min_partial' offset changed from 128 to 192 (in bits) (by +64 bits)
    'unsigned int size' offset changed from 192 to 256 (in bits) (by +64 bits)
    'unsigned int object_size' offset changed from 224 to 288 (in bits) (by +64 bits)
    'reciprocal_value reciprocal_size' offset changed from 256 to 320 (in bits) (by +64 bits)
    'unsigned int offset' offset changed from 320 to 384 (in bits) (by +64 bits)
    'unsigned int cpu_partial' offset changed from 352 to 416 (in bits) (by +64 bits)
    'unsigned int cpu_partial_slabs' offset changed from 384 to 448 (in bits) (by +64 bits)
    'kmem_cache_order_objects oo' offset changed from 416 to 512 (in bits) (by +96 bits)
    'kmem_cache_order_objects min' offset changed from 448 to 544 (in bits) (by +96 bits)
    'gfp_t allocflags' offset changed from 480 to 576 (in bits) (by +96 bits)
    'int refcount' offset changed from 512 to 608 (in bits) (by +96 bits)
    'void (void*)* ctor' offset changed from 576 to 640 (in bits) (by +64 bits)
    'unsigned int inuse' offset changed from 640 to 704 (in bits) (by +64 bits)
    'unsigned int align' offset changed from 672 to 736 (in bits) (by +64 bits)
    'unsigned int red_left_pad' offset changed from 704 to 768 (in bits) (by +64 bits)
    'const char* name' offset changed from 768 to 832 (in bits) (by +64 bits)
    'list_head list' offset changed from 832 to 896 (in bits) (by +64 bits)
    'kobject kobj' offset changed from 960 to 1024 (in bits) (by +64 bits)
    'unsigned int remote_node_defrag_ratio' offset changed from 1472 to 1536 (in bits) (by +64 bits)
    'kmem_cache_node* node[64]' offset changed from 1536 to 1600 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct kmem_cache_cpu</code> (slub.c:400:1)</summary>

```
  type size changed from 256 to 384 (in bits)
  there are data member changes:
    type 'typedef local_lock_t' of 'kmem_cache_cpu::lock' changed:
      typedef name changed from local_lock_t to local_trylock_t at local_lock_internal.h:25:1
      underlying type 'struct local_lock_t' at local_lock_internal.h:11:1 changed:
        type name changed from 'local_lock_t' to 'local_trylock_t'
        type size changed from 0 to 8 (in bits)
        1 data member insertion:
          'u8 acquired', at offset 0 (in bits) at local_lock_internal.h:24:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct kmem_cache_node</code> (slub.c:441:1)</summary>

```
  type size changed from 512 to 576 (in bits)
  1 data member insertion:
    'node_barn* barn', at offset 512 (in bits) at slub.c:499:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct mnt_namespace</code> (mount.h:10:1)</summary>

```
  type size changed from 1536 to 1600 (in bits)
  4 data member deletions:
    'u64 seq', at offset 576 (in bits) at mount.h:20:1
    'union {wait_queue_head_t poll; callback_head mnt_ns_rcu;}', at offset 640 (in bits)
    'rb_node mnt_ns_tree_node', at offset 1152 (in bits) at mount.h:33:1
    'list_head mnt_ns_list', at offset 1344 (in bits) at mount.h:34:1
  1 data member insertion:
    'wait_queue_head_t poll', at offset 1024 (in bits) at mount.h:20:1
  there are data member changes:
    type 'struct ns_common' of 'mnt_namespace::ns' changed, as reported earlier
    'mount* root' offset changed from 192 to 640 (in bits) (by +448 bits)
    anonymous data member 'struct {rb_root mounts; rb_node* mnt_last_node; rb_node* mnt_first_node;}' offset changed from 256 to 704 (in bits) (by +448 bits)
    'user_namespace* user_ns' offset changed from 448 to 896 (in bits) (by +448 bits)
    'ucounts* ucounts' offset changed from 512 to 960 (in bits) (by +448 bits)
    'u64 seq_origin' offset changed from 832 to 1216 (in bits) (by +384 bits)
    'u64 event' offset changed from 896 to 1280 (in bits) (by +384 bits)
    '__u32 n_fsnotify_mask' offset changed from 960 to 1344 (in bits) (by +384 bits)
    'fsnotify_mark_connector* n_fsnotify_marks' offset changed from 1024 to 1408 (in bits) (by +384 bits)
    'unsigned int nr_mounts' offset changed from 1088 to 1472 (in bits) (by +384 bits)
    'unsigned int pending_mounts' offset changed from 1120 to 1504 (in bits) (by +384 bits)
    'refcount_t passive' offset changed from 1472 to 1536 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct mount</code> (mount.h:49:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'mount** mnt_pprev_for_sb', at offset 1088 (in bits) at mount.h:62:1
  there are data member changes:
    type 'struct list_head' of 'mount::mnt_instance' changed:
      entity changed from 'struct list_head' to 'mount*'
      type size changed from 128 to 64 (in bits)
    and name of 'mount::mnt_instance' changed to 'mount::mnt_next_for_sb' at mount.h:61:1
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct msi_domain_ops</code> (msi.h:453:1)</summary>

```
  type size changed from 704 to 640 (in bits)
  1 data member deletion:
    'void (irq_domain*, device*)* msi_post_free', at offset 576 (in bits) at msi.h:476:1
  there are data member changes:
    'int (irq_domain*, irq_fwspec*, irq_hw_number_t*, unsigned int*)* msi_translate' offset changed from 640 to 576 (in bits) (by -64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct net</code> (net_namespace.h:61:1)</summary>

```
  type size changed from 30208 to 30720 (in bits)
  there are data member changes:
    type 'struct ns_common' of 'net::ns' changed, as reported earlier
    'list_head dev_base_head' offset changed from 1408 to 1856 (in bits) (by +448 bits)
    'ref_tracker_dir notrefcnt_tracker' offset changed from 1408 to 1856 (in bits) (by +448 bits)
    'ref_tracker_dir refcnt_tracker' offset changed from 1408 to 1856 (in bits) (by +448 bits)
    'proc_dir_entry* proc_net' offset changed from 1536 to 1984 (in bits) (by +448 bits)
    'proc_dir_entry* proc_net_stat' offset changed from 1600 to 2048 (in bits) (by +448 bits)
    'ctl_table_set sysctls' offset changed from 1664 to 2112 (in bits) (by +448 bits)
    'sock* rtnl' offset changed from 2496 to 2944 (in bits) (by +448 bits)
    'sock* genl_sock' offset changed from 2560 to 3008 (in bits) (by +448 bits)
    'uevent_sock* uevent_sock' offset changed from 2624 to 3072 (in bits) (by +448 bits)
    'hlist_head* dev_name_head' offset changed from 2688 to 3136 (in bits) (by +448 bits)
    'hlist_head* dev_index_head' offset changed from 2752 to 3200 (in bits) (by +448 bits)
    'xarray dev_by_index' offset changed from 2816 to 3264 (in bits) (by +448 bits)
    'raw_notifier_head netdev_chain' offset changed from 2944 to 3392 (in bits) (by +448 bits)
    'u32 hash_mix' offset changed from 3008 to 3456 (in bits) (by +448 bits)
    'net_device* loopback_dev' offset changed from 3072 to 3520 (in bits) (by +448 bits)
    'list_head rules_ops' offset changed from 3136 to 3584 (in bits) (by +448 bits)
    'netns_core core' offset changed from 3264 to 3712 (in bits) (by +448 bits)
    'netns_mib mib' offset changed from 3584 to 4032 (in bits) (by +448 bits)
    'netns_packet packet' offset changed from 4416 to 4864 (in bits) (by +448 bits)
    'netns_unix unx' offset changed from 4736 to 5184 (in bits) (by +448 bits)
    'netns_nexthop nexthop' offset changed from 4992 to 5440 (in bits) (by +448 bits)
    type 'struct netns_ipv4' of 'net::ipv4' changed:
      type size hasn't changed
      3 data member insertions:
        'u8 sysctl_tcp_ecn_option', at offset 3496 (in bits) at ipv4.h:151:1
        'u8 sysctl_tcp_ecn_option_beacon', at offset 3504 (in bits) at ipv4.h:152:1
        'u16 ping_port_rover', at offset 5376 (in bits) at ipv4.h:256:1
      there are data member changes:
        'u8 sysctl_tcp_ecn_fallback' offset changed from 3496 to 3512 (in bits) (by +16 bits)
        'u8 sysctl_ip_default_ttl' offset changed from 3504 to 3520 (in bits) (by +16 bits)
        'u8 sysctl_ip_no_pmtu_disc' offset changed from 3512 to 3528 (in bits) (by +16 bits)
        'u8 sysctl_ip_fwd_update_priority' offset changed from 3520 to 3536 (in bits) (by +16 bits)
        'u8 sysctl_ip_nonlocal_bind' offset changed from 3528 to 3544 (in bits) (by +16 bits)
        'u8 sysctl_ip_autobind_reuse' offset changed from 3536 to 3552 (in bits) (by +16 bits)
        'u8 sysctl_ip_dynaddr' offset changed from 3544 to 3560 (in bits) (by +16 bits)
        'u8 sysctl_udp_early_demux' offset changed from 3552 to 3568 (in bits) (by +16 bits)
        'u8 sysctl_nexthop_compat_mode' offset changed from 3560 to 3576 (in bits) (by +16 bits)
  ...
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct per_cpu_nodestat</code> (mmzone.h:762:1)</summary>

```
  type size changed from 384 to 392 (in bits)
  there are data member changes:
    type 's8[47]' of 'per_cpu_nodestat::vm_node_stat_diff' changed:
      type name changed from 's8[47]' to 's8[48]'
      array type size changed from 376 to 384
      array type subrange 1 changed length from 47 to 48
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct perf_buffer</code> (internal.h:13:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'typedef atomic_t' of 'perf_buffer::mmap_count' changed:
      typedef name changed from atomic_t to refcount_t at refcount_types.h:17:1
      underlying type 'struct atomic_t' at types.h:181:1 changed:
        type name changed from 'atomic_t' to 'refcount_struct'
        type size hasn't changed
        there are data member changes:
          type 'int' of 'atomic_t::counter' changed:
            entity changed from 'int' to 'typedef atomic_t' at types.h:183:1
            type size hasn't changed
          and name of 'atomic_t::counter' changed to 'refcount_struct::refs' at refcount_types.h:16:1
    type 'typedef atomic_t' of 'perf_buffer::aux_mmap_count' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct perf_event</code> (perf_event.h:764:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'typedef atomic_t' of 'perf_event::mmap_count' changed, as reported earlier
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct pglist_data</code> (mmzone.h:1360:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int' of 'pglist_data::kswapd_failures' changed:
      entity changed from 'int' to 'typedef atomic_t' at types.h:183:1
      type size hasn't changed
    type 'atomic_long_t[47]' of 'pglist_data::vm_stat' changed:
      type name changed from 'atomic_long_t[47]' to 'atomic_long_t[48]'
      array type size changed from 3008 to 3072
      array type subrange 1 changed length from 47 to 48
    'memory_tier* memtier' offset changed from 112128 to 112192 (in bits) (by +64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct proc_ns_operations</code> (proc_ns.h:17:1)</summary>

```
  type size changed from 512 to 448 (in bits)
  1 data member deletion:
    'int type', at offset 128 (in bits) at proc_ns.h:20:1
  there are data member changes:
    'ns_common* (task_struct*)* get' offset changed from 192 to 128 (in bits) (by -64 bits)
    'void (ns_common*)* put' offset changed from 256 to 192 (in bits) (by -64 bits)
    'int (nsset*, ns_common*)* install' offset changed from 320 to 256 (in bits) (by -64 bits)
    'user_namespace* (ns_common*)* owner' offset changed from 384 to 320 (in bits) (by -64 bits)
    'ns_common* (ns_common*)* get_parent' offset changed from 448 to 384 (in bits) (by -64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct proto</code> (sock.h:1251:1)</summary>

```
  type size changed from 3584 to 3520 (in bits)
  1 data member deletion:
    'unsigned int* orphan_count', at offset 2816 (in bits) at sock.h:1349:1
  there are data member changes:
    'request_sock_ops* rsk_prot' offset changed from 2880 to 2816 (in bits) (by -64 bits)
    'timewait_sock_ops* twsk_prot' offset changed from 2944 to 2880 (in bits) (by -64 bits)
    'union {inet_hashinfo* hashinfo; udp_table* udp_table; raw_hashinfo* raw_hash; smc_hashinfo* smc_hash;} h' offset changed from 3008 to 2944 (in bits) (by -64 bits)
    'module* owner' offset changed from 3072 to 3008 (in bits) (by -64 bits)
    'char name[32]' offset changed from 3136 to 3072 (in bits) (by -64 bits)
    'list_head node' offset changed from 3392 to 3328 (in bits) (by -64 bits)
    'int (sock*, int)* diag_destroy' offset changed from 3520 to 3456 (in bits) (by -64 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct sock</code> (sock.h:352:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'mem_cgroup* sk_memcg', at offset 2368 (in bits) at sock.h:447:1
  1 data member insertion:
    'numa_drop_counters* sk_drop_counters', at offset 5824 (in bits) at sock.h:574:1
  there are data member changes:
    'xfrm_policy* sk_policy[2]' offset changed from 2432 to 2368 (in bits) (by -64 bits)
    '__u8 __cacheline_group_begin__sock_write_rxtx[]' offset changed from 2560 to 2496 (in bits) (by -64 bits)
    '__u8 __cacheline_group_end__sock_read_rxtx[]' offset changed from 2560 to 2496 (in bits) (by -64 bits)
    'socket_lock_t sk_lock' offset changed from 2560 to 2496 (in bits) (by -64 bits)
    'u32 sk_reserved_mem' offset changed from 2816 to 2752 (in bits) (by -64 bits)
    'int sk_forward_alloc' offset changed from 2848 to 2784 (in bits) (by -64 bits)
    'u32 sk_tsflags' offset changed from 2880 to 2816 (in bits) (by -64 bits)
    '__u8 __cacheline_group_begin__sock_write_tx[]' offset changed from 2912 to 2848 (in bits) (by -64 bits)
    '__u8 __cacheline_group_end__sock_write_rxtx[]' offset changed from 2912 to 2848 (in bits) (by -64 bits)
    'int sk_write_pending' offset changed from 2912 to 2848 (in bits) (by -64 bits)
    'atomic_t sk_omem_alloc' offset changed from 2944 to 2880 (in bits) (by -64 bits)
    'int sk_sndbuf' offset changed from 2976 to 4480 (in bits) (by +1504 bits)
    'int sk_wmem_queued' offset changed from 3008 to 2944 (in bits) (by -64 bits)
    'refcount_t sk_wmem_alloc' offset changed from 3040 to 2976 (in bits) (by -64 bits)
    'unsigned long int sk_tsq_flags' offset changed from 3072 to 3008 (in bits) (by -64 bits)
    anonymous data member 'union {sk_buff* sk_send_head; rb_root tcp_rtx_queue;}' offset changed from 3136 to 3072 (in bits) (by -64 bits)
    'sk_buff_head sk_write_queue' offset changed from 3200 to 3136 (in bits) (by -64 bits)
    'u32 sk_dst_pending_confirm' offset changed from 3392 to 3328 (in bits) (by -64 bits)
    'u32 sk_pacing_status' offset changed from 3424 to 3360 (in bits) (by -64 bits)
    'page_frag sk_frag' offset changed from 3456 to 3392 (in bits) (by -64 bits)
    'timer_list sk_timer' offset changed from 3584 to 3520 (in bits) (by -64 bits)
    'unsigned long int sk_pacing_rate' offset changed from 3904 to 3840 (in bits) (by -64 bits)
    'atomic_t sk_zckey' offset changed from 3968 to 3904 (in bits) (by -64 bits)
    'atomic_t sk_tskey' offset changed from 4000 to 3936 (in bits) (by -64 bits)
    '__u8 __cacheline_group_begin__sock_read_tx[]' offset changed from 4032 to 3968 (in bits) (by -64 bits)
    '__u8 __cacheline_group_end__sock_write_tx[]' offset changed from 4032 to 3968 (in bits) (by -64 bits)
    'unsigned long int sk_max_pacing_rate' offset changed from 4032 to 3968 (in bits) (by -64 bits)
    'long int sk_sndtimeo' offset changed from 4096 to 4032 (in bits) (by -64 bits)
    'u32 sk_priority' offset changed from 4160 to 4096 (in bits) (by -64 bits)
    'u32 sk_mark' offset changed from 4192 to 4128 (in bits) (by -64 bits)
    'u8 sk_pacing_shift' offset changed from 4480 to 4512 (in bits) (by +32 bits)
    'bool sk_use_task_frag' offset changed from 4488 to 4520 (in bits) (by +32 bits)
    '__u8 __cacheline_group_end__sock_read_tx[]' offset changed from 4496 to 4528 (in bits) (by +32 bits)
    'u8 sk_gso_disabled' offset changed from 4496 to 4528 (in bits) (by +32 bits)
  ...
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>union bpf_attr</code> (bpf.h:1484:1)</summary>

```
  type size changed from 1216 to 1344 (in bits)
  1 data member deletion:
    'struct {__u32 map_type; __u32 key_size; __u32 value_size; __u32 max_entries; __u32 map_flags; __u32 inner_map_fd; __u32 numa_node; char map_name[16]; __u32 map_ifindex; __u32 btf_fd; __u32 btf_key_type_id; __u32 btf_value_type_id; __u32 btf_vmlinux_value_type_id; __u64 map_extra; __s32 value_type_btf_obj_fd; __s32 map_token_fd;}'
  1 data member insertion:
    'struct {__u32 prog_type; __u32 insn_cnt; __u64 insns; __u64 license; __u32 log_level; __u32 log_size; __u64 log_buf; __u32 kern_version; __u32 prog_flags; char prog_name[16]; __u32 prog_ifindex; __u32 expected_attach_type; __u32 prog_btf_fd; __u32 func_info_rec_size; __u64 func_info; __u32 func_info_cnt; __u32 line_info_rec_size; __u64 line_info; __u32 line_info_cnt; __u32 attach_btf_id; union {__u32 attach_prog_fd; __u32 attach_btf_obj_fd;}; __u32 core_relo_cnt; __u64 fd_array; __u64 core_relos; __u32 core_relo_rec_size; __u32 log_true_size; __s32 prog_token_fd; __u32 fd_array_cnt; __u64 signature; __u32 signature_size; __s32 keyring_id;}'
  there are data member changes:
    anonymous data member at offset 0 (in bits) changed from:
      struct {__u32 prog_type; __u32 insn_cnt; __u64 insns; __u64 license; __u32 log_level; __u32 log_size; __u64 log_buf; __u32 kern_version; __u32 prog_flags; char prog_name[16]; __u32 prog_ifindex; __u32 expected_attach_type; __u32 prog_btf_fd; __u32 func_info_rec_size; __u64 func_info; __u32 func_info_cnt; __u32 line_info_rec_size; __u64 line_info; __u32 line_info_cnt; __u32 attach_btf_id; union {__u32 attach_prog_fd; __u32 attach_btf_obj_fd;}; __u32 core_relo_cnt; __u64 fd_array; __u64 core_relos; __u32 core_relo_rec_size; __u32 log_true_size; __s32 prog_token_fd; __u32 fd_array_cnt;}
    to:
      struct {__u32 map_type; __u32 key_size; __u32 value_size; __u32 max_entries; __u32 map_flags; __u32 inner_map_fd; __u32 numa_node; char map_name[16]; __u32 map_ifindex; __u32 btf_fd; __u32 btf_key_type_id; __u32 btf_value_type_id; __u32 btf_vmlinux_value_type_id; __u64 map_extra; __s32 value_type_btf_obj_fd; __s32 map_token_fd; __u64 excl_prog_hash; __u32 excl_prog_hash_size;}
    and size changed from 1216 to 768 (in bits) (by -448 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+475 more, see impacted.tsv)

</details>

<details><summary><code>struct trace_iterator</code> (trace_events.h:96:1)</summary>

```
  type size changed from 132736 to 132608 (in bits)
  there are data member changes:
    type 'struct trace_seq' of 'trace_iterator::tmp_seq' changed:
      type size changed from 65600 to 65536 (in bits)
      there are data member changes:
        'char buffer[8156]' offset changed from 0 to 288 (in bits) (by +288 bits)
        'seq_buf seq' offset changed from 65280 to 0 (in bits) (by -65280 bits)
        'size_t readpos' offset changed from 65472 to 192 (in bits) (by -65280 bits)
        'int full' offset changed from 65536 to 256 (in bits) (by -65280 bits)
    'cpumask_var_t started' offset changed from 66560 to 66496 (in bits) (by -64 bits)
    'bool closed' offset changed from 66624 to 66560 (in bits) (by -64 bits)
    'bool snapshot' offset changed from 66632 to 66568 (in bits) (by -64 bits)
    type 'struct trace_seq' of 'trace_iterator::seq' changed, as reported earlier
    and offset changed from 66688 to 66624 (in bits) (by -64 bits)
    'trace_entry* ent' offset changed from 132288 to 132160 (in bits) (by -128 bits)
    'unsigned long int lost_events' offset changed from 132352 to 132224 (in bits) (by -128 bits)
    'int leftover' offset changed from 132416 to 132288 (in bits) (by -128 bits)
    'int ent_size' offset changed from 132448 to 132320 (in bits) (by -128 bits)
    'int cpu' offset changed from 132480 to 132352 (in bits) (by -128 bits)
    'u64 ts' offset changed from 132544 to 132416 (in bits) (by -128 bits)
    'loff_t pos' offset changed from 132608 to 132480 (in bits) (by -128 bits)
    'long int idx' offset changed from 132672 to 132544 (in bits) (by -128 bits)
```

Reaches: `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong`, `const kernel_param_ops param_ops_ulong`, `const bus_type pci_bus_type`, `const file_operations relay_file_operations`, `function page* __alloc_pages_noprof(gfp_t, unsigned int, int, nodemask_t*)` … (+477 more, see impacted.tsv)

</details>

<details><summary><code>struct pid_namespace</code> (pid_namespace.h:26:1)</summary>

```
  type size changed from 2304 to 2752 (in bits)
  there are data member changes:
    type 'struct ns_common' of 'pid_namespace::ns' changed, as reported earlier
    'work_struct work' offset changed from 1088 to 1536 (in bits) (by +448 bits)
    'ctl_table_set set' offset changed from 1344 to 1792 (in bits) (by +448 bits)
    'ctl_table_header* sysctls' offset changed from 2176 to 2624 (in bits) (by +448 bits)
    'int memfd_noexec_scope' offset changed from 2240 to 2688 (in bits) (by +448 bits)
```

Reaches: `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string`, `const kernel_param_ops param_ops_uint`, `const kernel_param_ops param_ops_ullong` … (+479 more, see impacted.tsv)

</details>

<details><summary><code>struct cgroup</code> (cgroup-defs.h:438:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cgroup_freezer_state' of 'cgroup::freezer' changed:
      type size changed from 96 to 256 (in bits)
      3 data member insertions:
        'seqcount_spinlock_t freeze_seq', at offset 96 (in bits) at cgroup-defs.h:455:1
        'u64 freeze_start_nsec', at offset 128 (in bits) at cgroup-defs.h:462:1
        'u64 frozen_nsec', at offset 192 (in bits) at cgroup-defs.h:469:1
    'cgroup* ancestors[]' offset changed from 8384 to 8512 (in bits) (by +128 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string` … (+481 more, see impacted.tsv)

</details>

<details><summary><code>struct cgroup_namespace</code> (cgroup.h:786:1)</summary>

```
  type size changed from 384 to 832 (in bits)
  there are data member changes:
    type 'struct ns_common' of 'cgroup_namespace::ns' changed:
      type size changed from 192 to 640 (in bits)
      1 data member deletion:
        'refcount_t count', at offset 160 (in bits) at ns_common.h:13:1
      3 data member insertions:
        'u32 ns_type', at offset 0 (in bits) at ns_common.h:41:1
        'refcount_t __ns_ref', at offset 224 (in bits) at ns_common.h:45:1
        'union {struct {u64 ns_id; rb_node ns_tree_node; list_head ns_list_node;}; callback_head ns_rcu;}', at offset 256 (in bits)
      there are data member changes:
        'dentry* stashed' offset changed from 0 to 64 (in bits) (by +64 bits)
        'const proc_ns_operations* ops' offset changed from 64 to 128 (in bits) (by +64 bits)
        'unsigned int inum' offset changed from 128 to 192 (in bits) (by +64 bits)
    'user_namespace* user_ns' offset changed from 192 to 640 (in bits) (by +448 bits)
    'ucounts* ucounts' offset changed from 256 to 704 (in bits) (by +448 bits)
    'css_set* root_cset' offset changed from 320 to 768 (in bits) (by +448 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string` … (+481 more, see impacted.tsv)

</details>

<details><summary><code>struct cgroup_root</code> (cgroup-defs.h:603:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cgroup' of 'cgroup_root::cgrp' changed, as reported earlier
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string` … (+481 more, see impacted.tsv)

</details>

<details><summary><code>struct cgroup_subsys</code> (cgroup-defs.h:732:1)</summary>

```
  type size changed from 2112 to 2048 (in bits)
  1 data member deletion:
    'void ()* post_attach', at offset 832 (in bits) at cgroup-defs.h:749:1
  there are data member changes:
    'int (task_struct*, css_set*)* can_fork' offset changed from 896 to 832 (in bits) (by -64 bits)
    'void (task_struct*, css_set*)* cancel_fork' offset changed from 960 to 896 (in bits) (by -64 bits)
    'void (task_struct*)* fork' offset changed from 1024 to 960 (in bits) (by -64 bits)
    'void (task_struct*)* exit' offset changed from 1088 to 1024 (in bits) (by -64 bits)
    'void (task_struct*)* release' offset changed from 1152 to 1088 (in bits) (by -64 bits)
    'void (cgroup_subsys_state*)* bind' offset changed from 1216 to 1152 (in bits) (by -64 bits)
    'bool early_init' offset changed from 1280 to 1216 (in bits) (by -64 bits)
    'bool implicit_on_dfl' offset changed from 1281 to 1217 (in bits) (by -64 bits)
    'bool threaded' offset changed from 1282 to 1218 (in bits) (by -64 bits)
    'int id' offset changed from 1312 to 1248 (in bits) (by -64 bits)
    'const char* name' offset changed from 1344 to 1280 (in bits) (by -64 bits)
    'const char* legacy_name' offset changed from 1408 to 1344 (in bits) (by -64 bits)
    'cgroup_root* root' offset changed from 1472 to 1408 (in bits) (by -64 bits)
    'idr css_idr' offset changed from 1536 to 1472 (in bits) (by -64 bits)
    'list_head cfts' offset changed from 1728 to 1664 (in bits) (by -64 bits)
    'cftype* dfl_cftypes' offset changed from 1856 to 1792 (in bits) (by -64 bits)
    'cftype* legacy_cftypes' offset changed from 1920 to 1856 (in bits) (by -64 bits)
    'unsigned int depends_on' offset changed from 1984 to 1920 (in bits) (by -64 bits)
    'spinlock_t rstat_ss_lock' offset changed from 2016 to 1952 (in bits) (by -64 bits)
    'llist_head* lhead' offset changed from 2048 to 1984 (in bits) (by -64 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string` … (+481 more, see impacted.tsv)

</details>

<details><summary><code>struct user_namespace</code> (user_namespace.h:76:1)</summary>

```
  type size changed from 4736 to 5184 (in bits)
  there are data member changes:
    type 'struct ns_common' of 'user_namespace::ns' changed, as reported earlier
    'unsigned long int flags' offset changed from 1920 to 2368 (in bits) (by +448 bits)
    'bool parent_could_setfcap' offset changed from 1984 to 2432 (in bits) (by +448 bits)
    'list_head keyring_name_list' offset changed from 2048 to 2496 (in bits) (by +448 bits)
    'key* user_keyring_register' offset changed from 2176 to 2624 (in bits) (by +448 bits)
    'rw_semaphore keyring_sem' offset changed from 2240 to 2688 (in bits) (by +448 bits)
    'work_struct work' offset changed from 2560 to 3008 (in bits) (by +448 bits)
    'ctl_table_set set' offset changed from 2816 to 3264 (in bits) (by +448 bits)
    'ctl_table_header* sysctls' offset changed from 3648 to 4096 (in bits) (by +448 bits)
    'ucounts* ucounts' offset changed from 3712 to 4160 (in bits) (by +448 bits)
    'long int ucount_max[10]' offset changed from 3776 to 4224 (in bits) (by +448 bits)
    'long int rlimit_max[4]' offset changed from 4416 to 4864 (in bits) (by +448 bits)
    'binfmt_misc* binfmt_misc' offset changed from 4672 to 5120 (in bits) (by +448 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint`, `const kernel_param_ops param_ops_int`, `const kernel_param_ops param_ops_string` … (+481 more, see impacted.tsv)

</details>

<details><summary><code>struct arch_uprobe</code> (uprobes.h:25:1)</summary>

```
  type size changed from 256 to 320 (in bits)
  1 data member insertion:
    'unsigned long int flags', at offset 256 (in bits) at uprobes.h:54:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct attribute_group</code> (sysfs.h:99:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    anonymous data member union {const bin_attribute* const* bin_attrs; const bin_attribute* const* bin_attrs_new;} at offset 320 (in bits) became data member 'const bin_attribute* const* bin_attrs'
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct bin_attribute</code> (sysfs.h:304:1)</summary>

```
  type size changed from 704 to 576 (in bits)
  2 data member deletions:
    'typedef ssize_t (file*, kobject*, const bin_attribute*, char*, typedef loff_t, typedef size_t)* read_new', at offset 384 (in bits) at sysfs.h:311:1
    'typedef ssize_t (file*, kobject*, const bin_attribute*, char*, typedef loff_t, typedef size_t)* write_new', at offset 512 (in bits) at sysfs.h:315:1
  there are data member changes:
    'typedef ssize_t (file*, kobject*, const bin_attribute*, char*, typedef loff_t, typedef size_t)* write' offset changed from 448 to 384 (in bits) (by -64 bits)
    'typedef loff_t (file*, kobject*, const bin_attribute*, typedef loff_t, int)* llseek' offset changed from 576 to 448 (in bits) (by -128 bits)
    'int (file*, kobject*, const bin_attribute*, vm_area_struct*)* mmap' offset changed from 640 to 512 (in bits) (by -128 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct dentry</code> (dcache.h:92:1)</summary>

```
  type size hasn't changed
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct file</code> (fs.h:1099:1)</summary>

```
  type size hasn't changed
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct inode</code> (fs.h:675:1)</summary>

```
  type size hasn't changed
  there are data member changes:
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct mm_struct</code> (mm_types.h:937:1)</summary>

```
  type size hasn't changed
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct page</code> (mm_types.h:73:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'unsigned long int' of 'page::flags' changed:
      entity changed from 'unsigned long int' to 'typedef memdesc_flags_t' at mm_types.h:39:1
      type size hasn't changed
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct signal_struct</code> (signal.h:94:1)</summary>

```
  type size changed from 8768 to 9088 (in bits)
  1 data member insertion:
    'rw_semaphore cgroup_threadgroup_rwsem', at offset 8064 (in bits) at signal.h:230:1
  there are data member changes:
    'bool oom_flag_origin' offset changed from 8064 to 8384 (in bits) (by +320 bits)
    'short int oom_score_adj' offset changed from 8080 to 8400 (in bits) (by +320 bits)
    'short int oom_score_adj_min' offset changed from 8096 to 8416 (in bits) (by +320 bits)
    'mm_struct* oom_mm' offset changed from 8128 to 8448 (in bits) (by +320 bits)
    'mutex cred_guard_mutex' offset changed from 8192 to 8512 (in bits) (by +320 bits)
    'rw_semaphore exec_update_lock' offset changed from 8448 to 8768 (in bits) (by +320 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct super_block</code> (fs.h:1328:1)</summary>

```
  type size changed from 10752 to 10240 (in bits)
  there are data member changes:
    type 'struct list_head' of 'super_block::s_mounts' changed:
      entity changed from 'struct list_head' to 'mount*'
      type size changed from 128 to 64 (in bits)
    'block_device* s_bdev' offset changed from 1600 to 1536 (in bits) (by -64 bits)
    'file* s_bdev_file' offset changed from 1664 to 1600 (in bits) (by -64 bits)
    'backing_dev_info* s_bdi' offset changed from 1728 to 1664 (in bits) (by -64 bits)
    'mtd_info* s_mtd' offset changed from 1792 to 1728 (in bits) (by -64 bits)
    'hlist_node s_instances' offset changed from 1856 to 1792 (in bits) (by -64 bits)
    'unsigned int s_quota_types' offset changed from 1984 to 1920 (in bits) (by -64 bits)
    'quota_info s_dquot' offset changed from 2048 to 1984 (in bits) (by -64 bits)
    'sb_writers s_writers' offset changed from 4544 to 4480 (in bits) (by -64 bits)
    'void* s_fs_info' offset changed from 7040 to 6976 (in bits) (by -64 bits)
    'u32 s_time_gran' offset changed from 7104 to 7040 (in bits) (by -64 bits)
    'time64_t s_time_min' offset changed from 7168 to 7104 (in bits) (by -64 bits)
    'time64_t s_time_max' offset changed from 7232 to 7168 (in bits) (by -64 bits)
    'u32 s_fsnotify_mask' offset changed from 7296 to 7232 (in bits) (by -64 bits)
    'fsnotify_sb_info* s_fsnotify_info' offset changed from 7360 to 7296 (in bits) (by -64 bits)
    'char s_id[32]' offset changed from 7424 to 7360 (in bits) (by -64 bits)
    'uuid_t s_uuid' offset changed from 7680 to 7616 (in bits) (by -64 bits)
    'u8 s_uuid_len' offset changed from 7808 to 7744 (in bits) (by -64 bits)
    'char s_sysfs_name[37]' offset changed from 7816 to 7752 (in bits) (by -64 bits)
    'unsigned int s_max_links' offset changed from 8128 to 8064 (in bits) (by -64 bits)
    'unsigned int s_d_flags' offset changed from 8160 to 8096 (in bits) (by -64 bits)
    'mutex s_vfs_rename_mutex' offset changed from 8192 to 8128 (in bits) (by -64 bits)
    'const char* s_subtype' offset changed from 8448 to 8384 (in bits) (by -64 bits)
    'const dentry_operations* __s_d_op' offset changed from 8512 to 8448 (in bits) (by -64 bits)
    'shrinker* s_shrink' offset changed from 8576 to 8512 (in bits) (by -64 bits)
    'atomic_long_t s_remove_count' offset changed from 8640 to 8576 (in bits) (by -64 bits)
    'int s_readonly_remount' offset changed from 8704 to 8640 (in bits) (by -64 bits)
    'errseq_t s_wb_err' offset changed from 8736 to 8672 (in bits) (by -64 bits)
    'workqueue_struct* s_dio_done_wq' offset changed from 8768 to 8704 (in bits) (by -64 bits)
    'hlist_head s_pins' offset changed from 8832 to 8768 (in bits) (by -64 bits)
    'user_namespace* s_user_ns' offset changed from 8896 to 8832 (in bits) (by -64 bits)
    'list_lru s_dentry_lru' offset changed from 8960 to 8896 (in bits) (by -64 bits)
    'list_lru s_inode_lru' offset changed from 9024 to 8960 (in bits) (by -64 bits)
    'callback_head rcu' offset changed from 9088 to 9024 (in bits) (by -64 bits)
    'work_struct destroy_work' offset changed from 9216 to 9152 (in bits) (by -64 bits)
    'mutex s_sync_lock' offset changed from 9472 to 9408 (in bits) (by -64 bits)
  ...
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct uprobes_state</code> (uprobes.h:186:1)</summary>

```
  type size changed from 64 to 128 (in bits)
  1 data member insertion:
    'hlist_head head_tramps', at offset 64 (in bits) at uprobes.h:190:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct vm_area_desc</code> (mm_types.h:786:1)</summary>

```
  type size changed from 576 to 640 (in bits)
  1 data member insertion:
    'file* vm_file', at offset 320 (in bits) at mm_types.h:792:1
  there are data member changes:
    'unsigned long int start' offset changed from 64 to 128 (in bits) (by +64 bits)
    'unsigned long int end' offset changed from 128 to 192 (in bits) (by +64 bits)
    'unsigned long int pgoff' offset changed from 192 to 256 (in bits) (by +64 bits)
    type 'file*' of 'vm_area_desc::file' changed:
      entity changed from 'file*' to 'file* const'
      type size hasn't changed
    and offset changed from 256 to 64 (in bits) (by -192 bits)
    'vm_flags_t vm_flags' offset changed from 320 to 384 (in bits) (by +64 bits)
    'pgprot_t page_prot' offset changed from 384 to 448 (in bits) (by +64 bits)
    'const vm_operations_struct* vm_ops' offset changed from 448 to 512 (in bits) (by +64 bits)
    'void* private_data' offset changed from 512 to 576 (in bits) (by +64 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct vm_operations_struct</code> (mm.h:586:1)</summary>

```
  type size changed from 1024 to 960 (in bits)
  1 data member deletion:
    'page* (vm_area_struct*, unsigned long int)* find_special_page', at offset 960 (in bits) at mm.h:656:1
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+483 more, see impacted.tsv)

</details>

<details><summary><code>struct hrtimer_clock_base</code> (hrtimer_defs.h:47:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'typedef ktime_t ()* get_time', at offset 384 (in bits) at hrtimer_defs.h:54:1
  there are data member changes:
    'ktime_t offset' offset changed from 448 to 384 (in bits) (by -64 bits)
```

Reaches: `const i2c_algorithm i2c_bit_algo`, `function int i2c_bit_add_bus(i2c_adapter*)`, `function void cec_fill_conn_info_from_drm(cec_connector_info*, const drm_connector*)`, `function cec_notifier* cec_notifier_conn_register(device*, const char*, const cec_connector_info*)`, `function void cec_notifier_conn_unregister(cec_notifier*)`, `function void cec_notifier_set_phys_addr(cec_notifier*, u16)`, `function int virtio_dma_buf_attach(dma_buf*, dma_buf_attachment*)`, `function dma_buf* virtio_dma_buf_export(const dma_buf_export_info*)`, `agp_bridge_data* (pci_dev*)* agp_find_bridge`, `const bus_type i2c_bus_type`, `const sysfs_ops kobj_sysfs_ops`, `const kernel_param_ops param_ops_bint`, `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_charp`, `const kernel_param_ops param_ops_hexint` … (+489 more, see impacted.tsv)

</details>

## Header-level interfaces

Macros, static inline functions, struct/union/enum tags, typedefs and enumerators defined in non-DRM Linux headers (`include/`, `arch/x86/include/`) and named in the compiled DRM sources. These never appear as ELF symbols, but LinuxKPI has to provide them. Name-based, so a name can occasionally be a false positive (e.g. a struct member that happens to share a macro's name).

| | count |
|---|---|
| used in v6.17 | 2949 |
| used in v6.18 | 2982 |
| newly used | 40 |
| no longer used | 7 |
| likely renames | 0 |
| macro/inline signature changed | 15 |
| macro body changed | 7 |
| moved to another header | 1 |

### Likely renames (header)

None.

### Newly used (header)

| name | kind | header | signature | used by |
|---|---|---|---|---|
| `BACKLIGHT_SCALE_LINEAR` | enumerator | include/linux/backlight.h |  | amdgpu |
| `BACKLIGHT_SCALE_NON_LINEAR` | enumerator | include/linux/backlight.h |  | amdgpu |
| `FIELD_PREP_WM16` | macro | include/linux/hw_bitfield.h | `(_mask,_val)` | drm-headers |
| `PATH_MAX` | macro | include/uapi/linux/limits.h |  | xe |
| `PCI_COMMAND_MASTER` | macro | include/uapi/linux/pci_regs.h |  | xe |
| `PCI_EXP_TYPE_DOWNSTREAM` | macro | include/uapi/linux/pci_regs.h |  | amdgpu |
| `PCI_EXP_TYPE_UPSTREAM` | macro | include/uapi/linux/pci_regs.h |  | amdgpu |
| `PCI_VENDOR_ID` | macro | include/uapi/linux/pci_regs.h |  | amdgpu |
| `PCI_VENDOR_ID_AMD` | macro | include/linux/pci_ids.h |  | amdgpu |
| `SYSTEM_POWER_OFF` | enumerator | include/linux/kernel.h |  | amdgpu |
| `TAINT_TEST` | macro | include/linux/panic.h |  | xe |
| `atomic_read_acquire` | inline | include/linux/atomic/atomic-instrumented.h | `int(const atomic_t *v)` | amdgpu,xe |
| `bitmap_read` | inline | include/linux/bitmap.h | `unsigned long(const unsigned long *map, unsigned long start, unsigned long nbits)` | amdgpu |
| `bitmap_write` | inline | include/linux/bitmap.h | `void(unsigned long *map, unsigned long value, unsigned long start, unsigned long nbits)` | amdgpu |
| `bmap` | inline | include/linux/fs.h | `int(struct inode *inode, sector_t *block)` | amdgpu |
| `devm_add_action` | macro | include/linux/device/devres.h | `(dev,action,data)` | xe |
| `devm_mutex_init` | macro | include/linux/mutex.h | `(dev,mutex)` | xe |
| `devm_remove_action` | inline | include/linux/device/devres.h | `void(struct device *dev, void (*action)(void *), void *data)` | xe |
| `list_is_head` | inline | include/linux/list.h | `int(const struct list_head *list, const struct list_head *head)` | amdgpu |
| `list_last_entry_or_null` | macro | include/linux/list.h | `(ptr,type,member)` | drm-headers |
| `mempool` | struct | include/linux/mempool.h |  | xe |
| `no_free_ptr` | macro | include/linux/cleanup.h | `(p)` | amdgpu |
| `pci_dev_for_each_resource` | macro | include/linux/pci.h | `(dev,res,...)` | xe |
| `pci_pcie_type` | inline | include/linux/pci.h | `int(const struct pci_dev *dev)` | amdgpu |
| `pm_hibernation_mode_is_suspend` | inline | include/linux/suspend.h | `bool(void)` | amdgpu |
| `pm_ptr` | macro | include/linux/pm.h | `(_ptr)` | amdgpu |
| `pm_sleep_ptr` | macro | include/linux/pm.h | `(_ptr)` | amdgpu |
| `poll_timeout_us` | macro | include/linux/iopoll.h | `(op,cond,sleep_us,timeout_us,sleep_before_op)` | amdgpu,drm-headers,i915 |
| `poll_timeout_us_atomic` | macro | include/linux/iopoll.h | `(op,cond,delay_us,timeout_us,delay_before_op)` | i915 |
| `psp_version` | enum | include/uapi/linux/psp.h |  | amdgpu,drm-headers |
| `range_end_overflows_t` | macro | include/linux/overflow.h | `(type,start,size,max)` | i915 |
| `range_overflows` | macro | include/linux/overflow.h | `(start,size,max)` | drm_buddy,i915 |
| `range_overflows_t` | macro | include/linux/overflow.h | `(type,start,size,max)` | i915 |
| `readl_poll_timeout_atomic` | macro | include/linux/iopoll.h | `(addr,val,cond,delay_us,timeout_us)` | drm-headers |
| `reset_mode` | enum | include/uapi/linux/fd.h |  | amdgpu |
| `try_cmpxchg64` | macro | include/linux/atomic/atomic-instrumented.h | `(ptr,oldp,...)` | i915 |
| `vcalloc` | macro | include/linux/vmalloc.h | `(...)` | radeon |
| `vfs_parse_fs_string` | inline | include/linux/fs_context.h | `int(struct fs_context *fc, const char *key, const char *value)` | i915 |
| `video_is_primary_device` | macro | include/asm-generic/video.h |  | drm |
| `vmalloc_array` | macro | include/linux/vmalloc.h | `(...)` | radeon |

### No longer used (header)

| name | kind | header | signature | used by |
|---|---|---|---|---|
| `HMM_PFN_FLAGS` | enumerator | include/linux/hmm.h |  | xe |
| `HMM_PFN_VALID` | enumerator | include/linux/hmm.h |  | xe |
| `cmpxchg64` | macro | include/linux/atomic/atomic-instrumented.h | `(ptr,...)` | i915 |
| `hmm_pfn_to_map_order` | inline | include/linux/hmm.h | `unsigned int(unsigned long hmm_pfn)` | xe |
| `is_device_private_page` | inline | include/linux/memremap.h | `bool(const struct page *page)` | xe |
| `mmap_assert_locked` | inline | include/linux/mmap_lock.h | `void(const struct mm_struct *mm)` | xe |
| `nth_page` | macro | include/linux/mm.h | `(page,n)` | i915 |

### Signature changed (header)

| name | kind | header | v6.17 | v6.18 |
|---|---|---|---|---|
| `folio_batch_count` | inline | include/linux/pagevec.h | `unsigned int(struct folio_batch *fbatch)` | `unsigned int(const struct folio_batch *fbatch)` |
| `folio_batch_space` | inline | include/linux/pagevec.h | `unsigned int(struct folio_batch *fbatch)` | `unsigned int(const struct folio_batch *fbatch)` |
| `folio_nr_pages` | inline | include/linux/mm.h | `long(const struct folio *folio)` | `unsigned long(const struct folio *folio)` |
| `kmap_atomic` | inline | include/linux/highmem-internal.h | `void *(struct page *page)` | `void *(const struct page *page)` |
| `kmap_local_page` | inline | include/linux/highmem-internal.h | `void *(struct page *page)` | `void *(const struct page *page)` |
| `kmap_local_page_prot` | inline | include/linux/highmem-internal.h | `void *(struct page *page, pgprot_t prot)` | `void *(const struct page *page, pgprot_t prot)` |
| `kmap_local_page_try_from_panic` | inline | include/linux/highmem-internal.h | `void *(struct page *page)` | `void *(const struct page *page)` |
| `kunmap` | inline | include/linux/highmem-internal.h | `void(struct page *page)` | `void(const struct page *page)` |
| `kvmalloc` | macro | include/linux/slab.h | `(_size,_flags)` | `(...)` |
| `mapping_gfp_constraint` | inline | include/linux/pagemap.h | `gfp_t(struct address_space *mapping, gfp_t gfp_mask)` | `gfp_t(const struct address_space *mapping, gfp_t gfp_mask)` |
| `mapping_gfp_mask` | inline | include/linux/pagemap.h | `gfp_t(struct address_space *mapping)` | `gfp_t(const struct address_space *mapping)` |
| `page_size` | inline | include/linux/mm.h | `unsigned long(struct page *page)` | `unsigned long(const struct page *page)` |
| `read_poll_timeout_atomic` | macro | include/linux/iopoll.h | `(op,val,cond,delay_us,timeout_us,delay_before_read,args...)` | `(op,val,cond,sleep_us,timeout_us,sleep_before_read,args...)` |
| `vma_pages` | inline | include/linux/mm.h | `unsigned long(struct vm_area_struct *vma)` | `unsigned long(const struct vm_area_struct *vma)` |
| `zone_managed_pages` | inline | include/linux/mmzone.h | `unsigned long(struct zone *zone)` | `unsigned long(const struct zone *zone)` |

### Moved to another header

| name | v6.17 | v6.18 |
|---|---|---|
| `list_for_each_rcu` | include/linux/list.h | include/linux/rculist.h |

<details><summary>Macro body changed (7)</summary>

| macro | header | v6.17 | v6.18 |
|---|---|---|---|
| `DMA_BIT_MASK` | include/linux/dma-mapping.h | `(((n) == 64) ? ~0ULL : ((1ULL<<(n))-1))` | `GENMASK_ULL(n - 1, 0)` |
| `MODULE_DEVICE_TABLE` | include/linux/module.h | `static typeof(name) __mod_device_table__##type##__##name __attribute__ ((used, alias(__stringify(name))))` | `static typeof(name) __mod_device_table(type, name) __attribute__ ((used, alias(__stringify(name))))` |
| `flush_workqueue` | include/linux/workqueue.h | `({ struct workqueue_struct *_wq = (wq); if ((__builtin_constant_p(_wq == system_wq) && _wq == system_wq) \|\| (__builtin_constant_p(_wq == system_highpri_wq) && _wq == system_highpri_wq) \|\| (__builtin_c` | `({ struct workqueue_struct *_wq = (wq); if ((__builtin_constant_p(_wq == system_percpu_wq) && _wq == system_percpu_wq) \|\| (__builtin_constant_p(_wq == system_highpri_wq) && _wq == system_highpri_wq) \|` |
| `krealloc` | include/linux/slab.h | `alloc_hooks(krealloc_noprof(__VA_ARGS__))` | `krealloc_node(__VA_ARGS__, NUMA_NO_NODE)` |
| `kvrealloc` | include/linux/slab.h | `alloc_hooks(kvrealloc_noprof(__VA_ARGS__))` | `kvrealloc_node(__VA_ARGS__, NUMA_NO_NODE)` |
| `read_poll_timeout` | include/linux/iopoll.h | `({ u64 __timeout_us = (timeout_us); unsigned long __sleep_us = (sleep_us); ktime_t __timeout = ktime_add_us(ktime_get(), __timeout_us); might_sleep_if((__sleep_us) != 0); if (sleep_before_read && __sl` | `poll_timeout_us((val) = op(args), cond, sleep_us, timeout_us, sleep_before_read)` |
| `xen_pv_domain` | include/xen/xen.h | `(xen_domain_type == XEN_PV_DOMAIN)` | `(cpu_feature_enabled(X86_FEATURE_XENPV))` |

</details>

## Same interface, different set of DRM users

| symbol | v6.17 | v6.18 |
|---|---|---|
| `__mmap_lock_do_trace_acquire_returned` | amdgpu,i915,radeon,xe | amdgpu,i915,radeon |
| `__mmap_lock_do_trace_start_locking` | amdgpu,i915,radeon,xe | amdgpu,i915,radeon |
| `__tracepoint_mmap_lock_acquire_returned` | amdgpu,i915,radeon,xe | amdgpu,i915,radeon |
| `__tracepoint_mmap_lock_start_locking` | amdgpu,i915,radeon,xe | amdgpu,i915,radeon |
| `__x86_indirect_thunk_r10` | amdgpu,drm,drm_gpuvm,i915,ttm,xe | amdgpu,drm,i915,ttm,xe |
| `__x86_indirect_thunk_r8` | amdgpu,drm,drm_gpuvm,drm_kms_helper,i915,radeon,xe | amdgpu,drm,drm_kms_helper,i915,radeon,xe |
| `__x86_indirect_thunk_rcx` | amdgpu,drm,drm_kms_helper,i915,radeon,xe | amdgpu,drm,drm_kms_helper,gpu-sched,i915,radeon,xe |
| `debugfs_create_symlink` | drm | drm,xe |
| `devm_device_add_group` | amdgpu | amdgpu,xe |
| `down_read_trylock` | amdgpu,radeon | amdgpu,radeon,xe |
| `hmm_range_fault` | amdgpu,xe | amdgpu |
| `i2c_add_adapter` | amdgpu,drm_display_helper,i915,radeon,xe | drm_display_helper,i915,radeon,xe |
| `i2c_del_adapter` | amdgpu,drm_display_helper,i915,radeon,xe | drm_display_helper,i915,radeon,xe |
| `ioremap_wc` | amdgpu,i915,ttm,xe | amdgpu,i915,ttm |
| `iounmap` | amdgpu,i915,radeon,ttm,xe | amdgpu,i915,radeon,ttm |
| `mmu_interval_notifier_insert` | amdgpu,i915,radeon,xe | amdgpu,i915,radeon |
| `mmu_interval_notifier_remove` | amdgpu,i915,radeon,xe | amdgpu,i915,radeon |
| `mmu_interval_read_begin` | amdgpu,i915,radeon,xe | amdgpu,i915,radeon |
| `mod_delayed_work_on` | drm_kms_helper,gpu-sched,i915,xe | amdgpu,drm_kms_helper,gpu-sched,i915,xe |
| `mutex_lock` | amdgpu,drm,drm_display_helper,drm_kms_helper,i915,radeon,ttm,virtio-gpu,xe | amdgpu,amdxcp,drm,drm_display_helper,drm_kms_helper,i915,radeon,ttm,virtio-gpu,xe |
| `mutex_unlock` | amdgpu,drm,drm_display_helper,drm_kms_helper,i915,radeon,ttm,virtio-gpu,xe | amdgpu,amdxcp,drm,drm_display_helper,drm_kms_helper,i915,radeon,ttm,virtio-gpu,xe |
| `strncmp` | amdgpu,drm,i915,radeon | amdgpu,drm,i915,radeon,xe |
| `system_wq` | amdgpu,drm,drm_display_helper,drm_kms_helper,gpu-sched,i915,radeon,virtio-gpu,xe | amdgpu,drm_kms_helper,gpu-sched,xe |
| `vmalloc_noprof` | amdgpu,radeon | amdgpu |
| `vmemdup_user` | virtio-gpu | amdgpu,virtio-gpu |
| `vmf_insert_pfn` | drm_shmem_helper | drm_shmem_helper,xe |
| `vzalloc_noprof` | amdgpu,radeon | amdgpu |

