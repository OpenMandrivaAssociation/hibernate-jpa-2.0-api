%_javapackages_macros
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             hibernate-jpa-2.0-api
Version:          1.0.1
Release:          12.0%{?dist}
Summary:          Java Persistence 2.0 (JSR 317) API


License:          EPL and BSD
URL:              http://www.hibernate.org/

# svn export http://anonsvn.jboss.org/repos/hibernate/jpa-api/tags/hibernate-jpa-2.0-api-1.0.1.Final/ hibernate-jpa-2.0-api-1.0.1.Final
# tar -zcvf hibernate-jpa-2.0-api-1.0.1.Final.tar.gz hibernate-jpa-2.0-api-1.0.1.Final
Source0:          %{name}-%{namedversion}.tar.gz
Patch0:           %{name}-%{namedversion}-encoding.patch
Patch1:           %{name}-%{namedversion}-osgi-manifest.patch

BuildArch:        noarch

Requires:         java
Requires:         jpackage-utils

BuildRequires:    jpackage-utils
BuildRequires:    java-devel
BuildRequires:    maven-local

BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin

%description
Hibernate definition of the Java Persistence 2.0 (JSR 317) API.

%package javadoc
Summary:        Javadocs for %{name}

Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1
%patch1 -p1

%pom_xpath_remove pom:build/pom:extensions

%build
mvn-rpmbuild install javadoc:aggregate

%install
# Fixing wrong-file-end-of-line-encoding
sed -i 's/\r//' target/site/apidocs/jdstyle.css

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp  target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc license.txt

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt
