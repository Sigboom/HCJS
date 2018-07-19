<%@ page contentType="text/html;charset=utf-8"%>
<head>
    <jsp:include page="head.jsp"/>
</head>
<html>
    <body bgcolor=yellow>
        <P><font size=2 color=red>This is three.jsp</font>
        <font size=3>
            <% String s=request.getParameter("number");
            out.println("<br>传递过来的值是"+s);
            %>
            <br><img src ="b.jpg" width="<%=s%>" height="<%=s%>"></img>
        </font>
    </body>
</html> 
