# Interfaces used by wifi/ath11k: v6.17 → v6.18

## Symbol-level summary

| | count |
|---|---|
| interfaces used in v6.17 | 270 |
| interfaces used in v6.18 | 270 |
| likely renames | 0 |
| newly used (excluding renames) | 1 |
| no longer used (excluding renames) | 0 |
| export kind/owner/namespace changed | 0 |
| used in both, own declaration changed | 0 |
| changed types reachable from used interfaces | 74 |

## Likely renames

None.

## Newly used in v6.18

| symbol | kind | exporter | export | defined in | used by |
|---|---|---|---|---|---|
| `system_percpu_wq` | data | vmlinux | plain | include/linux/workqueue.h | amdgpu,drm_display_helper,drm,drm_kms_helper,i915,radeon,gpu-sched,xe,ath11k,brcmfmac,iwlwifi,iwlmld,iwlmvm,rtw89_core |

## No longer used in v6.18

None.

## Interfaces whose own declaration changed

Return/parameter types, variable types, or interfaces that lost their debug info. `[C]` changed, `[D]` deleted.

None.

## Changed types

Each changed type reachable from an interface this group uses, with the number of those interfaces it reaches, fewest first: low counts are targeted changes, high counts are churn reached through hub types (reachability is transitive through pointers, so e.g. `struct device` or `struct module` pull in hundreds).

| type | declared at | change | used interfaces reached |
|---|---|---|---|
| `struct cfg80211_nan_conf` | cfg80211.h:3899:1 | type size changed from 16 to 1216 (in bits); 10 data member insertions | 1 |
| `struct cfg80211_pmsr_request_peer` | cfg80211.h:4236:1 | type size changed from 448 to 512 (in bits); there are data member changes | 1 |
| `struct cfg80211_tid_cfg` | cfg80211.h:867:1 | type size changed from 3200 to 5120 (in bits); there are data member changes | 1 |
| `struct ieee80211_channel_switch` | mac80211.h:1838:1 | type size changed from 448 to 512 (in bits); there are data member changes | 1 |
| `enum skb_drop_reason` | dropreason-core.h:137:1 | 2 enumerator insertions; 1 enumerator change | 2 |
| `struct cfg80211_ap_settings` | cfg80211.h:1486:1 | type size changed from 7552 to 9536 (in bits); there are data member changes | 7 |
| `struct pci_dev` | pci.h:337:1 | 2 data member insertions; there are data member changes | 18 |
| `struct cfg80211_bitrate_mask` | cfg80211.h:838:1 | type size changed from 2880 to 4800 (in bits); there are data member changes | 23 |
| `struct ieee80211_bss_conf` | mac80211.h:764:1 | type size changed from 7104 to 9152 (in bits); there are data member changes | 23 |
| `struct ieee80211_vif` | mac80211.h:2038:1 | type size changed from 9472 to 11520 (in bits); there are data member changes | 23 |
| `struct ieee80211_chanctx_conf` | mac80211.h:263:1 | type size changed from 832 to 1024 (in bits); there are data member changes | 25 |
| `struct ieee80211_conf` | mac80211.h:1803:1 | type size changed from 512 to 576 (in bits); there are data member changes | 28 |
| `struct ieee80211_hw` | mac80211.h:3061:1 | type size changed from 1536 to 1600 (in bits); there are data member changes | 28 |
| `struct wiphy` | cfg80211.h:5851:1 | 2 data member insertions; there are data member changes | 36 |
| `struct wireless_dev` | cfg80211.h:6459:1 | type size changed from 11840 to 12928 (in bits); there are data member changes | 36 |
| `struct cfg80211_chan_def` | cfg80211.h:825:1 | type size changed from 256 to 320 (in bits); 1 data member insertion | 40 |
| `struct bio` | blk_types.h:214:1 | 1 data member deletion; there are data member changes | 80 |
| `struct bio_set` | bio.h:641:1 | there are data member changes | 80 |
| `struct block_device_operations` | blkdev.h:1650:1 | there are data member changes | 80 |
| `struct gendisk` | blkdev.h:143:1 | there are data member changes | 80 |
| `struct kmem_cache` | slab.h:234:1 | type size changed from 5632 to 5696 (in bits); 3 data member insertions; there are data member changes | 80 |
| `struct kmem_cache_cpu` | slub.c:400:1 | type size changed from 256 to 384 (in bits); there are data member changes | 80 |
| `struct kmem_cache_node` | slub.c:441:1 | type size changed from 512 to 576 (in bits); 1 data member insertion | 80 |
| `struct mnt_namespace` | mount.h:10:1 | type size changed from 1536 to 1600 (in bits); 4 data member deletions; 1 data member insertion; there are data member changes | 80 |
| `struct mount` | mount.h:49:1 | 1 data member insertion; there are data member changes | 80 |
| `struct msi_domain_ops` | msi.h:453:1 | type size changed from 704 to 640 (in bits); 1 data member deletion; there are data member changes | 80 |
| `struct netdev_queue_mgmt_ops` | netdev_queues.h:134:1 | type size changed from 320 to 384 (in bits); 1 data member insertion | 80 |
| `struct netpoll_info` | netpoll.h:49:1 | type size changed from 1344 to 1280 (in bits); 1 data member deletion; there are data member changes | 80 |
| `struct per_cpu_nodestat` | mmzone.h:762:1 | type size changed from 384 to 392 (in bits); there are data member changes | 80 |
| `struct perf_buffer` | internal.h:13:1 | there are data member changes | 80 |
| `struct pglist_data` | mmzone.h:1360:1 | there are data member changes | 80 |
| `struct proc_ns_operations` | proc_ns.h:17:1 | type size changed from 512 to 448 (in bits); 1 data member deletion; there are data member changes | 80 |
| `struct rps_dev_flow` | rps.h:31:1 | type size changed from 64 to 96 (in bits); 1 data member insertion | 80 |
| `struct rt6_info` | ip6_fib.h:207:1 | there are data member changes | 80 |
| `struct rtable` | route.h:57:1 | there are data member changes | 80 |
| `struct perf_event` | perf_event.h:764:1 | there are data member changes | 94 |
| `struct pid_namespace` | pid_namespace.h:26:1 | type size changed from 2304 to 2752 (in bits); there are data member changes | 94 |
| `struct trace_iterator` | trace_events.h:96:1 | type size changed from 132736 to 132608 (in bits); there are data member changes | 94 |
| `struct ethtool_ops` | ethtool.h:1097:1 | type size changed from 5184 to 5248 (in bits); 1 data member insertion; there are data member changes | 116 |
| `struct bpf_offloaded_map` | bpf.h:619:1 | type size changed from 2240 to 2560 (in bits); there are data member changes | 123 |
| `struct dst_entry` | dst.h:26:1 | type size hasn't changed | 123 |
| `struct net` | net_namespace.h:61:1 | type size changed from 30208 to 30720 (in bits); there are data member changes | 123 |
| `struct proto` | sock.h:1251:1 | type size changed from 3584 to 3520 (in bits); 1 data member deletion; there are data member changes | 123 |
| `struct sock` | sock.h:352:1 | 1 data member deletion; 1 data member insertion; there are data member changes | 123 |
| `struct timewait_sock_ops` | timewait_sock.h:14:1 | type size changed from 256 to 192 (in bits); 1 data member deletion | 123 |
| `enum bpf_arg_type` | bpf.h:784:1 | 1 enumerator change | 137 |
| `enum bpf_reg_type` | bpf.h:941:1 | 1 enumerator change | 137 |
| `enum bpf_return_type` | bpf.h:843:1 | 1 enumerator change | 137 |
| `struct arch_uprobe` | uprobes.h:25:1 | type size changed from 256 to 320 (in bits); 1 data member insertion | 137 |
| `struct attribute_group` | sysfs.h:99:1 | there are data member changes | 137 |
| `struct bin_attribute` | sysfs.h:304:1 | type size changed from 704 to 576 (in bits); 2 data member deletions; there are data member changes | 137 |
| `struct bpf_map` | bpf.h:290:1 | type size changed from 1920 to 2240 (in bits); 2 data member insertions; there are data member changes | 137 |
| `struct bpf_map_ops` | bpf.h:82:1 | type size changed from 2752 to 2816 (in bits); 1 data member insertion; there are data member changes | 137 |
| `struct bpf_map_owner` | bpf.h:282:1 | type size changed from 256 to 320 (in bits); 1 data member insertion | 137 |
| `struct bpf_prog` | bpf.h:1693:1 | type size changed from 576 to 768 (in bits); there are data member changes | 137 |
| `struct bpf_prog_aux` | bpf.h:1582:1 | type size changed from 10304 to 10368 (in bits); 2 data member insertions; there are data member changes | 137 |
| `struct btf_record` | bpf.h:254:1 | 1 data member insertion | 137 |
| `struct cgroup` | cgroup-defs.h:438:1 | there are data member changes | 137 |
| `struct cgroup_namespace` | cgroup.h:786:1 | type size changed from 384 to 832 (in bits); there are data member changes | 137 |
| `struct cgroup_root` | cgroup-defs.h:603:1 | there are data member changes | 137 |
| `struct cgroup_subsys` | cgroup-defs.h:732:1 | type size changed from 2112 to 2048 (in bits); 1 data member deletion; there are data member changes | 137 |
| `struct dentry` | dcache.h:92:1 | type size hasn't changed | 137 |
| `struct file` | fs.h:1099:1 | type size hasn't changed | 137 |
| `struct hrtimer_clock_base` | hrtimer_defs.h:47:1 | 1 data member deletion; there are data member changes | 137 |
| `struct inode` | fs.h:675:1 | there are data member changes | 137 |
| `struct mm_struct` | mm_types.h:937:1 | type size hasn't changed | 137 |
| `struct page` | mm_types.h:73:1 | there are data member changes | 137 |
| `struct signal_struct` | signal.h:94:1 | type size changed from 8768 to 9088 (in bits); 1 data member insertion; there are data member changes | 137 |
| `struct super_block` | fs.h:1328:1 | type size changed from 10752 to 10240 (in bits); there are data member changes | 137 |
| `struct uprobes_state` | uprobes.h:186:1 | type size changed from 64 to 128 (in bits); 1 data member insertion | 137 |
| `struct user_namespace` | user_namespace.h:76:1 | type size changed from 4736 to 5184 (in bits); there are data member changes | 137 |
| `struct vm_area_desc` | mm_types.h:786:1 | type size changed from 576 to 640 (in bits); 1 data member insertion; there are data member changes | 137 |
| `struct vm_operations_struct` | mm.h:586:1 | type size changed from 1024 to 960 (in bits); 1 data member deletion | 137 |
| `union bpf_attr` | bpf.h:1484:1 | type size changed from 1216 to 1344 (in bits); 1 data member deletion; 1 data member insertion; there are data member changes | 137 |

### Details

<details><summary><code>struct cfg80211_nan_conf</code> (cfg80211.h:3899:1)</summary>

```
  type size changed from 16 to 1216 (in bits)
  10 data member insertions:
    'const u8* cluster_id', at offset 64 (in bits) at cfg80211.h:3987:1
    'u16 scan_period', at offset 128 (in bits) at cfg80211.h:3988:1
    'u16 scan_dwell_time', at offset 144 (in bits) at cfg80211.h:3989:1
    'u8 discovery_beacon_interval', at offset 160 (in bits) at cfg80211.h:3990:1
    'bool enable_dw_notification', at offset 168 (in bits) at cfg80211.h:3991:1
    'cfg80211_nan_band_config band_cfgs[6]', at offset 192 (in bits) at cfg80211.h:3992:1
    'const u8* extra_nan_attrs', at offset 960 (in bits) at cfg80211.h:3993:1
    'u16 extra_nan_attrs_len', at offset 1024 (in bits) at cfg80211.h:3994:1
    'const u8* vendor_elems', at offset 1088 (in bits) at cfg80211.h:3995:1
    'u16 vendor_elems_len', at offset 1152 (in bits) at cfg80211.h:3996:1
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`

</details>

<details><summary><code>struct cfg80211_pmsr_request_peer</code> (cfg80211.h:4236:1)</summary>

```
  type size changed from 448 to 512 (in bits)
  there are data member changes:
    type 'struct cfg80211_chan_def' of 'cfg80211_pmsr_request_peer::chandef' changed, as reported earlier
    'u8 report_ap_tsf' offset changed from 320 to 384 (in bits) (by +64 bits)
    'cfg80211_pmsr_ftm_request_peer ftm' offset changed from 352 to 416 (in bits) (by +64 bits)
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`

</details>

<details><summary><code>struct cfg80211_tid_cfg</code> (cfg80211.h:867:1)</summary>

```
  type size changed from 3200 to 5120 (in bits)
  there are data member changes:
    type 'struct cfg80211_bitrate_mask' of 'cfg80211_tid_cfg::txrate_mask' changed, as reported earlier
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`

</details>

<details><summary><code>struct ieee80211_channel_switch</code> (mac80211.h:1838:1)</summary>

```
  type size changed from 448 to 512 (in bits)
  there are data member changes:
    type 'struct cfg80211_chan_def' of 'ieee80211_channel_switch::chandef' changed, as reported earlier
    'u8 count' offset changed from 384 to 448 (in bits) (by +64 bits)
    'u8 link_id' offset changed from 392 to 456 (in bits) (by +64 bits)
    'u32 delay' offset changed from 416 to 480 (in bits) (by +64 bits)
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`

</details>

<details><summary><code>enum skb_drop_reason</code> (dropreason-core.h:137:1)</summary>

```
  type size hasn't changed
  2 enumerator insertions:
    'skb_drop_reason::SKB_DROP_REASON_PSP_INPUT' value '125'
    'skb_drop_reason::SKB_DROP_REASON_PSP_OUTPUT' value '126'
  1 enumerator change:
    'skb_drop_reason::SKB_DROP_REASON_MAX' from value '125' to '127' at dropreason-core.h:139:1
```

Reaches: `function void dev_kfree_skb_any_reason(sk_buff*, skb_drop_reason)`, `function void sk_skb_reason_drop(sock*, sk_buff*, skb_drop_reason)`

</details>

<details><summary><code>struct cfg80211_ap_settings</code> (cfg80211.h:1486:1)</summary>

```
  type size changed from 7552 to 9536 (in bits)
  there are data member changes:
    type 'struct cfg80211_chan_def' of 'cfg80211_ap_settings::chandef' changed:
      type size changed from 256 to 320 (in bits)
      1 data member insertion:
        'bool s1g_primary_2mhz', at offset 256 (in bits) at cfg80211.h:833:1
    'cfg80211_beacon_data beacon' offset changed from 256 to 320 (in bits) (by +64 bits)
    'int beacon_interval' offset changed from 1600 to 1664 (in bits) (by +64 bits)
    'int dtim_period' offset changed from 1632 to 1696 (in bits) (by +64 bits)
    'const u8* ssid' offset changed from 1664 to 1728 (in bits) (by +64 bits)
    'size_t ssid_len' offset changed from 1728 to 1792 (in bits) (by +64 bits)
    'nl80211_hidden_ssid hidden_ssid' offset changed from 1792 to 1856 (in bits) (by +64 bits)
    'cfg80211_crypto_settings crypto' offset changed from 1856 to 1920 (in bits) (by +64 bits)
    'bool privacy' offset changed from 2752 to 2816 (in bits) (by +64 bits)
    'nl80211_auth_type auth_type' offset changed from 2784 to 2848 (in bits) (by +64 bits)
    'int inactivity_timeout' offset changed from 2816 to 2880 (in bits) (by +64 bits)
    'u8 p2p_ctwindow' offset changed from 2848 to 2912 (in bits) (by +64 bits)
    'bool p2p_opp_ps' offset changed from 2856 to 2920 (in bits) (by +64 bits)
    'const cfg80211_acl_data* acl' offset changed from 2880 to 2944 (in bits) (by +64 bits)
    'bool pbss' offset changed from 2944 to 3008 (in bits) (by +64 bits)
    type 'struct cfg80211_bitrate_mask' of 'cfg80211_ap_settings::beacon_rate' changed:
      type size changed from 2880 to 4800 (in bits)
      there are data member changes:
        '__anonymous_struct__165 control[6]' size changed from 2880 to 4800 (in bits) (by +1920 bits)
    and offset changed from 2976 to 3040 (in bits) (by +64 bits)
    'const ieee80211_ht_cap* ht_cap' offset changed from 5888 to 7872 (in bits) (by +1984 bits)
    'const ieee80211_vht_cap* vht_cap' offset changed from 5952 to 7936 (in bits) (by +1984 bits)
    'const ieee80211_he_cap_elem* he_cap' offset changed from 6016 to 8000 (in bits) (by +1984 bits)
    'const ieee80211_he_operation* he_oper' offset changed from 6080 to 8064 (in bits) (by +1984 bits)
    'const ieee80211_eht_cap_elem* eht_cap' offset changed from 6144 to 8128 (in bits) (by +1984 bits)
    'const ieee80211_eht_operation* eht_oper' offset changed from 6208 to 8192 (in bits) (by +1984 bits)
    'bool ht_required' offset changed from 6272 to 8256 (in bits) (by +1984 bits)
    'bool vht_required' offset changed from 6280 to 8264 (in bits) (by +1984 bits)
    'bool he_required' offset changed from 6288 to 8272 (in bits) (by +1984 bits)
    'bool sae_h2e_required' offset changed from 6296 to 8280 (in bits) (by +1984 bits)
    'bool twt_responder' offset changed from 6304 to 8288 (in bits) (by +1984 bits)
    'u32 flags' offset changed from 6336 to 8320 (in bits) (by +1984 bits)
    'ieee80211_he_obss_pd he_obss_pd' offset changed from 6368 to 8352 (in bits) (by +1984 bits)
    'cfg80211_fils_discovery fils_discovery' offset changed from 6592 to 8576 (in bits) (by +1984 bits)
    'cfg80211_unsol_bcast_probe_resp unsol_bcast_probe_resp' offset changed from 6848 to 8832 (in bits) (by +1984 bits)
  ...
```

Reaches: `function cfg80211_bss* __cfg80211_get_bss(wiphy*, ieee80211_channel*, const u8*, const u8*, size_t, ieee80211_bss_type, ieee80211_privacy, u32)`, `function unsigned int cfg80211_chandef_dfs_cac_time(wiphy*, const cfg80211_chan_def*)`, `function bool cfg80211_chandef_dfs_usable(wiphy*, const cfg80211_chan_def*)`, `function void cfg80211_put_bss(wiphy*, cfg80211_bss*)`, `function ieee80211_channel* ieee80211_get_channel_khz(wiphy*, u32)`, `function unsigned int ieee80211_get_hdrlen_from_skb(const sk_buff*)`, `function int regulatory_set_wiphy_regd(wiphy*, ieee80211_regdomain*)`

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

Reaches: `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function int pci_alloc_irq_vectors(pci_dev*, unsigned int, unsigned int, unsigned int)`, `function int pci_assign_resource(pci_dev*, int)`, `function void pci_disable_device(pci_dev*)`, `function int pci_enable_device(pci_dev*)`, `function void pci_free_irq_vectors(pci_dev*)`, `function void* pci_iomap(pci_dev*, int, unsigned long int)`, `function void pci_iounmap(pci_dev*, void*)`, `function int pci_irq_vector(pci_dev*, unsigned int)`, `function int pci_read_config_dword(const pci_dev*, int, u32*)`, `function int pci_read_config_word(const pci_dev*, int, u16*)`, `function void pci_release_region(pci_dev*, int)`, `function int pci_request_region(pci_dev*, int, const char*)`, `function void pci_set_master(pci_dev*)`, `function void pci_unregister_driver(pci_driver*)` … (+3 more)

</details>

<details><summary><code>struct cfg80211_bitrate_mask</code> (cfg80211.h:838:1)</summary>

```
  type size changed from 2880 to 4800 (in bits)
  there are data member changes:
    '__anonymous_struct__174 control[6]' size changed from 2880 to 4800 (in bits) (by +1920 bits)
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_color_change_finish(ieee80211_vif*, u8)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta(ieee80211_vif*, const u8*)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function sk_buff* ieee80211_get_unsol_bcast_probe_resp_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_gtk_rekey_notify(ieee80211_vif*, const u8*, const u8*, gfp_t)`, `function void ieee80211_handle_wake_tx_queue(ieee80211_hw*, ieee80211_txq*)` … (+8 more)

</details>

<details><summary><code>struct ieee80211_bss_conf</code> (mac80211.h:764:1)</summary>

```
  type size changed from 7104 to 9152 (in bits)
  there are data member changes:
    type 'struct ieee80211_chan_req' of 'ieee80211_bss_conf::chanreq' changed:
      type size changed from 512 to 640 (in bits)
      there are data member changes:
        type 'struct cfg80211_chan_def' of 'ieee80211_chan_req::oper' changed, as reported earlier
        type 'struct cfg80211_chan_def' of 'ieee80211_chan_req::ap' changed, as reported earlier
        and offset changed from 256 to 320 (in bits) (by +64 bits)
    'ieee80211_mu_group_data mu_group' offset changed from 1600 to 1728 (in bits) (by +128 bits)
    'bool qos' offset changed from 1792 to 1920 (in bits) (by +128 bits)
    'bool hidden_ssid' offset changed from 1800 to 1928 (in bits) (by +128 bits)
    'int txpower' offset changed from 1824 to 1952 (in bits) (by +128 bits)
    'nl80211_tx_power_setting txpower_type' offset changed from 1856 to 1984 (in bits) (by +128 bits)
    'ieee80211_p2p_noa_attr p2p_noa_attr' offset changed from 1888 to 2016 (in bits) (by +128 bits)
    'bool allow_p2p_go_ps' offset changed from 2320 to 2448 (in bits) (by +128 bits)
    'u16 max_idle_period' offset changed from 2336 to 2464 (in bits) (by +128 bits)
    'bool protected_keep_alive' offset changed from 2352 to 2480 (in bits) (by +128 bits)
    'bool ftm_responder' offset changed from 2360 to 2488 (in bits) (by +128 bits)
    'ieee80211_ftm_responder_params* ftmr_params' offset changed from 2368 to 2496 (in bits) (by +128 bits)
    'bool nontransmitted' offset changed from 2432 to 2560 (in bits) (by +128 bits)
    'ieee80211_bss_conf* tx_bss_conf' offset changed from 2496 to 2624 (in bits) (by +128 bits)
    'u8 transmitter_bssid[6]' offset changed from 2560 to 2688 (in bits) (by +128 bits)
    'u8 bssid_index' offset changed from 2608 to 2736 (in bits) (by +128 bits)
    'u8 bssid_indicator' offset changed from 2616 to 2744 (in bits) (by +128 bits)
    'bool ema_ap' offset changed from 2624 to 2752 (in bits) (by +128 bits)
    'u8 profile_periodicity' offset changed from 2632 to 2760 (in bits) (by +128 bits)
    'struct {u32 params; u16 nss_set;} he_oper' offset changed from 2656 to 2784 (in bits) (by +128 bits)
    'ieee80211_he_obss_pd he_obss_pd' offset changed from 2720 to 2848 (in bits) (by +128 bits)
    'cfg80211_he_bss_color he_bss_color' offset changed from 2888 to 3016 (in bits) (by +128 bits)
    'ieee80211_fils_discovery fils_discovery' offset changed from 2912 to 3040 (in bits) (by +128 bits)
    'u32 unsol_bcast_probe_resp_interval' offset changed from 2976 to 3104 (in bits) (by +128 bits)
    type 'struct cfg80211_bitrate_mask' of 'ieee80211_bss_conf::beacon_tx_rate' changed, as reported earlier
    and offset changed from 3008 to 3136 (in bits) (by +128 bits)
    'ieee80211_ap_reg_power power_type' offset changed from 5888 to 7936 (in bits) (by +2048 bits)
    'ieee80211_parsed_tpe tpe' offset changed from 5920 to 7968 (in bits) (by +2048 bits)
    'u8 pwr_reduction' offset changed from 6752 to 8800 (in bits) (by +2048 bits)
    'bool eht_support' offset changed from 6760 to 8808 (in bits) (by +2048 bits)
    'bool epcs_support' offset changed from 6768 to 8816 (in bits) (by +2048 bits)
    'bool csa_active' offset changed from 6776 to 8824 (in bits) (by +2048 bits)
    'bool mu_mimo_owner' offset changed from 6784 to 8832 (in bits) (by +2048 bits)
  ...
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_color_change_finish(ieee80211_vif*, u8)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta(ieee80211_vif*, const u8*)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function sk_buff* ieee80211_get_unsol_bcast_probe_resp_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_gtk_rekey_notify(ieee80211_vif*, const u8*, const u8*, gfp_t)`, `function void ieee80211_handle_wake_tx_queue(ieee80211_hw*, ieee80211_txq*)` … (+8 more)

</details>

<details><summary><code>struct ieee80211_vif</code> (mac80211.h:2038:1)</summary>

```
  type size changed from 9472 to 11520 (in bits)
  there are data member changes:
    type 'struct ieee80211_bss_conf' of 'ieee80211_vif::bss_conf' changed, as reported earlier
    'ieee80211_bss_conf* link_conf[15]' offset changed from 7808 to 9856 (in bits) (by +2048 bits)
    'u16 valid_links' offset changed from 8768 to 10816 (in bits) (by +2048 bits)
    'u16 active_links' offset changed from 8784 to 10832 (in bits) (by +2048 bits)
    'u16 dormant_links' offset changed from 8800 to 10848 (in bits) (by +2048 bits)
    'u16 suspended_links' offset changed from 8816 to 10864 (in bits) (by +2048 bits)
    'ieee80211_neg_ttlm neg_ttlm' offset changed from 8832 to 10880 (in bits) (by +2048 bits)
    'u8 addr[6]' offset changed from 9104 to 11152 (in bits) (by +2048 bits)
    'bool addr_valid' offset changed from 9152 to 11200 (in bits) (by +2048 bits)
    'bool p2p' offset changed from 9160 to 11208 (in bits) (by +2048 bits)
    'u8 cab_queue' offset changed from 9168 to 11216 (in bits) (by +2048 bits)
    'u8 hw_queue[4]' offset changed from 9176 to 11224 (in bits) (by +2048 bits)
    'ieee80211_txq* txq' offset changed from 9216 to 11264 (in bits) (by +2048 bits)
    'netdev_features_t netdev_features' offset changed from 9280 to 11328 (in bits) (by +2048 bits)
    'u32 driver_flags' offset changed from 9344 to 11392 (in bits) (by +2048 bits)
    'u32 offload_flags' offset changed from 9376 to 11424 (in bits) (by +2048 bits)
    'bool probe_req_reg' offset changed from 9408 to 11456 (in bits) (by +2048 bits)
    'bool rx_mcast_action_reg' offset changed from 9416 to 11464 (in bits) (by +2048 bits)
    'u8 drv_priv[]' offset changed from 9472 to 11520 (in bits) (by +2048 bits)
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_color_change_finish(ieee80211_vif*, u8)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta(ieee80211_vif*, const u8*)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function sk_buff* ieee80211_get_unsol_bcast_probe_resp_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_gtk_rekey_notify(ieee80211_vif*, const u8*, const u8*, gfp_t)`, `function void ieee80211_handle_wake_tx_queue(ieee80211_hw*, ieee80211_txq*)` … (+8 more)

</details>

<details><summary><code>struct ieee80211_chanctx_conf</code> (mac80211.h:263:1)</summary>

```
  type size changed from 832 to 1024 (in bits)
  there are data member changes:
    type 'struct cfg80211_chan_def' of 'ieee80211_chanctx_conf::def' changed, as reported earlier
    type 'struct cfg80211_chan_def' of 'ieee80211_chanctx_conf::min_def' changed, as reported earlier
    and offset changed from 256 to 320 (in bits) (by +64 bits)
    type 'struct cfg80211_chan_def' of 'ieee80211_chanctx_conf::ap' changed, as reported earlier
    and offset changed from 512 to 640 (in bits) (by +128 bits)
    'int radio_idx' offset changed from 768 to 960 (in bits) (by +192 bits)
    'u8 rx_chains_static' offset changed from 800 to 992 (in bits) (by +192 bits)
    'u8 rx_chains_dynamic' offset changed from 808 to 1000 (in bits) (by +192 bits)
    'bool radar_enabled' offset changed from 816 to 1008 (in bits) (by +192 bits)
    'u8 drv_priv[]' offset changed from 832 to 1024 (in bits) (by +192 bits)
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_color_change_finish(ieee80211_vif*, u8)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta(ieee80211_vif*, const u8*)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function sk_buff* ieee80211_get_unsol_bcast_probe_resp_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_gtk_rekey_notify(ieee80211_vif*, const u8*, const u8*, gfp_t)`, `function void ieee80211_handle_wake_tx_queue(ieee80211_hw*, ieee80211_txq*)` … (+10 more)

</details>

<details><summary><code>struct ieee80211_conf</code> (mac80211.h:1803:1)</summary>

```
  type size changed from 512 to 576 (in bits)
  there are data member changes:
    type 'struct cfg80211_chan_def' of 'ieee80211_conf::chandef' changed, as reported earlier
    'bool radar_enabled' offset changed from 448 to 512 (in bits) (by +64 bits)
    'ieee80211_smps_mode smps_mode' offset changed from 480 to 544 (in bits) (by +64 bits)
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function sk_buff* ieee80211_get_unsol_bcast_probe_resp_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_handle_wake_tx_queue(ieee80211_hw*, ieee80211_txq*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_iterate_stations_mtx(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)` … (+13 more)

</details>

<details><summary><code>struct ieee80211_hw</code> (mac80211.h:3061:1)</summary>

```
  type size changed from 1536 to 1600 (in bits)
  there are data member changes:
    type 'struct ieee80211_conf' of 'ieee80211_hw::conf' changed, as reported earlier
    'wiphy* wiphy' offset changed from 512 to 576 (in bits) (by +64 bits)
    'const char* rate_control_algorithm' offset changed from 576 to 640 (in bits) (by +64 bits)
    'void* priv' offset changed from 640 to 704 (in bits) (by +64 bits)
    'unsigned long int flags[1]' offset changed from 704 to 768 (in bits) (by +64 bits)
    'unsigned int extra_tx_headroom' offset changed from 768 to 832 (in bits) (by +64 bits)
    'unsigned int extra_beacon_tailroom' offset changed from 800 to 864 (in bits) (by +64 bits)
    'int vif_data_size' offset changed from 832 to 896 (in bits) (by +64 bits)
    'int sta_data_size' offset changed from 864 to 928 (in bits) (by +64 bits)
    'int chanctx_data_size' offset changed from 896 to 960 (in bits) (by +64 bits)
    'int txq_data_size' offset changed from 928 to 992 (in bits) (by +64 bits)
    'u16 queues' offset changed from 960 to 1024 (in bits) (by +64 bits)
    'u16 max_listen_interval' offset changed from 976 to 1040 (in bits) (by +64 bits)
    's8 max_signal' offset changed from 992 to 1056 (in bits) (by +64 bits)
    'u8 max_rates' offset changed from 1000 to 1064 (in bits) (by +64 bits)
    'u8 max_report_rates' offset changed from 1008 to 1072 (in bits) (by +64 bits)
    'u8 max_rate_tries' offset changed from 1016 to 1080 (in bits) (by +64 bits)
    'u16 max_rx_aggregation_subframes' offset changed from 1024 to 1088 (in bits) (by +64 bits)
    'u16 max_tx_aggregation_subframes' offset changed from 1040 to 1104 (in bits) (by +64 bits)
    'u8 max_tx_fragments' offset changed from 1056 to 1120 (in bits) (by +64 bits)
    'u8 offchannel_tx_hw_queue' offset changed from 1064 to 1128 (in bits) (by +64 bits)
    'u8 radiotap_mcs_details' offset changed from 1072 to 1136 (in bits) (by +64 bits)
    'u16 radiotap_vht_details' offset changed from 1088 to 1152 (in bits) (by +64 bits)
    'struct {int units_pos; s16 accuracy;} radiotap_timestamp' offset changed from 1120 to 1184 (in bits) (by +64 bits)
    'netdev_features_t netdev_features' offset changed from 1216 to 1280 (in bits) (by +64 bits)
    'u8 uapsd_queues' offset changed from 1280 to 1344 (in bits) (by +64 bits)
    'u8 uapsd_max_sp_len' offset changed from 1288 to 1352 (in bits) (by +64 bits)
    'u8 max_nan_de_entries' offset changed from 1296 to 1360 (in bits) (by +64 bits)
    'u8 tx_sk_pacing_shift' offset changed from 1304 to 1368 (in bits) (by +64 bits)
    'u8 weight_multiplier' offset changed from 1312 to 1376 (in bits) (by +64 bits)
    'u32 max_mtu' offset changed from 1344 to 1408 (in bits) (by +64 bits)
    'const s8* tx_power_levels' offset changed from 1408 to 1472 (in bits) (by +64 bits)
    'u8 max_txpwr_levels_idx' offset changed from 1472 to 1536 (in bits) (by +64 bits)
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function sk_buff* ieee80211_get_unsol_bcast_probe_resp_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_handle_wake_tx_queue(ieee80211_hw*, ieee80211_txq*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_iterate_stations_mtx(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)`, `function void ieee80211_queue_work(ieee80211_hw*, work_struct*)` … (+13 more)

</details>

<details><summary><code>struct wiphy</code> (cfg80211.h:5851:1)</summary>

```
  type size hasn't changed
  2 data member insertions:
    'u32 bss_param_support', at offset 9632 (in bits) at cfg80211.h:6114:1
    'wiphy_nan_capa nan_capa', at offset 9728 (in bits) at cfg80211.h:6118:1
  there are data member changes:
    'u32 bss_select_support' offset changed from 9632 to 9664 (in bits) (by +32 bits)
    'u8 nan_supported_bands' offset changed from 9664 to 9696 (in bits) (by +32 bits)
    'u32 txq_limit' offset changed from 9696 to 9824 (in bits) (by +128 bits)
    'u32 txq_memory_limit' offset changed from 9728 to 9856 (in bits) (by +128 bits)
    'u32 txq_quantum' offset changed from 9760 to 9888 (in bits) (by +128 bits)
    'unsigned long int tx_queue_len' offset changed from 9792 to 9920 (in bits) (by +128 bits)
    'u8 support_mbssid' offset changed from 9856 to 9984 (in bits) (by +128 bits)
    'u8 support_only_he_mbssid' offset changed from 9857 to 9985 (in bits) (by +128 bits)
    'const cfg80211_pmsr_capabilities* pmsr_capa' offset changed from 9920 to 10048 (in bits) (by +128 bits)
    'struct {u64 peer; u64 vif; u8 max_retry;} tid_config_support' offset changed from 9984 to 10112 (in bits) (by +128 bits)
    'u8 max_data_retry_count' offset changed from 10176 to 10304 (in bits) (by +128 bits)
    'const cfg80211_sar_capa* sar_capa' offset changed from 10240 to 10368 (in bits) (by +128 bits)
    'rfkill* rfkill' offset changed from 10304 to 10432 (in bits) (by +128 bits)
    'u8 mbssid_max_interfaces' offset changed from 10368 to 10496 (in bits) (by +128 bits)
    'u8 ema_max_profile_periodicity' offset changed from 10376 to 10504 (in bits) (by +128 bits)
    'u16 max_num_akm_suites' offset changed from 10384 to 10512 (in bits) (by +128 bits)
    'u16 hw_timestamp_max_peers' offset changed from 10400 to 10528 (in bits) (by +128 bits)
    'int n_radio' offset changed from 10432 to 10560 (in bits) (by +128 bits)
    'const wiphy_radio* radio' offset changed from 10496 to 10624 (in bits) (by +128 bits)
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function sk_buff* ieee80211_get_unsol_bcast_probe_resp_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_handle_wake_tx_queue(ieee80211_hw*, ieee80211_txq*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_iterate_stations_mtx(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)` … (+21 more)

</details>

<details><summary><code>struct wireless_dev</code> (cfg80211.h:6459:1)</summary>

```
  type size changed from 11840 to 12928 (in bits)
  there are data member changes:
    type 'union {struct {u8 connected_addr[6]; u8 ssid[32]; u8 ssid_len;} client; struct {int beacon_interval; cfg80211_chan_def preset_chandef; cfg80211_chan_def chandef; u8 id[32]; u8 id_len; u8 id_up_len;} mesh; struct {cfg80211_chan_def preset_chandef; u8 ssid[32]; u8 ssid_len;} ap; struct {cfg80211_internal_bss* current_bss; cfg80211_chan_def chandef; int beacon_interval; u8 ssid[32]; u8 ssid_len;} ibss; struct {cfg80211_chan_def chandef;} ocb;}' of 'wireless_dev::u' changed:
      type size changed from 896 to 1024 (in bits)
      1 data member insertion:
        'struct {u8 cluster_id[6];} nan' at cfg80211.h:6777:1
      there are data member changes:
        type 'struct {cfg80211_chan_def preset_chandef; u8 ssid[32]; u8 ssid_len;}' of '__anonymous_union__111::ap' changed:
          type size changed from 576 to 640 (in bits)
          there are data member changes:
            type 'struct cfg80211_chan_def' of '__anonymous_struct__122::preset_chandef' changed, as reported earlier
            'u8 ssid[32]' offset changed from 256 to 320 (in bits) (by +64 bits)
            'u8 ssid_len' offset changed from 512 to 576 (in bits) (by +64 bits)
        type 'struct {cfg80211_internal_bss* current_bss; cfg80211_chan_def chandef; int beacon_interval; u8 ssid[32]; u8 ssid_len;}' of '__anonymous_union__111::ibss' changed:
          type size changed from 640 to 704 (in bits)
          there are data member changes:
            type 'struct cfg80211_chan_def' of '__anonymous_struct__123::chandef' changed, as reported earlier
            'int beacon_interval' offset changed from 320 to 384 (in bits) (by +64 bits)
            'u8 ssid[32]' offset changed from 352 to 416 (in bits) (by +64 bits)
            'u8 ssid_len' offset changed from 608 to 672 (in bits) (by +64 bits)
        type 'struct {int beacon_interval; cfg80211_chan_def preset_chandef; cfg80211_chan_def chandef; u8 id[32]; u8 id_len; u8 id_up_len;}' of '__anonymous_union__111::mesh' changed:
          type size changed from 896 to 1024 (in bits)
          there are data member changes:
            type 'struct cfg80211_chan_def' of '__anonymous_struct__121::preset_chandef' changed, as reported earlier
            type 'struct cfg80211_chan_def' of '__anonymous_struct__121::chandef' changed, as reported earlier
            and offset changed from 320 to 384 (in bits) (by +64 bits)
            'u8 id[32]' offset changed from 576 to 704 (in bits) (by +128 bits)
            'u8 id_len' offset changed from 832 to 960 (in bits) (by +128 bits)
            'u8 id_up_len' offset changed from 840 to 968 (in bits) (by +128 bits)
        type 'struct {cfg80211_chan_def chandef;}' of '__anonymous_union__111::ocb' changed:
          type size changed from 256 to 320 (in bits)
          there are data member changes:
            type 'struct cfg80211_chan_def' of '__anonymous_struct__124::chandef' changed, as reported earlier
    '__anonymous_struct__125 links[15]' offset changed from 3136 to 3264 (in bits) (by +128 bits), size changed from 8640 to 9600 (in bits) (by +960 bits)
    'u16 valid_links' offset changed from 11776 to 12864 (in bits) (by +1088 bits)
    'u32 radio_mask' offset changed from 11808 to 12896 (in bits) (by +1088 bits)
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function sk_buff* ieee80211_get_unsol_bcast_probe_resp_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_handle_wake_tx_queue(ieee80211_hw*, ieee80211_txq*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_iterate_stations_mtx(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)` … (+21 more)

</details>

<details><summary><code>struct cfg80211_chan_def</code> (cfg80211.h:825:1)</summary>

```
  type size changed from 256 to 320 (in bits)
  1 data member insertion:
    'bool s1g_primary_2mhz', at offset 256 (in bits) at cfg80211.h:833:1
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function bool ieee80211_beacon_cntdwn_is_complete(ieee80211_vif*, unsigned int)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function void ieee80211_beacon_loss(ieee80211_vif*)`, `function u8 ieee80211_beacon_update_cntdwn(ieee80211_vif*, unsigned int)`, `function void ieee80211_color_change_finish(ieee80211_vif*, u8)`, `function void ieee80211_connection_loss(ieee80211_vif*)`, `function void ieee80211_csa_finish(ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta(ieee80211_vif*, const u8*)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)` … (+25 more)

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

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

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

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

</details>

<details><summary><code>struct block_device_operations</code> (blkdev.h:1650:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'int (block_device*, hd_geometry*)*' of 'block_device_operations::getgeo' changed:
      pointer type changed from: 'int (block_device*, hd_geometry*)*' to: 'int (gendisk*, hd_geometry*)*'
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

</details>

<details><summary><code>struct gendisk</code> (blkdev.h:143:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct bio_set' of 'gendisk::bio_split' changed, as reported earlier
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

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

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

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

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

</details>

<details><summary><code>struct kmem_cache_node</code> (slub.c:441:1)</summary>

```
  type size changed from 512 to 576 (in bits)
  1 data member insertion:
    'node_barn* barn', at offset 512 (in bits) at slub.c:499:1
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

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

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

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

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

</details>

<details><summary><code>struct msi_domain_ops</code> (msi.h:453:1)</summary>

```
  type size changed from 704 to 640 (in bits)
  1 data member deletion:
    'void (irq_domain*, device*)* msi_post_free', at offset 576 (in bits) at msi.h:476:1
  there are data member changes:
    'int (irq_domain*, irq_fwspec*, irq_hw_number_t*, unsigned int*)* msi_translate' offset changed from 640 to 576 (in bits) (by -64 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

</details>

<details><summary><code>struct netdev_queue_mgmt_ops</code> (netdev_queues.h:134:1)</summary>

```
  type size changed from 320 to 384 (in bits)
  1 data member insertion:
    'device* (net_device*, int)* ndo_queue_get_dma_dev', at offset 320 (in bits) at netdev_queues.h:150:1
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

</details>

<details><summary><code>struct netpoll_info</code> (netpoll.h:49:1)</summary>

```
  type size changed from 1344 to 1280 (in bits)
  1 data member deletion:
    'netpoll* netpoll', at offset 1152 (in bits) at netpoll.h:58:1
  there are data member changes:
    'callback_head rcu' offset changed from 1216 to 1152 (in bits) (by -64 bits)
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

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

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

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

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

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

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

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

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

</details>

<details><summary><code>struct rps_dev_flow</code> (rps.h:31:1)</summary>

```
  type size changed from 64 to 96 (in bits)
  1 data member insertion:
    'u32 hash', at offset 64 (in bits) at rps.h:36:1
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

</details>

<details><summary><code>struct rt6_info</code> (ip6_fib.h:207:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct dst_entry' of 'rt6_info::dst' changed, as reported earlier
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

</details>

<details><summary><code>struct rtable</code> (route.h:57:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct dst_entry' of 'rtable::dst' changed, as reported earlier
```

Reaches: `const kernel_param_ops param_ops_bool`, `const kernel_param_ops param_ops_uint`, `function void __dma_sync_single_for_cpu(device*, dma_addr_t, size_t, dma_data_direction)`, `function void __dma_sync_single_for_device(device*, dma_addr_t, size_t, dma_data_direction)`, `function void* __kmalloc_cache_noprof(kmem_cache*, gfp_t, size_t)`, `function void __napi_schedule(napi_struct*)`, `function sk_buff* __netdev_alloc_skb(net_device*, unsigned int, gfp_t)`, `function void __netif_napi_del_locked(napi_struct*)`, `function int __pci_register_driver(pci_driver*, module*, const char*)`, `function void __skb_get_hash_net(const net*, sk_buff*)`, `function void _dev_err(const device*, const char*, ...)`, `function void _dev_info(const device*, const char*, ...)`, `function void _dev_warn(const device*, const char*, ...)`, `function net_device* alloc_netdev_dummy(int)`, `function workqueue_struct* alloc_workqueue_noprof(const char*, unsigned int, int, ...)` … (+65 more)

</details>

<details><summary><code>struct perf_event</code> (perf_event.h:764:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'typedef atomic_t' of 'perf_event::mmap_count' changed:
      typedef name changed from atomic_t to refcount_t at refcount_types.h:17:1
      underlying type 'struct atomic_t' at types.h:181:1 changed:
        type name changed from 'atomic_t' to 'refcount_struct'
        type size hasn't changed
        there are data member changes:
          type 'int' of 'atomic_t::counter' changed:
            entity changed from 'int' to 'typedef atomic_t' at types.h:183:1
            type size hasn't changed
          and name of 'atomic_t::counter' changed to 'refcount_struct::refs' at refcount_types.h:16:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `const kernel_param_ops param_ops_bool` … (+79 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `const kernel_param_ops param_ops_bool` … (+79 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `const kernel_param_ops param_ops_bool` … (+79 more)

</details>

<details><summary><code>struct ethtool_ops</code> (ethtool.h:1097:1)</summary>

```
  type size changed from 5184 to 5248 (in bits)
  1 data member insertion:
    'typedef u32 (net_device*)* get_rx_ring_count', at offset 2432 (in bits) at ethtool.h:1188:1
  there are data member changes:
    'typedef u32 (net_device*)* get_rxfh_key_size' offset changed from 2432 to 2496 (in bits) (by +64 bits)
    'typedef u32 (net_device*)* get_rxfh_indir_size' offset changed from 2496 to 2560 (in bits) (by +64 bits)
    'int (net_device*, ethtool_rxfh_param*)* get_rxfh' offset changed from 2560 to 2624 (in bits) (by +64 bits)
    'int (net_device*, ethtool_rxfh_param*, netlink_ext_ack*)* set_rxfh' offset changed from 2624 to 2688 (in bits) (by +64 bits)
    'int (net_device*, ethtool_rxfh_fields*)* get_rxfh_fields' offset changed from 2688 to 2752 (in bits) (by +64 bits)
    'int (net_device*, const ethtool_rxfh_fields*, netlink_ext_ack*)* set_rxfh_fields' offset changed from 2752 to 2816 (in bits) (by +64 bits)
    'int (net_device*, ethtool_rxfh_context*, const ethtool_rxfh_param*, netlink_ext_ack*)* create_rxfh_context' offset changed from 2816 to 2880 (in bits) (by +64 bits)
    'int (net_device*, ethtool_rxfh_context*, const ethtool_rxfh_param*, netlink_ext_ack*)* modify_rxfh_context' offset changed from 2880 to 2944 (in bits) (by +64 bits)
    'int (net_device*, ethtool_rxfh_context*, typedef u32, netlink_ext_ack*)* remove_rxfh_context' offset changed from 2944 to 3008 (in bits) (by +64 bits)
    'void (net_device*, ethtool_channels*)* get_channels' offset changed from 3008 to 3072 (in bits) (by +64 bits)
    'int (net_device*, ethtool_channels*)* set_channels' offset changed from 3072 to 3136 (in bits) (by +64 bits)
    'int (net_device*, ethtool_dump*)* get_dump_flag' offset changed from 3136 to 3200 (in bits) (by +64 bits)
    'int (net_device*, ethtool_dump*, void*)* get_dump_data' offset changed from 3200 to 3264 (in bits) (by +64 bits)
    'int (net_device*, ethtool_dump*)* set_dump' offset changed from 3264 to 3328 (in bits) (by +64 bits)
    'int (net_device*, kernel_ethtool_ts_info*)* get_ts_info' offset changed from 3328 to 3392 (in bits) (by +64 bits)
    'void (net_device*, ethtool_ts_stats*)* get_ts_stats' offset changed from 3392 to 3456 (in bits) (by +64 bits)
    'int (net_device*, ethtool_modinfo*)* get_module_info' offset changed from 3456 to 3520 (in bits) (by +64 bits)
    'int (net_device*, ethtool_eeprom*, u8*)* get_module_eeprom' offset changed from 3520 to 3584 (in bits) (by +64 bits)
    'int (net_device*, ethtool_keee*)* get_eee' offset changed from 3584 to 3648 (in bits) (by +64 bits)
    'int (net_device*, ethtool_keee*)* set_eee' offset changed from 3648 to 3712 (in bits) (by +64 bits)
    'int (net_device*, const ethtool_tunable*, void*)* get_tunable' offset changed from 3712 to 3776 (in bits) (by +64 bits)
    'int (net_device*, const ethtool_tunable*, void*)* set_tunable' offset changed from 3776 to 3840 (in bits) (by +64 bits)
    'int (net_device*, typedef u32, ethtool_coalesce*)* get_per_queue_coalesce' offset changed from 3840 to 3904 (in bits) (by +64 bits)
    'int (net_device*, typedef u32, ethtool_coalesce*)* set_per_queue_coalesce' offset changed from 3904 to 3968 (in bits) (by +64 bits)
    'int (net_device*, ethtool_link_ksettings*)* get_link_ksettings' offset changed from 3968 to 4032 (in bits) (by +64 bits)
    'int (net_device*, const ethtool_link_ksettings*)* set_link_ksettings' offset changed from 4032 to 4096 (in bits) (by +64 bits)
    type 'void (net_device*, ethtool_fec_stats*)*' of 'ethtool_ops::get_fec_stats' changed:
      pointer type changed from: 'void (net_device*, ethtool_fec_stats*)*' to: 'void (net_device*, ethtool_fec_stats*, ethtool_fec_hist*)*'
    and offset changed from 4096 to 4160 (in bits) (by +64 bits)
    'int (net_device*, ethtool_fecparam*)* get_fecparam' offset changed from 4160 to 4224 (in bits) (by +64 bits)
    'int (net_device*, ethtool_fecparam*)* set_fecparam' offset changed from 4224 to 4288 (in bits) (by +64 bits)
    'void (net_device*, ethtool_stats*, u64*)* get_ethtool_phy_stats' offset changed from 4288 to 4352 (in bits) (by +64 bits)
    'int (net_device*, const ethtool_tunable*, void*)* get_phy_tunable' offset changed from 4352 to 4416 (in bits) (by +64 bits)
    'int (net_device*, const ethtool_tunable*, void*)* set_phy_tunable' offset changed from 4416 to 4480 (in bits) (by +64 bits)
    'int (net_device*, const ethtool_module_eeprom*, netlink_ext_ack*)* get_module_eeprom_by_page' offset changed from 4480 to 4544 (in bits) (by +64 bits)
    'int (net_device*, const ethtool_module_eeprom*, netlink_ext_ack*)* set_module_eeprom_by_page' offset changed from 4544 to 4608 (in bits) (by +64 bits)
  ...
```

Reaches: `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function sk_buff* ieee80211_get_unsol_bcast_probe_resp_tmpl(ieee80211_hw*, ieee80211_vif*)`, `function void ieee80211_handle_wake_tx_queue(ieee80211_hw*, ieee80211_txq*)`, `function void ieee80211_iter_chan_contexts_atomic(ieee80211_hw*, void (ieee80211_hw*, ieee80211_chanctx_conf*, void*)*, void*)`, `function void ieee80211_iterate_active_interfaces_atomic(ieee80211_hw*, u32, void (void*, u8*, ieee80211_vif*)*, void*)`, `function void ieee80211_iterate_stations_atomic(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_iterate_stations_mtx(ieee80211_hw*, void (void*, ieee80211_sta*)*, void*)`, `function void ieee80211_queue_delayed_work(ieee80211_hw*, delayed_work*, unsigned long int)` … (+101 more)

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

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)` … (+108 more)

</details>

<details><summary><code>struct dst_entry</code> (dst.h:26:1)</summary>

```
  type size hasn't changed
```

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)` … (+108 more)

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

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)` … (+108 more)

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

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)` … (+108 more)

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

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)` … (+108 more)

</details>

<details><summary><code>struct timewait_sock_ops</code> (timewait_sock.h:14:1)</summary>

```
  type size changed from 256 to 192 (in bits)
  1 data member deletion:
    'void (sock*)* twsk_destructor', at offset 192 (in bits) at timewait_sock.h:18:1
```

Reaches: `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)`, `function int qmi_handle_init(qmi_handle*, size_t, const qmi_ops*, const qmi_msg_handler*)`, `function void qmi_handle_release(qmi_handle*)`, `function ssize_t qmi_send_request(qmi_handle*, sockaddr_qrtr*, qmi_txn*, int, size_t, const qmi_elem_info*, void*)`, `function void qmi_txn_cancel(qmi_txn*)`, `function int qmi_txn_init(qmi_handle*, qmi_txn*, const qmi_elem_info*, void*)`, `function int qmi_txn_wait(qmi_txn*, unsigned long int)`, `function ieee80211_hw* ieee80211_alloc_hw_nm(size_t, const ieee80211_ops*, const char*)`, `function void ieee80211_beacon_free_ema_list(ieee80211_ema_beacons*)`, `function sk_buff* ieee80211_beacon_get_template(ieee80211_hw*, ieee80211_vif*, ieee80211_mutable_offsets*, unsigned int)`, `function ieee80211_ema_beacons* ieee80211_beacon_get_template_ema_list(ieee80211_hw*, ieee80211_vif*, unsigned int)`, `function ieee80211_sta* ieee80211_find_sta_by_ifaddr(ieee80211_hw*, const u8*, const u8*)`, `function void ieee80211_free_hw(ieee80211_hw*)`, `function void ieee80211_free_txskb(ieee80211_hw*, sk_buff*)`, `function sk_buff* ieee80211_get_fils_discovery_tmpl(ieee80211_hw*, ieee80211_vif*)` … (+108 more)

</details>

<details><summary><code>enum bpf_arg_type</code> (bpf.h:784:1)</summary>

```
  type size hasn't changed
  1 enumerator change:
    'bpf_arg_type::__BPF_ARG_TYPE_LIMIT' from value '134217727' to '268435455' at bpf.h:802:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>enum bpf_reg_type</code> (bpf.h:941:1)</summary>

```
  type size hasn't changed
  1 enumerator change:
    'bpf_reg_type::__BPF_REG_TYPE_LIMIT' from value '134217727' to '268435455' at bpf.h:959:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>enum bpf_return_type</code> (bpf.h:843:1)</summary>

```
  type size hasn't changed
  1 enumerator change:
    'bpf_return_type::__BPF_RET_TYPE_LIMIT' from value '134217727' to '268435455' at bpf.h:861:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct arch_uprobe</code> (uprobes.h:25:1)</summary>

```
  type size changed from 256 to 320 (in bits)
  1 data member insertion:
    'unsigned long int flags', at offset 256 (in bits) at uprobes.h:54:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct attribute_group</code> (sysfs.h:99:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    anonymous data member union {const bin_attribute* const* bin_attrs; const bin_attribute* const* bin_attrs_new;} at offset 320 (in bits) became data member 'const bin_attribute* const* bin_attrs'
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct bpf_map_owner</code> (bpf.h:282:1)</summary>

```
  type size changed from 256 to 320 (in bits)
  1 data member insertion:
    'bpf_attach_type expected_attach_type', at offset 256 (in bits) at bpf.h:292:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct btf_record</code> (bpf.h:254:1)</summary>

```
  type size hasn't changed
  1 data member insertion:
    'int task_work_off', at offset 224 (in bits) at bpf.h:265:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct cgroup_root</code> (cgroup-defs.h:603:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'struct cgroup' of 'cgroup_root::cgrp' changed, as reported earlier
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct dentry</code> (dcache.h:92:1)</summary>

```
  type size hasn't changed
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct file</code> (fs.h:1099:1)</summary>

```
  type size hasn't changed
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct hrtimer_clock_base</code> (hrtimer_defs.h:47:1)</summary>

```
  type size hasn't changed
  1 data member deletion:
    'typedef ktime_t ()* get_time', at offset 384 (in bits) at hrtimer_defs.h:54:1
  there are data member changes:
    'ktime_t offset' offset changed from 448 to 384 (in bits) (by -64 bits)
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct inode</code> (fs.h:675:1)</summary>

```
  type size hasn't changed
  there are data member changes:
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct mm_struct</code> (mm_types.h:937:1)</summary>

```
  type size hasn't changed
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct page</code> (mm_types.h:73:1)</summary>

```
  type size hasn't changed
  there are data member changes:
    type 'unsigned long int' of 'page::flags' changed:
      entity changed from 'unsigned long int' to 'typedef memdesc_flags_t' at mm_types.h:39:1
      type size hasn't changed
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct uprobes_state</code> (uprobes.h:186:1)</summary>

```
  type size changed from 64 to 128 (in bits)
  1 data member insertion:
    'hlist_head head_tramps', at offset 64 (in bits) at uprobes.h:190:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

<details><summary><code>struct vm_operations_struct</code> (mm.h:586:1)</summary>

```
  type size changed from 1024 to 960 (in bits)
  1 data member deletion:
    'page* (vm_area_struct*, unsigned long int)* find_special_page', at offset 960 (in bits) at mm.h:656:1
```

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

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

Reaches: `function mhi_controller* mhi_alloc_controller()`, `function int mhi_device_get_sync(mhi_device*)`, `function void mhi_device_put(mhi_device*)`, `function int mhi_download_rddm_image(mhi_controller*, bool)`, `function void mhi_free_controller(mhi_controller*)`, `function int mhi_pm_resume_force(mhi_controller*)`, `function int mhi_pm_suspend(mhi_controller*)`, `function void mhi_power_down(mhi_controller*, bool)`, `function void mhi_power_down_keep_dev(mhi_controller*, bool)`, `function int mhi_prepare_for_power_up(mhi_controller*)`, `function int mhi_register_controller(mhi_controller*, const mhi_controller_config*)`, `function int mhi_sync_power_up(mhi_controller*)`, `function void mhi_unprepare_after_power_down(mhi_controller*)`, `function void mhi_unregister_controller(mhi_controller*)`, `function int qmi_add_lookup(qmi_handle*, unsigned int, unsigned int, unsigned int)` … (+122 more)

</details>

## Header-level interfaces

Macros, static inline functions, struct/union/enum tags, typedefs and enumerators defined in provider headers (headers the consumer objects were compiled against that are not consumer code) and named in consumer code. They never appear as ELF symbols, but LinuxKPI has to provide them. Name-based, so an occasional false positive is possible (e.g. a local variable or member sharing a macro's name).

| | count |
|---|---|
| used in v6.17 | 1059 |
| used in v6.18 | 1059 |
| newly used | 1 |
| no longer used | 0 |
| likely renames | 0 |
| macro/inline signature changed | 0 |
| macro body changed | 2 |
| moved to another header | 0 |

### Likely renames (header)

None.

### Newly used (header)

| name | kind | header | signature | used by |
|---|---|---|---|---|
| `of_reserved_mem_region_to_resource` | inline | include/linux/of_reserved_mem.h | `int(const struct device_node *np, unsigned int idx, struct resource *res)` | ath11k |

### No longer used (header)

None.

### Signature changed (header)

None.

<details><summary>Macro body changed (2)</summary>

| macro | header | v6.17 | v6.18 |
|---|---|---|---|
| `DMA_BIT_MASK` | include/linux/dma-mapping.h | `(((n) == 64) ? ~0ULL : ((1ULL<<(n))-1))` | `GENMASK_ULL(n - 1, 0)` |
| `MODULE_DEVICE_TABLE` | include/linux/module.h | `static typeof(name) __mod_device_table__##type##__##name __attribute__ ((used, alias(__stringify(name))))` | `static typeof(name) __mod_device_table(type, name) __attribute__ ((used, alias(__stringify(name))))` |

</details>

## Same interface, different set of users

| symbol | v6.17 | v6.18 |
|---|---|---|
| `__dma_sync_single_for_cpu` | ath10k_pci,ath11k,ath12k,iwlwifi,mt76,rtw88_pci,rtw89_pci | ath10k_pci,ath11k,ath12k,iwlwifi,mt76,mt7996e,rtw88_pci,rtw89_pci |
| `__dma_sync_single_for_device` | ath10k_core,ath10k_pci,ath11k,iwlwifi,mt76,rtw88_pci,rtw89_pci | ath10k_core,ath10k_pci,ath11k,iwlwifi,mt76,mt7996e,rtw88_pci,rtw89_pci |
| `__sw_hweight32` | amdgpu,drm_display_helper,drm,drm_kms_helper,i915,radeon,xe,ath10k_core,ath11k,ath12k,iwlwifi,iwlmld,iwlmvm,mt76,mt76-connac-lib,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw88_core,rtw89_core | amdgpu,drm_display_helper,drm,drm_kms_helper,i915,radeon,xe,ath10k_core,ath11k,ath12k,iwlwifi,iwlmld,iwlmvm,mt76,mt76-connac-lib,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw88_core,rtw89_core,rtw89_pci |
| `__x86_indirect_thunk_r9` | amdgpu,drm,drm_gpuvm,i915,xe,ath11k,ath12k,mt76,mt7996e,rtw88_8822b,rtw88_8822c,rtw89_core,rtw89_pci | amdgpu,drm,drm_gpuvm,i915,xe,ath11k,ath12k,mt76,mt7996e,rtw88_8822b,rtw88_8822c,rtw89_core |
| `__x86_indirect_thunk_rcx` | amdgpu,drm,drm_kms_helper,i915,radeon,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt7615-common,mt7915e,mt7925-common,mt7925e,mt7996e,rtw88_8723d,rtw88_8814a,rtw88_8821c,rtw88_8822b,rtw88_8822c,rtw88_core,rtw88_pci,rtw89_8922a,rtw89_core,rtw89_pci | amdgpu,drm,drm_kms_helper,i915,radeon,gpu-sched,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt7615-common,mt7915e,mt7925-common,mt7925e,mt7996e,rtw88_8723d,rtw88_8814a,rtw88_8821c,rtw88_8822b,rtw88_8822c,rtw88_core,rtw88_pci,rtw89_8922a,rtw89_core,rtw89_pci |
| `_raw_spin_lock` | amdgpu,drm,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76 | amdgpu,drm,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7996e |
| `_raw_spin_unlock` | amdgpu,drm,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76 | amdgpu,drm,drm_gpuvm,drm_kms_helper,drm_suballoc_helper,i915,radeon,gpu-sched,ttm,xe,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7996e |
| `complete` | amdgpu,ath10k_core,ath11k,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,mt76,rtw88_core,rtw89_core,rtw89_pci | amdgpu,ath10k_core,ath11k,ath12k,brcmfmac,brcmfmac-cyw,iwlwifi,mt76,rtw88_core,rtw89_core |
| `complete_all` | drm,drm_kms_helper,i915,gpu-sched,xe,ath11k,ath12k,brcmfmac,rtw88_core,rtw89_core | drm,drm_kms_helper,i915,gpu-sched,xe,ath11k,ath12k,brcmfmac,rtw88_core,rtw89_core,rtw89_pci |
| `completion_done` | xe,ath10k_core,ath11k,ath12k | xe,ath10k_core,ath11k,ath12k,rtw89_core |
| `iounmap` | amdgpu,i915,radeon,ttm,xe,ath11k,ath12k,brcmfmac | amdgpu,i915,radeon,ttm,ath11k,ath12k,brcmfmac |
| `jiffies_to_msecs` | amdgpu,i915,radeon,xe,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt7615-common,mt7921-common,mt7925-common,mt792x-lib | amdgpu,i915,radeon,xe,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt7615-common,mt7921-common,mt7925-common,mt792x-lib,rtw89_core |
| `mutex_lock` | amdgpu,drm_display_helper,drm,drm_kms_helper,i915,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7615e,mt7915e,mt7921-common,mt7921e,mt7925-common,mt7925e,mt792x-lib,mt7996e,rtw88_core,rtw88_pci,rtw89_8851b,rtw89_8852a,rtw89_8852b,rtw89_8852b_common,rtw89_8852bt,rtw89_8852c,rtw89_8922a,rtw89_core | amdgpu,amdxcp,drm_display_helper,drm,drm_kms_helper,i915,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7615e,mt7915e,mt7921-common,mt7921e,mt7925-common,mt7925e,mt792x-lib,mt7996e,rtw88_core,rtw88_pci,rtw89_8851b,rtw89_8852a,rtw89_8852b,rtw89_8852b_common,rtw89_8852bt,rtw89_8852c,rtw89_8922a,rtw89_core |
| `mutex_unlock` | amdgpu,drm_display_helper,drm,drm_kms_helper,i915,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7615e,mt7915e,mt7921-common,mt7921e,mt7925-common,mt7925e,mt792x-lib,mt7996e,rtw88_core,rtw88_pci,rtw89_8851b,rtw89_8852a,rtw89_8852b,rtw89_8852b_common,rtw89_8852bt,rtw89_8852c,rtw89_8922a,rtw89_core | amdgpu,amdxcp,drm_display_helper,drm,drm_kms_helper,i915,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7615-common,mt7615e,mt7915e,mt7921-common,mt7921e,mt7925-common,mt7925e,mt792x-lib,mt7996e,rtw88_core,rtw88_pci,rtw89_8851b,rtw89_8852a,rtw89_8852b,rtw89_8852b_common,rtw89_8852bt,rtw89_8852c,rtw89_8922a,rtw89_core |
| `page_offset_base` | amdgpu,drm,i915,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7925-common,rtw88_pci,rtw89_pci | amdgpu,drm,i915,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7925-common,mt7996e,rtw88_pci,rtw89_pci |
| `phys_base` | amdgpu,i915,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,rtw88_pci,rtw89_pci | amdgpu,i915,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,mt76,mt7996e,rtw88_pci,rtw89_pci |
| `strncmp` | amdgpu,drm,i915,radeon,ath11k,brcmfmac,iwlwifi | amdgpu,drm,i915,radeon,xe,ath11k,brcmfmac,iwlwifi |
| `system_wq` | amdgpu,drm_display_helper,drm,drm_kms_helper,i915,radeon,gpu-sched,xe,ath11k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt7921-common,mt7925-common,rtw89_core | amdgpu,drm_kms_helper,gpu-sched,xe,iwlmvm,mt7921-common,mt7925-common |
| `vmemmap_base` | amdgpu,drm,i915,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7925-common,rtw88_pci,rtw89_pci | amdgpu,drm,i915,radeon,ttm,xe,ath10k_core,ath10k_pci,ath11k,ath12k,brcmfmac,iwlwifi,iwlmld,iwlmvm,mt76,mt7925-common,mt7996e,rtw88_pci,rtw89_pci |
| `vzalloc_noprof` | amdgpu,radeon,ath10k_core,ath11k_pci,brcmfmac,iwlwifi,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw88_core,rtw89_core | amdgpu,ath10k_core,ath11k_pci,brcmfmac,iwlwifi,mt7615-common,mt7915e,mt7921-common,mt7925-common,mt7996e,rtw88_core,rtw89_core |

