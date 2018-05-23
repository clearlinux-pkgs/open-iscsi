#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : open-iscsi
Version  : 2.0.876
Release  : 27
URL      : https://github.com/open-iscsi/open-iscsi/archive/2.0.876.tar.gz
Source0  : https://github.com/open-iscsi/open-iscsi/archive/2.0.876.tar.gz
Summary  : iSCSI userspace library
Group    : Development/Tools
License  : GPL-2.0
Requires: open-iscsi-bin
Requires: open-iscsi-config
Requires: open-iscsi-lib
Requires: open-iscsi-doc
BuildRequires : open-isns-dev
BuildRequires : openssl-dev
BuildRequires : util-linux-dev
Patch1: systemd-units-with-name-generation.patch
Patch2: 0001-Install-iscsistart.patch
Patch3: 0002-Remove-Werror-from-CFLAGS.patch

%description
=================================================================
Linux* Open-iSCSI

%package autostart
Summary: autostart components for the open-iscsi package.
Group: Default

%description autostart
autostart components for the open-iscsi package.


%package bin
Summary: bin components for the open-iscsi package.
Group: Binaries
Requires: open-iscsi-config

%description bin
bin components for the open-iscsi package.


%package config
Summary: config components for the open-iscsi package.
Group: Default

%description config
config components for the open-iscsi package.


%package dev
Summary: dev components for the open-iscsi package.
Group: Development
Requires: open-iscsi-lib
Requires: open-iscsi-bin
Provides: open-iscsi-devel

%description dev
dev components for the open-iscsi package.


%package doc
Summary: doc components for the open-iscsi package.
Group: Documentation

%description doc
doc components for the open-iscsi package.


%package lib
Summary: lib components for the open-iscsi package.
Group: Libraries

%description lib
lib components for the open-iscsi package.


%prep
%setup -q -n open-iscsi-2.0.876
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527111418
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1527111418
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
cp etc/systemd/* %{buildroot}/usr/lib/systemd/system
ln -s ../iscsid.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
cp utils/iscsi-gen-initiatorname %{buildroot}/usr/bin
chmod +x %{buildroot}/usr/bin/iscsi-gen-initiatorname
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/iscsid.service

%files bin
%defattr(-,root,root,-)
/usr/bin/iscsi-gen-initiatorname
/usr/bin/iscsi-iname
/usr/bin/iscsi_discovery
/usr/bin/iscsi_fw_login
/usr/bin/iscsi_offload
/usr/bin/iscsiadm
/usr/bin/iscsid
/usr/bin/iscsistart
/usr/bin/iscsiuio

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/iscsid.service
/usr/lib/systemd/system/iscsi-gen-initiatorname.service
/usr/lib/systemd/system/iscsid.service
/usr/lib/systemd/system/iscsid.socket

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libopeniscsiusr.so
/usr/lib64/pkgconfig/libopeniscsiusr.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libopeniscsiusr.so.0
/usr/lib64/libopeniscsiusr.so.0.1.0
