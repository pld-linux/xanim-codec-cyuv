Summary:	CYUV codec for XAnim
Summary(pl):	Kodek CYUV dla XAnima
Name:		xanim-codec-cyuv
Version:	1.0
Release:	1
License:	non-distributable, for use with xanim exclusively
Group:		X11/Applications/Graphics
# old dlls at http://xanim.polter.net/dlls/
Source1:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_cyuv_1.0_linuxELFx86c6.tgz
# NoSource1-md5:	afd24beb82bc9a7de51719de32b4970a
Source2:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_cyuv_1.0_linuxELFalphaC6.tgz
# NoSource2-md5:	97329c7d918cc1c6540233ef761e24a2
Source3:	ftp://ftp.informatik.uni-hamburg.de/pub/soft/graphics/xanim/dlls/vid_cyuv_1.0_linuxELFppc.tgz
# NoSource3-md5:	e870727ded8e00832792df24c3fd13a4
NoSource:	1
NoSource:	2
NoSource:	3
URL:		http://xanim.polter.net/
Requires:	xanim >= 1:2920
ExclusiveArch:	%{ix86} alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Creative Technology CYUV codec decompression DLL for XAnim.

%description -l pl
Biblioteka do dekompresji kodeka Creative Technology CYUV dla XAnima.

%prep
%ifarch %{ix86}
%setup -q -c -T -a1
%endif
%ifarch alpha
%setup -q -c -T -a2
%endif
%ifarch ppc
%setup -q -c -T -a3
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xanim

install vid_cyuv_*.xa $RPM_BUILD_ROOT%{_libdir}/xanim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc cyuv.readme
%attr(755,root,root) %{_libdir}/xanim/vid_cyuv_*.xa
