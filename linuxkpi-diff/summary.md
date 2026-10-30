# DRM → kernel interface usage, v6.15 … v6.18

| version | interfaces used |
|---|---|
| v6.15 | 1046 |
| v6.16 | 1050 |
| v6.17 | 1071 |
| v6.18 | 1082 |

Symbol-level counts include renames; see each report.

| step | newly used | no longer used | declaration changed | changed types | header: newly / no longer used | report |
|---|---|---|---|---|---|---|
| v6.15 → v6.16 | 11 | 7 | 6 | 70 | n/a | diff-v6.15..v6.16/report.md |
| v6.16 → v6.17 | 24 | 3 | 5 | 64 | n/a | diff-v6.16..v6.17/report.md |
| v6.17 → v6.18 | 13 | 2 | 7 | 58 | 40 / 7 | diff-v6.17..v6.18/report.md |

## Used in v6.18 but not in v6.15 (48)

| symbol | first used | exporter | defined in | used by |
|---|---|---|---|---|
| `USER_PTR_MAX` | v6.18 | vmlinux | arch/x86/include/asm/uaccess_64.h | drm,i915,radeon |
| `__devm_regmap_init` | v6.17 | vmlinux | drivers/base/regmap/regmap.c | xe |
| `__put_task_struct_rcu_cb` | v6.17 | vmlinux | kernel/fork.c | amdgpu,xe |
| `alloc_workqueue_noprof` | v6.17 | vmlinux | kernel/workqueue.c | amdgpu,drm_display_helper,gpu-sched,i915,radeon,ttm,xe |
| `compat_vma_mmap_prepare` | v6.16 | vmlinux | mm/util.c | i915 |
| `device_property_present` | v6.17 | vmlinux | drivers/base/property.c | drm |
| `devm_i2c_add_adapter` | v6.18 | vmlinux | drivers/i2c/i2c-core-base.c | amdgpu |
| `devm_remove_action_nowarn` | v6.18 | vmlinux | drivers/base/devres.c | xe |
| `dma_fence_dedup_array` | v6.16 | vmlinux | drivers/dma-buf/dma-fence-unwrap.c | amdgpu |
| `dma_fence_driver_name` | v6.17 | vmlinux | drivers/dma-buf/dma-fence.c | i915 |
| `dma_fence_init64` | v6.17 | vmlinux | drivers/dma-buf/dma-fence.c | amdgpu |
| `dma_fence_timeline_name` | v6.17 | vmlinux | drivers/dma-buf/dma-fence.c | i915 |
| `dma_resv_describe` | v6.16 | vmlinux | drivers/dma-buf/dma-resv.c | amdgpu |
| `down_write_trylock` | v6.18 | vmlinux | kernel/locking/rwsem.c | xe |
| `dummy_irq_chip` | v6.17 | vmlinux | include/linux/irq.h | xe |
| `folio_redirty_for_writepage` | v6.16 | vmlinux | mm/page-writeback.c | i915 |
| `fwnode_create_software_node` | v6.17 | vmlinux | drivers/base/swnode.c | xe |
| `fwnode_device_is_available` | v6.17 | vmlinux | drivers/base/property.c | drm |
| `fwnode_find_reference` | v6.17 | vmlinux | drivers/base/property.c | drm |
| `fwnode_remove_software_node` | v6.17 | vmlinux | drivers/base/swnode.c | xe |
| `generic_handle_irq_safe` | v6.16 | vmlinux | kernel/irq/irqdesc.c | i915,xe |
| `hrtimer_cb_get_time` | v6.18 | vmlinux | kernel/time/hrtimer.c | amdgpu,i915,xe |
| `i2c_bus_type` | v6.17 | vmlinux | include/linux/i2c.h | xe |
| `i2c_unregister_device` | v6.17 | vmlinux | drivers/i2c/i2c-core-base.c | xe |
| `i2c_verify_adapter` | v6.17 | vmlinux | drivers/i2c/i2c-core-base.c | xe |
| `int_pow` | v6.17 | vmlinux | lib/math/int_pow.c | i915,xe |
| `intel_gmch_gtt_read_entry` | v6.16 | vmlinux | drivers/char/agp/intel-gtt.c | i915 |
| `intlog10` | v6.17 | vmlinux | lib/math/int_log.c | i915,xe |
| `irq_dispose_mapping` | v6.17 | vmlinux | kernel/irq/irqdomain.c | xe |
| `kernel_write` | v6.17 | vmlinux | fs/read_write.c | i915 |
| `krealloc_node_align_noprof` | v6.18 | vmlinux | mm/slub.c | amdgpu,drm,drm_kms_helper,i915,xe |
| `kvrealloc_node_align_noprof` | v6.18 | vmlinux | mm/slub.c | drm_exec |
| `platform_device_add` | v6.17 | vmlinux | drivers/base/platform.c | xe |
| `platform_device_add_resources` | v6.17 | vmlinux | drivers/base/platform.c | xe |
| `platform_device_alloc` | v6.17 | vmlinux | drivers/base/platform.c | xe |
| `platform_device_put` | v6.17 | vmlinux | drivers/base/platform.c | xe |
| `pm_hibernate_is_recovering` | v6.17 | vmlinux | drivers/base/power/main.c | amdgpu |
| `pm_hibernation_mode_is_suspend` | v6.18 | vmlinux | kernel/power/hibernate.c | amdgpu |
| `refcount_dec_not_one` | v6.16 | vmlinux | lib/refcount.c | drm_shmem_helper |
| `shmem_writeout` | v6.16 | vmlinux | mm/shmem.c | i915,ttm |
| `sysfs_update_group` | v6.16 | vmlinux | fs/sysfs/group.c | amdgpu |
| `system_percpu_wq` | v6.18 | vmlinux | include/linux/workqueue.h | amdgpu,drm,drm_display_helper,drm_kms_helper,gpu-sched,i915,radeon,virtio-gpu,xe |
| `system_state` | v6.18 | vmlinux | include/linux/kernel.h | amdgpu |
| `timer_init_key` | v6.16 | vmlinux | kernel/time/timer.c | amdgpu,drm,drm_kms_helper,gpu-sched,i915,radeon,xe |
| `vcalloc_noprof` | v6.18 | vmlinux | mm/util.c | radeon |
| `video_is_primary_device` | v6.18 | vmlinux | arch/x86/video/video-common.c | drm |
| `vmalloc_array_noprof` | v6.18 | vmlinux | mm/util.c | radeon |
| `writeback_iter` | v6.16 | vmlinux | mm/page-writeback.c | i915 |
