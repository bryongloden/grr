#!/usr/bin/env python
# -*- mode: python; encoding: utf-8 -*-

# Copyright 2011 Google Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""This is a test fixture for client objects.."""



# This dict represents a client VFS. It is a list of (path, attributes) tuples,
# where attributes is a tuple of AFF4 object type and a dict of attributes. All
# strings can contain interpolation strings, and protobufs are encoded in text
# form for readability and interpolation-ability.
VFS = [
    ("/", ("VFSGRRClient", {
        "metadata:hostname": "Host%(client_id)s",
        "metadata:system": "Windows",
        "metadata:os_release": "7",
        "metadata:os_version": "6.1.7600",
        "metadata:uname": "Windows-6.1.7600-7",
        "metadata:clock": "1308864467329740",
        "metadata:install_date": "1303680521557627",
        "aff4:directory_listing": """
children {
  path: "fs"
  st_mode: 16877
  st_ino: 1026248
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 4874
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
"""
        })),
    (u"/fs", ("VFSDirectory", {
        "aff4:directory_listing": u"""
children {
  path: "os"
  st_mode: 16877
  st_ino: 106118
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 4874
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
"""
        })),
    (u"/fs/os", ("VFSDirectory", {
        "aff4:directory_listing": u"""
children {
  path: "c"
  st_mode: 16877
  st_ino: 10268
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 4874
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
"""
        })),
    (u"/fs/os/c", ("VFSDirectory", {
        "aff4:directory_listing": u"""
children {
  path: "中国新闻网新闻中"
  st_mode: 16877
  st_ino: 1026118
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 4874
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bin %(client_id)s"
  st_mode: 16877
  st_ino: 1026118
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 4874
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
"""
        })),
    (u"/fs/os/c/中国新闻网新闻中", ("VFSDirectory", {
        "aff4:directory_listing": """
children {
  path: "bzcmp"
  st_mode: 33261
  st_ino: 1026148
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 4874
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
"""
        })),
    ("/fs/os/c/bin %(client_id)s", ("VFSDirectory", {
        "aff4:directory_listing": """
children {
  path: "bzcmp"
  st_mode: 33261
  st_ino: 1026180
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 2140
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "csh"
  st_mode: 33261
  st_ino: 1026157
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 150592
  st_atime: 1299502220
  st_mtime: 1247833437
  st_ctime: 1299502221
  st_blocks: 304
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ypdomainname"
  st_mode: 33261
  st_ino: 1026209
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 14736
  st_atime: 1299502220
  st_mtime: 1268260136
  st_ctime: 1299502221
  st_blocks: 32
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ls"
  st_mode: 33261
  st_ino: 1026249
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 114032
  st_atime: 1308964882
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 232
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "run-parts"
  st_mode: 33261
  st_ino: 1026193
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 19208
  st_atime: 1308993422
  st_mtime: 1260277502
  st_ctime: 1299502221
  st_blocks: 40
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "egrep"
  st_mode: 33261
  st_ino: 1026253
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 105688
  st_atime: 1308964880
  st_mtime: 1267767223
  st_ctime: 1299502221
  st_blocks: 216
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "nc"
  st_mode: 33261
  st_ino: 1026248
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 31296
  st_atime: 1308964808
  st_mtime: 1266733955
  st_ctime: 1299502221
  st_blocks: 64
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "nano"
  st_mode: 33261
  st_ino: 1026214
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 191976
  st_atime: 1301488817
  st_mtime: 1265074241
  st_ctime: 1299502221
  st_blocks: 384
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bsd-csh"
  st_mode: 33261
  st_ino: 1026157
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 150592
  st_atime: 1299502220
  st_mtime: 1247833437
  st_ctime: 1299502221
  st_blocks: 304
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zfgrep"
  st_mode: 33261
  st_ino: 1026244
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 64
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zsh"
  st_mode: 33261
  st_ino: 1026199
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 675792
  st_atime: 1299502220
  st_mtime: 1271643982
  st_ctime: 1299502221
  st_blocks: 1328
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zgrep"
  st_mode: 33261
  st_ino: 1026262
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 5597
  st_atime: 1309035964
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ntfs-3g"
  st_mode: 33261
  st_ino: 1026171
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 52832
  st_atime: 1308269351
  st_mtime: 1269527574
  st_ctime: 1299502221
  st_blocks: 112
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "kbd_mode"
  st_mode: 33261
  st_ino: 1026231
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10464
  st_atime: 1308269352
  st_mtime: 1268404152
  st_ctime: 1299502221
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "mt-gnu"
  st_mode: 33261
  st_ino: 1026258
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 39880
  st_atime: 1299502220
  st_mtime: 1267760625
  st_ctime: 1299502221
  st_blocks: 80
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "less"
  st_mode: 33261
  st_ino: 1026242
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 149496
  st_atime: 1309027569
  st_mtime: 1257411121
  st_ctime: 1299502221
  st_blocks: 304
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "lesskey"
  st_mode: 33261
  st_ino: 1026161
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 15840
  st_atime: 1299502220
  st_mtime: 1257411121
  st_ctime: 1299502221
  st_blocks: 32
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "vdir"
  st_mode: 33261
  st_ino: 1026153
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 114032
  st_atime: 1299502220
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 232
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bzless"
  st_mode: 33261
  st_ino: 1026240
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 1297
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ping6"
  st_mode: 35309
  st_ino: 1026175
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 31448
  st_atime: 1299502220
  st_mtime: 1268394116
  st_ctime: 1299502221
  st_blocks: 64
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ping"
  st_mode: 35309
  st_ino: 1026274
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 35680
  st_atime: 1304668794
  st_mtime: 1268394116
  st_ctime: 1299502221
  st_blocks: 72
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "rbash"
  st_mode: 33261
  st_ino: 1026236
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 934336
  st_atime: 1309007414
  st_mtime: 1271643361
  st_ctime: 1299502221
  st_blocks: 1840
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "chvt"
  st_mode: 33261
  st_ino: 1026176
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10456
  st_atime: 1299502220
  st_mtime: 1268404152
  st_ctime: 1299502221
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "mail"
  st_mode: 33261
  st_ino: 1580605
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 97416
  st_atime: 1309028378
  st_mtime: 1257840311
  st_ctime: 1299502309
  st_blocks: 200
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zmore"
  st_mode: 33261
  st_ino: 1026275
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 2416
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "usleep"
  st_mode: 33261
  st_ino: 1026218
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 35720
  st_atime: 1299502220
  st_mtime: 1265928226
  st_ctime: 1299502221
  st_blocks: 72
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "gzip"
  st_mode: 33261
  st_ino: 1026252
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 64168
  st_atime: 1309035805
  st_mtime: 1282034617
  st_ctime: 1299502221
  st_blocks: 136
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bzip2recover"
  st_mode: 33261
  st_ino: 1026203
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10392
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ps"
  st_mode: 33261
  st_ino: 1026277
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 101232
  st_atime: 1308964867
  st_mtime: 1260992083
  st_ctime: 1299502221
  st_blocks: 208
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "rzsh"
  st_mode: 33261
  st_ino: 1026199
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 675792
  st_atime: 1299502220
  st_mtime: 1271643982
  st_ctime: 1299502221
  st_blocks: 1328
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "dnsdomainname"
  st_mode: 33261
  st_ino: 1026238
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 14736
  st_atime: 1299502220
  st_mtime: 1268260136
  st_ctime: 1299502221
  st_blocks: 32
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "dbus-uuidgen"
  st_mode: 33261
  st_ino: 1026304
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10424
  st_atime: 1303294484
  st_mtime: 1299262962
  st_ctime: 1301187156
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "chown"
  st_mode: 33261
  st_ino: 1026206
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 64144
  st_atime: 1308959430
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 136
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ksh"
  st_mode: 33261
  st_ino: 1026210
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 1322432
  st_atime: 1299502220
  st_mtime: 1244469385
  st_ctime: 1299502221
  st_blocks: 2592
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "setfont"
  st_mode: 33261
  st_ino: 1026219
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 39808
  st_atime: 1308269352
  st_mtime: 1268404152
  st_ctime: 1299502221
  st_blocks: 80
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "true"
  st_mode: 33261
  st_ino: 1026241
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 35216
  st_atime: 1308899805
  st_mtime: 1285093976
  st_ctime: 1299502221
  st_blocks: 72
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "mv"
  st_mode: 33261
  st_ino: 1026181
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 97352
  st_atime: 1309005675
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 200
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zforce"
  st_mode: 33261
  st_ino: 1026190
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 2015
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "mknod"
  st_mode: 33261
  st_ino: 1026163
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 43488
  st_atime: 1299502220
  st_mtime: 1285093976
  st_ctime: 1299502221
  st_blocks: 88
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "nc.openbsd"
  st_mode: 33261
  st_ino: 1026248
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 31296
  st_atime: 1308964808
  st_mtime: 1266733955
  st_ctime: 1299502221
  st_blocks: 64
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "dmesg"
  st_mode: 33261
  st_ino: 1026149
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10432
  st_atime: 1307481506
  st_mtime: 1295553385
  st_ctime: 1299502221
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "which"
  st_mode: 33261
  st_ino: 1026179
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 946
  st_atime: 1309030669
  st_mtime: 1260277502
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "mt"
  st_mode: 33261
  st_ino: 1026258
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 39880
  st_atime: 1299502220
  st_mtime: 1267760625
  st_ctime: 1299502221
  st_blocks: 80
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "lessfile"
  st_mode: 33261
  st_ino: 1026228
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 6947
  st_atime: 1309030099
  st_mtime: 1257411119
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zless"
  st_mode: 33261
  st_ino: 1026185
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 1733
  st_atime: 1309035816
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zdiff"
  st_mode: 33261
  st_ino: 1026208
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 4424
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "static-sh"
  st_mode: 33261
  st_ino: 1026159
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 1841392
  st_atime: 1299502220
  st_mtime: 1271966876
  st_ctime: 1299502221
  st_blocks: 3608
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ulockmgr_server"
  st_mode: 33261
  st_ino: 1026309
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 14712
  st_atime: 1299502828
  st_mtime: 1297456930
  st_ctime: 1299502844
  st_blocks: 32
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bzfgrep"
  st_mode: 33261
  st_ino: 1026182
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 3642
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ksh93"
  st_mode: 33261
  st_ino: 1026210
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 1322432
  st_atime: 1299502220
  st_mtime: 1244469385
  st_ctime: 1299502221
  st_blocks: 2592
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ntfs-3g.usermap"
  st_mode: 33261
  st_ino: 1026281
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 14640
  st_atime: 1299502220
  st_mtime: 1269527574
  st_ctime: 1299502221
  st_blocks: 32
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "cp"
  st_mode: 33261
  st_ino: 1026260
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 109648
  st_atime: 1308964880
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 224
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bzcat"
  st_mode: 33261
  st_ino: 1026224
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 31176
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 64
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "mount"
  st_mode: 35309
  st_ino: 1026189
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 82256
  st_atime: 1308964262
  st_mtime: 1295553386
  st_ctime: 1299502221
  st_blocks: 176
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ln"
  st_mode: 33261
  st_ino: 1026245
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 55912
  st_atime: 1309027978
  st_mtime: 1285093976
  st_ctime: 1299502221
  st_blocks: 120
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bash"
  st_mode: 33261
  st_ino: 1026236
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 934336
  st_atime: 1309007414
  st_mtime: 1271643361
  st_ctime: 1299502221
  st_blocks: 1840
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "mkdir"
  st_mode: 33261
  st_ino: 1026184
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 43600
  st_atime: 1308964874
  st_mtime: 1285093976
  st_ctime: 1299502221
  st_blocks: 88
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "login"
  st_mode: 33261
  st_ino: 1026186
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 44992
  st_atime: 1299602124
  st_mtime: 1297721498
  st_ctime: 1299502221
  st_blocks: 88
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "uname"
  st_mode: 33261
  st_ino: 1026280
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 39360
  st_atime: 1309034899
  st_mtime: 1285093976
  st_ctime: 1299502221
  st_blocks: 80
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "znew"
  st_mode: 33261
  st_ino: 1026264
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 4952
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "setupcon"
  st_mode: 33261
  st_ino: 1026169
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10017
  st_atime: 1299502220
  st_mtime: 1272143857
  st_ctime: 1299502221
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "lessecho"
  st_mode: 33261
  st_ino: 1026255
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10504
  st_atime: 1299502220
  st_mtime: 1257411121
  st_ctime: 1299502221
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "umount"
  st_mode: 35309
  st_ino: 1026230
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 56680
  st_atime: 1308960934
  st_mtime: 1295553386
  st_ctime: 1299502221
  st_blocks: 120
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ntfs-3g.probe"
  st_mode: 33261
  st_ino: 1026276
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10432
  st_atime: 1299502220
  st_mtime: 1269527574
  st_ctime: 1299502221
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "sed"
  st_mode: 33261
  st_ino: 1026261
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 69088
  st_atime: 1309033744
  st_mtime: 1261435126
  st_ctime: 1299502221
  st_blocks: 144
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "cpio"
  st_mode: 33261
  st_ino: 1026269
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 129320
  st_atime: 1308269353
  st_mtime: 1267760625
  st_ctime: 1299502221
  st_blocks: 264
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "cat"
  st_mode: 33261
  st_ino: 1026267
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 60064
  st_atime: 1308964274
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 128
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zcmp"
  st_mode: 33261
  st_ino: 1026234
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 69
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "plymouth"
  st_mode: 33261
  st_ino: 1026227
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 35416
  st_atime: 1308269348
  st_mtime: 1290547719
  st_ctime: 1299502221
  st_blocks: 72
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bzgrep"
  st_mode: 33261
  st_ino: 1026182
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 3642
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ntfs-3g.secaudit"
  st_mode: 33261
  st_ino: 1026257
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 55848
  st_atime: 1299502220
  st_mtime: 1269527574
  st_ctime: 1299502221
  st_blocks: 120
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "domainname"
  st_mode: 33261
  st_ino: 1026239
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 14736
  st_atime: 1299502220
  st_mtime: 1268260136
  st_ctime: 1299502221
  st_blocks: 32
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "fgconsole"
  st_mode: 33261
  st_ino: 1026155
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10464
  st_atime: 1299502220
  st_mtime: 1268404152
  st_ctime: 1299502221
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bunzip2"
  st_mode: 33261
  st_ino: 1026162
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 31176
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 64
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bzdiff"
  st_mode: 33261
  st_ino: 1026180
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 2140
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "gunzip"
  st_mode: 33261
  st_ino: 1026197
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 63
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "mktemp"
  st_mode: 33261
  st_ino: 1026256
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 43600
  st_atime: 1308964808
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 88
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "su"
  st_mode: 35309
  st_ino: 1026154
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 36864
  st_atime: 1299502220
  st_mtime: 1297721498
  st_ctime: 1299502221
  st_blocks: 72
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "lesspipe"
  st_mode: 33261
  st_ino: 1026228
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 6947
  st_atime: 1309030099
  st_mtime: 1257411119
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "kill"
  st_mode: 33261
  st_ino: 1026173
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 18800
  st_atime: 1308917167
  st_mtime: 1260992083
  st_ctime: 1299502221
  st_blocks: 40
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "tar"
  st_mode: 33261
  st_ino: 1026207
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 344688
  st_atime: 1309028185
  st_mtime: 1284997756
  st_ctime: 1299502221
  st_blocks: 688
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "dumpkeys"
  st_mode: 33261
  st_ino: 1026156
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 82184
  st_atime: 1299502220
  st_mtime: 1268404152
  st_ctime: 1299502221
  st_blocks: 176
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "grep"
  st_mode: 33261
  st_ino: 1026235
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 113912
  st_atime: 1309015591
  st_mtime: 1267767223
  st_ctime: 1299502221
  st_blocks: 232
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "mountpoint"
  st_mode: 33261
  st_ino: 1026212
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10328
  st_atime: 1308353857
  st_mtime: 1307651435
  st_ctime: 1308353813
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "unicode_start"
  st_mode: 33261
  st_ino: 1026243
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 2762
  st_atime: 1299502220
  st_mtime: 1268404143
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "pidof"
  st_mode: 33261
  st_ino: 1286783
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 18776
  st_atime: 1308899687
  st_mtime: 1307651432
  st_ctime: 1308353809
  st_blocks: 40
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "touch"
  st_mode: 33261
  st_ino: 1026177
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 60016
  st_atime: 1308928450
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 128
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "rnano"
  st_mode: 33261
  st_ino: 1026214
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 191976
  st_atime: 1301488817
  st_mtime: 1265074241
  st_ctime: 1299502221
  st_blocks: 384
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "netcat"
  st_mode: 33261
  st_ino: 1026248
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 31296
  st_atime: 1308964808
  st_mtime: 1266733955
  st_ctime: 1299502221
  st_blocks: 64
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "openvt"
  st_mode: 33261
  st_ino: 1026168
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 14752
  st_atime: 1299502220
  st_mtime: 1268404152
  st_ctime: 1299502221
  st_blocks: 32
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "rmdir"
  st_mode: 33261
  st_ino: 1026196
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 39392
  st_atime: 1308899813
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 80
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "loadkeys"
  st_mode: 33261
  st_ino: 1026211
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 111352
  st_atime: 1308269352
  st_mtime: 1268404152
  st_ctime: 1299502221
  st_blocks: 232
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "pwd"
  st_mode: 33261
  st_ino: 1026167
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 39472
  st_atime: 1308899801
  st_mtime: 1285093976
  st_ctime: 1299502221
  st_blocks: 80
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "dash"
  st_mode: 33261
  st_ino: 1026266
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 101608
  st_atime: 1308966651
  st_mtime: 1270164579
  st_ctime: 1299502221
  st_blocks: 208
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "fgrep"
  st_mode: 33261
  st_ino: 1026270
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 64600
  st_atime: 1308353857
  st_mtime: 1267767223
  st_ctime: 1299502221
  st_blocks: 136
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "stty"
  st_mode: 33261
  st_ino: 1026225
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 64048
  st_atime: 1308964982
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 136
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "chgrp"
  st_mode: 33261
  st_ino: 1026265
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 64128
  st_atime: 1306244872
  st_mtime: 1285093976
  st_ctime: 1299502221
  st_blocks: 136
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "echo"
  st_mode: 33261
  st_ino: 1026268
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 39328
  st_atime: 1308964874
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 80
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "gzexe"
  st_mode: 33261
  st_ino: 1026223
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 5874
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "netstat"
  st_mode: 33261
  st_ino: 1026192
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 120184
  st_atime: 1308964271
  st_mtime: 1265937325
  st_ctime: 1299502221
  st_blocks: 248
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "df"
  st_mode: 33261
  st_ino: 1026150
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 76568
  st_atime: 1308964288
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 160
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "nisdomainname"
  st_mode: 33261
  st_ino: 1026229
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 14736
  st_atime: 1299502220
  st_mtime: 1268260136
  st_ctime: 1299502221
  st_blocks: 32
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "dir"
  st_mode: 33261
  st_ino: 1026250
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 114032
  st_atime: 1299502220
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 232
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "readlink"
  st_mode: 33261
  st_ino: 1026278
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 47656
  st_atime: 1309027908
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 96
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "tcsh"
  st_mode: 33261
  st_ino: 1582543
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 378144
  st_atime: 1299502220
  st_mtime: 1269299530
  st_ctime: 1299502322
  st_blocks: 752
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "sh"
  st_mode: 33261
  st_ino: 1026236
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 934336
  st_atime: 1309007414
  st_mtime: 1271643361
  st_ctime: 1299502221
  st_blocks: 1840
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "false"
  st_mode: 33261
  st_ino: 1026195
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 35216
  st_atime: 1299502220
  st_mtime: 1285093976
  st_ctime: 1299502221
  st_blocks: 72
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "lsmod"
  st_mode: 33261
  st_ino: 1026259
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 6152
  st_atime: 1299502220
  st_mtime: 1271219811
  st_ctime: 1299502221
  st_blocks: 16
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zcat"
  st_mode: 33261
  st_ino: 1026158
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 64
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "rm"
  st_mode: 33261
  st_ino: 1026194
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 64208
  st_atime: 1308989582
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 136
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bzip2"
  st_mode: 33261
  st_ino: 1026166
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 31176
  st_atime: 1308928443
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 64
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "chmod"
  st_mode: 33261
  st_ino: 1026273
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 60000
  st_atime: 1309026817
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 128
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "tailf"
  st_mode: 33261
  st_ino: 1026220
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10552
  st_atime: 1299502220
  st_mtime: 1295553385
  st_ctime: 1299502221
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zsh4"
  st_mode: 33261
  st_ino: 1026199
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 675792
  st_atime: 1299502220
  st_mtime: 1271643982
  st_ctime: 1299502221
  st_blocks: 1328
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "tempfile"
  st_mode: 33261
  st_ino: 1026246
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10376
  st_atime: 1306466024
  st_mtime: 1260277502
  st_ctime: 1299502221
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bzegrep"
  st_mode: 33261
  st_ino: 1026182
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 3642
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ip"
  st_mode: 33261
  st_ino: 1026164
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 226568
  st_atime: 1308964271
  st_mtime: 1263802269
  st_ctime: 1299502221
  st_blocks: 456
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "open"
  st_mode: 33261
  st_ino: 1026168
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 14752
  st_atime: 1299502220
  st_mtime: 1268404152
  st_ctime: 1299502221
  st_blocks: 32
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "hostname"
  st_mode: 33261
  st_ino: 1026226
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 14736
  st_atime: 1308955274
  st_mtime: 1268260136
  st_ctime: 1299502221
  st_blocks: 32
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "ed"
  st_mode: 33261
  st_ino: 1026272
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 48840
  st_atime: 1299502220
  st_mtime: 1267762314
  st_ctime: 1299502221
  st_blocks: 96
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "dd"
  st_mode: 33261
  st_ino: 1026152
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 60120
  st_atime: 1307482055
  st_mtime: 1285093976
  st_ctime: 1299502221
  st_blocks: 128
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "dbus-daemon"
  st_mode: 33261
  st_ino: 1026292
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 326784
  st_atime: 1309024234
  st_mtime: 1299262962
  st_ctime: 1301187156
  st_blocks: 648
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "sleep"
  st_mode: 33261
  st_ino: 1026279
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 39376
  st_atime: 1308980105
  st_mtime: 1285093976
  st_ctime: 1299502221
  st_blocks: 80
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "dbus-cleanup-sockets"
  st_mode: 33261
  st_ino: 1026301
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 10520
  st_atime: 1301187151
  st_mtime: 1299262962
  st_ctime: 1301187156
  st_blocks: 24
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "date"
  st_mode: 33261
  st_ino: 1026215
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 68192
  st_atime: 1309034900
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 144
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "fusermount"
  st_mode: 35309
  st_ino: 1026308
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 31384
  st_atime: 1307404930
  st_mtime: 1297456930
  st_ctime: 1299502844
  st_blocks: 64
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "uncompress"
  st_mode: 33261
  st_ino: 1026217
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 63
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "more"
  st_mode: 33261
  st_ino: 1026147
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 35512
  st_atime: 1299502220
  st_mtime: 1295553385
  st_ctime: 1299502221
  st_blocks: 72
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "bzmore"
  st_mode: 33261
  st_ino: 1026240
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 1297
  st_atime: 1299502220
  st_mtime: 1284154642
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "sh.distrib"
  st_mode: 33261
  st_ino: 1026236
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 934336
  st_atime: 1309007414
  st_mtime: 1271643361
  st_ctime: 1299502221
  st_blocks: 1840
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "keyctl"
  st_mode: 33261
  st_ino: 1026191
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 22936
  st_atime: 1299502220
  st_mtime: 1257410882
  st_ctime: 1299502221
  st_blocks: 48
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "sync"
  st_mode: 33261
  st_ino: 1026204
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 35232
  st_atime: 1303294466
  st_mtime: 1285093975
  st_ctime: 1299502221
  st_blocks: 72
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "fuser"
  st_mode: 33261
  st_ino: 1026178
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 31744
  st_atime: 1300397154
  st_mtime: 1263803640
  st_ctime: 1299502221
  st_blocks: 64
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "zegrep"
  st_mode: 33261
  st_ino: 1026183
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 64
  st_atime: 1299502220
  st_mtime: 1282034615
  st_ctime: 1299502221
  st_blocks: 8
  st_blksize: 4096
  st_rdev: 0
}
children {
  path: "busybox"
  st_mode: 33261
  st_ino: 1026159
  st_dev: 51713
  st_nlink: 1
  st_uid: 0
  st_gid: 0
  st_size: 1841392
  st_atime: 1299502220
  st_mtime: 1271966876
  st_ctime: 1299502221
  st_blocks: 3608
  st_blksize: 4096
  st_rdev: 0
}
""",
        })),
    ]
