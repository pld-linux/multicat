Summary:	Tools to easily and efficiently manipulate multicast streams, incluging MPEG-2 TS
Summary(pl.UTF-8):	Narzędzia do łatwego i wydajnego operowania na strumieniach multicastowych, w tym MPEG-2 TS
Name:		multicat
Version:	2.0
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://download.videolan.org/multicat/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	3aaa226a421c378c2ede0c8db8fd609c
URL:		http://www.videolan.org/projects/multicat.html
BuildRequires:	bitstream
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The multicat package contains a set of tools designed to easily and
efficiently manipulate multicast streams in general, and MPEG-2
Transport Streams (ISO/IEC 13818-1) in particular.

%description -l pl.UTF-8
Pakiet multicat zawiera zestaw narzędzi zaprojektowany w celu
łatwego i wydajnego operowania na strumieniach multicastowych w
ogólności, a w szczególności strumieniach transportowych MPEG-2
(MPEG-2 TS, ISO/IEC 13818-1).

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
LDLIBS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog NEWS README
%attr(755,root,root) %{_bindir}/aggregartp
%attr(755,root,root) %{_bindir}/ingests
%attr(755,root,root) %{_bindir}/lasts
%attr(755,root,root) %{_bindir}/multicat
%attr(755,root,root) %{_bindir}/multicat_validate
%attr(755,root,root) %{_bindir}/offsets
%attr(755,root,root) %{_bindir}/reordertp
%{_mandir}/man1/aggregartp.1*
%{_mandir}/man1/ingests.1*
%{_mandir}/man1/lasts.1*
%{_mandir}/man1/multicat.1*
%{_mandir}/man1/offsets.1*
%{_mandir}/man1/reordertp.1*
