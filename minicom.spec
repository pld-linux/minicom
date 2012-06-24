Summary:	TTY mode communications package ala Telix
Summary(de):	TTY-Modus-Kommunikationspaket (�hnlich Telix)
Summary(es):	Paquete de comunicaciones modo texto a la Telix
Summary(fi):	Tietoliikenneohjelma, kuten Telix
Summary(fr):	Package de communication en mode terminal � la Telix
Summary(pl):	Program komunikacyjny (podobny do Telix-a)
Summary(pt_BR):	Pacote de comunica��es modo texto a la Telix
Summary(ru):	���������������� ����� ���� Telix ��� ���������� ������
Summary(tr):	Telix benzeri, TTY kipi ileti�im paketi
Summary(uk):	����Φ��æ���� ����� ���� Telix ��� ���������� ������
Summary(zh_CN):	һ���ı�����ĵ��Խ�������������ն�ģ������
Name:		minicom
Version:	2.1
Release:	3
License:	GPL v2
Group:		Applications/Communications
Source0:	http://alioth.debian.org/download.php/123/%{name}-%{version}.tar.gz
# Source0-md5:	1c8f3b247c38fb16c3c2170df9fc102a
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	93ca30842bce63473004570b6b30be25
Patch0:		%{name}-fromsnap.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-uninitialized.patch
Patch3:		%{name}-pl_po.patch
Patch4:		%{name}-umask.patch
Patch5:		%{name}-drop-privs.patch
Patch6:		%{name}-check_exec.patch
Patch7:		%{name}-man_no_ko.patch
Patch8:		%{name}-ac25x.patch
Patch9:		%{name}-fi-fix.patch
Patch10:	%{name}-ac254.patch
URL:		http://alioth.debian.org/projects/minicom/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel >= 5.0
Requires:	/usr/bin/tput
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minicom is a communications program that resembles the MSDOS Telix
somewhat. It has a dialing directory, color, full ANSI and VT100
emulation, an (external) scripting language and more.

%description -l de
Minicom ist ein Kommunikationsprogramm, das �hnlichkeiten mit Telix
unter MSDOS aufweist. Es enth�lt ein W�hlverzeichnis, Farbe,
vollst�ndige ANSI- und VT100-Emulation, eine (externe) Scriptsprache
usw.

%description -l es
Minicom es un programa de comunicaci�n que se parece con el Telix del
MSDOS. Tiene un directorio de marcado, color, emulaci�n completa ANSI
y VT100, y un lenguaje externo de sxripts y mail.

%description -l fi
Minicom on MSDOS-Telixi� jossain m��rin muistuttava
tietoliikenneohjelma. Ohjelmassa on mm. puhelinluettelo, v�rit, ANSI-
ja VT100-emulaatiot ja ulkoinen script-kieli.

%description -l fr
Minicom est un programme de communication ressemblant a Telix sous
MSDOS. Il a un r�pertoire de num�rotation, des couleurs, une �mualtion
ANSI et VT100, un langage de script externe et plus encore.

%description -l pl
Minicom jest programem komunikacyjnym, przypominaj�cym DOS-owy program
Telix. Posiada ksi��k� telefoniczn�, emulacj� terminali ANSI i VT100,
zewn�trzny j�zyk skryptowy, obs�ug� kolor�w i wiele innych w�asno�ci.

%description -l pt_BR
Minicom � um programa de comunica��o que parece com o Telix do MSDOS.
Tem um diret�rio de discagem, cor, emula��o completa ANSI e VT100, e
uma linguagem externa de scripts e mail.

%description -l ru
Minicom - ��� ���������������� ���������, � ���-�� ������� �� MSDOS
Telix. ��� �������� ���������� �����, ����, ������ ��������� ANSI �
VT100, ������� ���� �������� � ������ ������.

%description -l tr
Minicom, MSDOS Telix program�na benzeyen bir ileti�im program�d�r.
Numara �evirme dizini, renk, tam ANSI uyumu ve VT100 �yk�n�m� ile
script gibi �zellikleri vard�r.

%description -l uk
Minicom - �� ����Φ��æ��� ��������, ������ ����� �� MSDOS Telix. ����
ͦ����� ��������� �����, ��̦�, ����� Ц������� ANSI �� VT100, ���Φ��
���� �����Ԧ� �� ������ ������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--sysconfdir="%{_sysconfdir}/minicom"

%{__make}
# LIBDIR="%{_sysconfdir}/minicom"

rm -f doc/*.old

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/profile.d,%{_sysconfdir}/minicom} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/locale,%{_mandir}/man1}

%{__make} DESTDIR="$RPM_BUILD_ROOT" \
	LIBDIR="%{_sysconfdir}/minicom" \
	MANDIR="%{_mandir}/man1" install

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/minicom/minirc.dfl
pu minit            ~^M~ATZ^M~
pu mreset           ~^M~ATZ^M~
EOF

cat << EOF > $RPM_BUILD_ROOT/etc/profile.d/minicom.sh
MINICOM="-L"
if [ "`/usr/bin/tput colors`" != "-1" ] ; then
	MINICOM="\$MINICOM -c on"
fi
export MINICOM
EOF

cat << EOF > $RPM_BUILD_ROOT/etc/profile.d/minicom.csh
setenv MINICOM "-L"
if ( "`/usr/bin/tput colors`" != "-1" ) \
	setenv MINICOM "\$MINICOM -c on"
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# Prepare directories with doc files
# (nasty hack to avoid Makefiles & have docs splitted into dirs)
install -d rpm-doc/{extras,doc,tables}
install extras/[hsu]* rpm-doc/extras
install doc/* rpm-doc/doc
install extras/tables/mc* rpm-doc/tables
rm -f rpm-doc/doc/Makefile*

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ja_JP.SJIS
%find_lang minicom

%clean
rm -rf $RPM_BUILD_ROOT

%files -f minicom.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README rpm-doc/{extras,doc,tables}

%attr(750,root,ttyS) %dir %{_sysconfdir}/minicom
%attr(640,root,ttyS) %config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/minicom/*
%attr(755,root,root) /etc/profile.d/minicom.sh
%attr(755,root,root) /etc/profile.d/minicom.csh

%attr(755,root,root) %{_bindir}/minicom

%attr(755,root,root) %{_bindir}/runscript
%attr(755,root,root) %{_bindir}/xminicom
%attr(755,root,root) %{_bindir}/ascii-xfr

%{_desktopdir}/minicom.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(pl) %{_mandir}/pl/man1/*
