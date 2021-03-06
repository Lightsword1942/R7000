#
# Copyright (c) 2009 Mark Heily <mark@heily.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

Name:       libkqueue
Summary:    Emulates the kqueue and kevent system calls
Version:    1.0.6
Release:    1
License:    BSD
Vendor:     Mark Heily
Group:      System Environment/Libraries
Source0:    %{name}-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Emulates the kqueue and kevent system calls

%prep
%setup -q -n libkqueue-1.0.6

%build
./configure --prefix=/usr
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
gzip $RPM_BUILD_ROOT/usr/share/man/man2/kqueue.2
gzip $RPM_BUILD_ROOT/usr/share/man/man2/kevent.2

%clean
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)

/usr/include/kqueue/sys/event.h
/usr/lib/libkqueue.so
/usr/lib/libkqueue.so.0
/usr/lib/libkqueue.so.0.0
/usr/lib/libkqueue.la
/usr/lib/libkqueue.a
/usr/lib/pkgconfig/libkqueue.pc
/usr/share/man/man2/kqueue.2.gz
/usr/share/man/man2/kevent.2.gz

%changelog
