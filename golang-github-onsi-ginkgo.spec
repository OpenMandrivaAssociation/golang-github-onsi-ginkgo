# http://github.com/onsi/ginkgo

%global goipath         github.com/onsi/ginkgo
%global commit          7f8ab55aaf3b86885aa55b762e803744d1674700


%gometa -i

Name:           %{goname}
Version:        1.1.0
Release:        17%{?dist}
Summary:        A Golang BDD Testing Framework
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml
# Upstream fix for aarch64 a0fde42
Patch1:         0001-Add-linux_arm64-support.patch

%description
%{summary}

%package devel
Summary:       %{summary}

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%patch1 -p1 -b .arm64

%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc CHANGELOG.md README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.1.0-16.git7f8ab55
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.1.0-11
- Add missing Provides
  related: #1214619

* Mon Jan 09 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.1.0-10
- Bump to upstream 7f8ab55aaf3b86885aa55b762e803744d1674700
  related: #1214619

* Tue Aug 09 2016 jchaloup <jchaloup@redhat.com> - 1.1.0-9
- Polish spec file, enable devel and unit-test for epel7
  related: #1214619

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Feb 23 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-7
- Add patch for aarch64
- Use %%license

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 1.1.0-4
- Update spec file to spec-2.0
  related: #1214619

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 jchaloup <jchaloup@redhat.com> - 1.1.0-2
- Bump to upstream 462326b1628e124b23f42e87a8f2750e3c4e2d24
  related: #1214619

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 1.1.0-1
- Bump to upstream dbb5c6caf33238b57facc1d975b1aaca6b90288c
  resolves: #1214619

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git17ea479
- Add buildtime dependency on github.com/onsi/gomega
- Fix installtime dependency on github.com/onsi/gomega
  related: #1148456

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git17ea479
- Bump to upstream 17ea479729ee427265ac1e913443018350946ddf
  related: #1148456

* Mon Oct 13 2014 jchaloup <jchaloup@redhat.com> - 0-0.2.git90d6a47
- BuildArch to ExclusiveArch

* Wed Oct 01 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git90d6a47
- First package for Fedora
